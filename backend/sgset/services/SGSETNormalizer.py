from unidecode import unidecode
import pandas as pd
from decimal import Decimal

from sgset.models.course import CourseModel
from sgset.models.day_of_week import DayOfWeekModel
from sgset.serializers.course_serializer import CourseSerializer


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
        weekdays = DayOfWeekModel.objects.all()
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
        CourseModel.objects.all().delete()
        serializer.is_valid(raise_exception=True)

        return serializer.save()
