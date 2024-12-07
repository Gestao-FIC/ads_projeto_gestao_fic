import os
import logging
from DataDownloader import ConfigLoader, Pipeline
from Etl import ETLProcessor

logging.basicConfig(level=logging.INFO)

class ETLPipelineOrchestrator:
    """Class to orchestrate the ETL and download processes."""
    
    def __init__(self, config_path):
        self.config = ConfigLoader.load_configurations(config_path)
        self.config['download_folder'] = os.path.join(os.path.expanduser("~"), "Downloads")

    def check_for_xls_files(self):
        """Check if there are any XLS/XLSX files in the destination folder."""
        xls_files = [f for f in os.listdir(self.config['destination_folder']) if f.endswith('.xls') or f.endswith('.xlsx')]
        return xls_files

    def run_etl(self):
        """Run the ETL process."""
        logging.info("Arquivo XLS encontrado. Iniciando o processo de ETL.")
        etl_processor = ETLProcessor(self.config['destination_folder'])
        etl_processor.perform_etl()

    def run_download(self):
        """Run the file download process."""
        logging.info("Nenhum arquivo XLS encontrado. Iniciando o download.")
        pipeline = Pipeline(
            url=self.config['url'],
            edge_driver_path=self.config['edge_driver_path'],
            destination_folder=self.config['destination_folder'],
            download_folder=self.config['download_folder'],
            timeout=self.config['timeout']
        )
        pipeline.run()

    def orchestrate(self):
        """Orchestrate the ETL and download processes."""
        if self.check_for_xls_files():
            self.run_etl()
        else:
            self.run_download()
            
            logging.info("Verificando arquivos XLS após o download.")
            if self.check_for_xls_files():
                self.run_etl()
            else:
                logging.error("Nenhum arquivo XLS encontrado após o download.")

def main():
    """Main function to start the orchestration."""
    orchestrator = ETLPipelineOrchestrator('../../config.yaml')
    orchestrator.orchestrate()

if __name__ == "__main__":
    main()
