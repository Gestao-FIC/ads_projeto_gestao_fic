from unidecode import unidecode

class SGSETNormalizer:

    @staticmethod
    def rename_columns(df_data):
        df_data.columns = df_data.columns.str.replace(" ", "_").str.lower().map(unidecode)
        print(df_data.columns)
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
