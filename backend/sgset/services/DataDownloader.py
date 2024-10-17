import os
import shutil
import time
import logging
import yaml
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)

class ConfigLoader:
    """Class to load configurations from a YAML file."""
    
    @staticmethod
    def load_configurations(config_file):
        """Loads configurations from a specified YAML file.

        Args:
            config_file (str): Path to the YAML configuration file.

        Returns:
            dict: Parsed configuration data from the YAML file.
        """
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)

class EdgeDriver:
    """Class to configure and create a Selenium WebDriver for Microsoft Edge."""
    
    def __init__(self, edge_driver_path):
        """Initializes the EdgeDriver with the specified driver path.

        Args:
            edge_driver_path (str): Path to the Microsoft Edge WebDriver executable.
        """
        self.edge_driver_path = edge_driver_path
        self.driver = self._configure_driver()

    def _configure_driver(self):
        """Configures and initializes the Edge WebDriver.

        Returns:
            webdriver.Edge: Configured Edge WebDriver instance.
        """
        service = Service(self.edge_driver_path)
        options = Options()
        options.add_argument('--start-maximized')
        prefs = {
            "download.default_directory": os.path.join(os.path.expanduser("~"), "Downloads"),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        options.add_experimental_option("prefs", prefs)
        return webdriver.Edge(service=service, options=options)

    def get_driver(self):
        """Retrieves the configured Edge WebDriver instance.

        Returns:
            webdriver.Edge: The Edge WebDriver instance.
        """
        return self.driver

    def quit(self):
        """Quits the Edge WebDriver, closing all associated windows."""
        self.driver.quit()

class Scraper:
    """Class to perform web scraping and file downloads."""
    
    def __init__(self, driver):
        """Initializes the Scraper with the specified WebDriver.

        Args:
            driver (webdriver.Edge): The Edge WebDriver instance to use for scraping.
        """
        self.driver = driver

    def perform_scraping(self, url):
        """Performs the scraping operation by navigating to the given URL and initiating a download.

        Args:
            url (str): The URL to navigate to for scraping.

        Raises:
            Exception: If there is an error during the scraping or download process.
        """
        try:
            self.driver.get(url)
            wait = WebDriverWait(self.driver, 20)
            download_button = wait.until(EC.element_to_be_clickable((By.ID, 'imgExportarXLS')))
            download_button.click()
            logging.info("Download initiated successfully.")
        except Exception as e:
            logging.error(f"Error trying to download the file: {e}")
            raise

class FileHandler:
    """Class to manage file operations such as moving and finding files."""
    
    @staticmethod
    def find_recent_file(download_folder):
        """Finds the most recently downloaded file in the specified download folder.

        Args:
            download_folder (str): Path to the folder where downloads are stored.

        Returns:
            str: Path to the most recently downloaded file, or None if no file is found.
        """
        files = [f for f in os.listdir(download_folder) if not f.endswith('.crdownload')]
        file_paths = [os.path.join(download_folder, file) for file in files]
        return max(file_paths, key=os.path.getctime, default=None)

    @staticmethod
    def move_file(source_file, destination):
        """Moves a file from the source path to the specified destination.

        Args:
            source_file (str): Path to the source file to be moved.
            destination (str): Path to the destination folder.

        Raises:
            Exception: If the move operation fails.
        """
        shutil.move(source_file, destination)
        logging.info(f"File {os.path.basename(source_file)} moved to {destination} successfully.")

    @staticmethod
    def wait_for_download_completion(download_folder, timeout):
        """Waits for the download to complete, checking for incomplete download files.

        Args:
            download_folder (str): Path to the folder where downloads are stored.
            timeout (int): Maximum time to wait for the download to complete in seconds.

        Raises:
            Exception: If the timeout for completing the download is exceeded.
        """
        while True:
            initial_time = time.time()
            time.sleep(5)
            if not any(f.endswith('.crdownload') for f in os.listdir(download_folder)):
                break
            if time.time() - initial_time > timeout:
                logging.error("Timeout for completing the download exceeded.")
                raise Exception("Timeout for completing the download exceeded.")
            time.sleep(1)

class Pipeline:
    """Class to execute the complete scraping and file handling pipeline."""
    
    def __init__(self, url, edge_driver_path, destination_folder, download_folder, timeout):
        """Initializes the Pipeline with the necessary parameters.

        Args:
            url (str): The URL to scrape.
            edge_driver_path (str): Path to the Microsoft Edge WebDriver executable.
            destination_folder (str): Path to the folder where downloaded files will be moved.
            download_folder (str): Path to the folder where downloads are stored.
            timeout (int): Maximum time to wait for downloads to complete in seconds.
        """
        self.url = url
        self.edge_driver_path = edge_driver_path
        self.destination_folder = destination_folder
        self.download_folder = download_folder
        self.timeout = timeout

    def run(self):
        """Executes the scraping and file handling process."""
        driver_manager = EdgeDriver(self.edge_driver_path)
        driver = driver_manager.get_driver()
        try:
            scraper = Scraper(driver)
            scraper.perform_scraping(self.url)
            FileHandler.wait_for_download_completion(self.download_folder, self.timeout)
            recent_file = FileHandler.find_recent_file(self.download_folder)
            if recent_file:
                FileHandler.move_file(recent_file, self.destination_folder)
            else:
                logging.warning("No file found to move.")
        finally:
            driver_manager.quit()
