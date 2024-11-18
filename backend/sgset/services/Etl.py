import os
import pandas as pd
import json
import logging

logging.basicConfig(level=logging.INFO)

class ETLProcessor:
    """Class to handle the ETL process for XLS files."""
    
    def __init__(self, destination_folder):
        """_summary_

        Args:
            destination_folder (_type_): _description_
        """
        self.destination_folder = destination_folder
        self.xls_file_path = None
        self.json_file_path = os.path.join(destination_folder, 'dynamic_data.json')

    def find_latest_xls_file(self):
        """Find the most recent XLS/XLSX file in the destination folder."""
        xls_files = [f for f in os.listdir(self.destination_folder) if f.endswith('.xls') or f.endswith('.xlsx')]
        if not xls_files:
            logging.error("Nenhum arquivo XLS encontrado na pasta.")
            return None
        self.xls_file_path = os.path.join(self.destination_folder, xls_files[0])
        return self.xls_file_path

    def split_week_days(self, week_day):
        """_summary_

        Args:
            week_day (_type_): _description_

        Returns:
            _type_: _description_
        """
        if pd.isna(week_day):
            return []
        
        days = week_day.replace('de', '').replace('ao', '').replace('feira', '').split(',')
        days = [day.strip() for day in days if day.strip()]

        result_days = []
        for day in days:
            if '5ª e 6ª' in day:
                result_days.append('5ª')
                result_days.append('6ª')
            else:
                result_days.append(day)

        return result_days

    def convert_to_string(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Returns:
            _type_: _description_
        """
        if isinstance(value, pd.Timestamp):
            return value.strftime('%Y-%m-%d')
        return str(value)

    def perform_etl(self):
        """Execute the ETL process."""
        logging.info("Starting ETL process...")

        xls_path = self.find_latest_xls_file()
        if not xls_path:
            return

        df = pd.read_excel(xls_path)
        json_data = []

        for _, row in df.iterrows():
            entry = {}
            for col in df.columns:
                value = row[col]
                if col == 'Dia da Semana':
                    days = self.split_week_days(value)
                    entry['Dias da Semana'] = days
                else:
                    entry[col] = self.convert_to_string(value)

            json_data.append(entry)

        with open(self.json_file_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)

        logging.info("Dynamic JSON generated successfully!")
        self.cleanup(xls_path)

    def cleanup(self, xls_path):
        """Remove the XLS file after processing."""
        os.remove(xls_path)
        logging.info(f"Temporary XLS file '{xls_path}' deleted.")
