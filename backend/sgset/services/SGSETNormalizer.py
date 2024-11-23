from unidecode import unidecode
from sgset.models.day_of_week import DayOfWeek
import pandas as pd

class SGSETNormalizer:

    @staticmethod
    def rename_columns(df_data):
        df_data.columns = df_data.columns.str.replace(" ", "_").str.lower().map(unidecode)
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
            "segunda-feira": r"2ª|segunda",
            "terça-feira": r"3ª|terça",
            "quarta-feira": r"4ª|quarta",
            "quinta-feira": r"5ª|quinta",
            "sexta-feira": r"6ª|sexta",
            "sábado": r"sabado|sábado",
            "domingo": r"domingo"
        }

        # Relationship list
        class_weekdays_relationship = []

        # Identify ids
        for weekday, regex in weekdays_regex.items():
            # Filter row that correspond to regex value
            matches_row = df_data['dia_da_semana'].str.lower().str.contains(regex, na=False)
            print(matches_row)

            # Get weekday ids
            weekday_id = df_weekdays.loc[df_weekdays['name'] == weekday, 'id'].values[0]
            print(weekday_id)

            # Connect class id and weekday id
            class_schedule = df_data.loc[matches_row, ['id']].copy()
            class_schedule['day_of_week'] = weekday_id

            class_weekdays_relationship.append(class_schedule)

        turma_dias_df = pd.concat(class_weekdays_relationship, ignore_index=True)
        turma_dias_df.head()
         

