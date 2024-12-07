from decimal import Decimal
from datetime import datetime
from unidecode import unidecode
import pandas as pd

from sgset.models.course import Course
from sgset.models.day_of_week import DayOfWeek
from sgset.serializers.course_serializer import CourseSerializer
from sgset.serializers.course_class_serializer import CourseClassModelSerializer
from sgset.models.course_class import CourseClass
from sgset.serializers.class_schedule import ClassScheduleSerializer
from sgset.models.class_schedule import ClassSchedule


class SGSETNormalizer:

    @staticmethod
    def rename_columns(df_data):
        df_data.columns = df_data.columns.str.replace(
            " ", "_").str.lower().map(unidecode)
        return df_data

    @staticmethod
    def remove_duplicates(df_data):
        # Remove empty lines
        df_data.dropna(inplace=True)

        # Sort row by start couse day field
        df_data = df_data.sort_values(by='periodo_de')

        # Remove duplicates rows and keep the last
        df_data = df_data.drop_duplicates(subset='turma', keep='last')

        return df_data

    @staticmethod
    def find_dayofweek_fk(df_data):

        # Transform day of week table in dataframe
        weekdays = DayOfWeek.objects.all()
        days_weekdays = list(weekdays.values('id', 'name'))
        df_weekdays = pd.DataFrame(days_weekdays)

        # Regex to identify weekday
        weekdays_regex = {
            "Segunda-feira": r"2ª|segunda",
            "Terça-feira": r"3ª|terça",
            "Quarta-feira": r"4ª|quarta",
            "Quinta-feira": r"5ª|quinta",
            "Sexta-feira": r"6ª|sexta",
            "Sabado": r"sabado|sábado"
        }

        # Relationship list
        class_weekdays_relationship = []

        # Identify ids
        for weekday, regex in weekdays_regex.items():
            # Filter row that correspond to regex value
            matches_row = df_data['dia_da_semana'].str.lower(
            ).str.contains(regex, na=False)

            # Get weekday ids
            weekday_id = df_weekdays.loc[df_weekdays['name']
                                         == weekday, 'id'].values[0]

            # Connect class id and weekday id
            class_schedule = df_data.loc[matches_row, ['class_id']].copy()
            class_schedule['day_of_week_id'] = weekday_id

            class_weekdays_relationship.append(class_schedule)

        return pd.concat(
            class_weekdays_relationship, ignore_index=True)

    @staticmethod
    def persist_class_schedule(df_data):
        # Rename df columns according to model
        column_rename = {
            'class_id': 'class_instance',
            'day_of_week_id': 'day_of_week'
        }
        df_data = df_data.rename(columns=column_rename)

        # Transform dataframe in python dict
        data = df_data.to_dict(orient='records')

        # Save rows in databasel
        serializer = ClassScheduleSerializer(data=data, many=True)
        ClassSchedule.objects.all().delete()
        serializer.is_valid(raise_exception=True)

        return serializer.save()

    @staticmethod
    def persist_course_info(df_data):
        # Select Curso and preco_por_participante column
        df_data = df_data[['curso', 'preco_por_participante']]

        # Remove nullable fields and duplicates
        df_data = df_data.dropna()
        df_data = df_data.drop_duplicates()

        # Rename df columns according to model
        column_rename = {
            'curso': 'name',
            'preco_por_participante': 'price_per_student'
        }
        df_data = df_data.rename(columns=column_rename)

        # Apply lambda function to convert 'price_per_student' column to valid decimal
        df_data['price_per_student'] = df_data['price_per_student'].apply(
            lambda x: Decimal(x.replace(".", "").replace(",", "."))
            if isinstance(x, str) else Decimal(x)
        )

        # Transform dataframe in python dict
        data = df_data.to_dict(orient='records')

        # Persist data
        serializer = CourseSerializer(data=data, many=True)
        Course.objects.all().delete()
        serializer.is_valid(raise_exception=True)

        return serializer.save()

    @staticmethod
    def persist_class_info(df_data):

        # Get unique course names from the 'curso' column of the DataFrame
        courses_names = df_data['curso'].unique()

        # Query the database to get all courses that match the names in 'courses_names'
        courses = Course.objects.filter(name__in=courses_names)
        course_ids_dict = {course.name: course.id for course in courses}

        # Map the 'curso' column to the new 'course' column with course IDs
        df_data['course'] = df_data['curso'].map(
            lambda x: str(course_ids_dict.get(x, "")).replace("-", "")
            if x in course_ids_dict else ""
        )

        # Rename df columns according to model
        column_rename = {
            'turma': 'code',
            'situacao': 'day_of_week',
            'situacao': 'day_of_week',
            'turno': "shift",
            'carga_horaria': 'duration',
            'no_de_matriculas_realizado': 'actual_enrollments',
            'no_de_matriculas_estimado': 'estimated_enrollments',
            'periodo_de': 'period_from',
            'periodo_ate': "period_to",
            'horario_de': 'start_time',
            'horario_ate': 'end_time',
            'dia_da_semana': 'day_of_week',
            'modalidade': 'modality',
            'atendimento': 'attendance',
        }
        df_data = df_data.rename(columns=column_rename)

        df_data['period_from'] = df_data['period_from'].dt.date
        df_data['period_to'] = df_data['period_to'].dt.date

        # Add the 'status' column based on the conditions
        df_data['status'] = df_data.apply(
            lambda row:
                'concluido' if row['period_to'] < datetime.now().date()
                else ('programado' if row['period_to'] > datetime.now().date() else 'em_andamento'),
            axis=1
        )

        # Transform dataframe in python dict
        data = df_data.to_dict(orient='records')

        # Persist data
        serializer = CourseClassModelSerializer(data=data, many=True)
        CourseClass.objects.all().delete()
        serializer.is_valid(raise_exception=True)

        return serializer.save()
