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

def load_configurations(config_file):
    """Load configurations from a YAML file.

    Args:
        config_file (str): Path to the YAML configuration file.

    Returns:
        dict: The configurations loaded from the file.
    """
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

def configure_driver(edge_driver_path):
    """Configure and create a Selenium WebDriver for Microsoft Edge.

    Args:
        edge_driver_path (str): Path to the Edge WebDriver executable.

    Returns:
        webdriver.Edge: Configured Edge WebDriver instance.
    """
    service = Service(edge_driver_path)
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

def perform_scraping(driver, url):
    """Navigate to a URL and initiate a file download.

    Args:
        driver (webdriver.Edge): The Selenium WebDriver instance.
        url (str): The URL to navigate to for scraping.

    Raises:
        Exception: If an error occurs while trying to download the file.
    """
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 20)
        download_button = wait.until(EC.element_to_be_clickable((By.ID, 'imgExportarXLS')))
        download_button.click()
        logging.info("Download initiated successfully.")
    except Exception as e:
        logging.error(f"Error trying to download the file: {e}")
        raise

def find_recent_file(download_folder):
    """Find the most recently downloaded file in a specified folder.

    Args:
        download_folder (str): The folder to search for downloaded files.

    Returns:
        str: The path to the most recent file, or None if no files found.
    """
    files = [f for f in os.listdir(download_folder) if not f.endswith('.crdownload')]
    file_paths = [os.path.join(download_folder, file) for file in files]
    return max(file_paths, key=os.path.getctime, default=None)

def move_file(source_file, destination):
    """Move a file from the source location to the destination.

    Args:
        source_file (str): Path to the source file to move.
        destination (str): Path to the destination folder.

    Raises:
        Exception: If moving the file fails.
    """
    shutil.move(source_file, destination)
    logging.info(f"File {os.path.basename(source_file)} moved to {destination} successfully.")

def wait_for_download_completion(download_folder, timeout):
    """Wait until all downloads in the specified folder are complete.

    Args:
        download_folder (str): The folder to monitor for downloads.
        timeout (int): Maximum time to wait for downloads to complete.

    Raises:
        Exception: If the timeout is exceeded before downloads complete.
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

def pipeline_step(url, edge_driver_path, destination_folder, download_folder, timeout):
    """Perform the complete pipeline for scraping and file handling.

    Args:
        url (str): The URL to scrape.
        edge_driver_path (str): Path to the Edge WebDriver executable.
        destination_folder (str): Folder to move the downloaded file to.
        download_folder (str): Folder where files are downloaded.
        timeout (int): Maximum time to wait for the download to complete.

    Raises:
        Exception: If an error occurs during the scraping or file handling process.
    """
    driver = configure_driver(edge_driver_path)
    try:
        perform_scraping(driver, url)
        wait_for_download_completion(download_folder, timeout)
        recent_file = find_recent_file(download_folder)
        if recent_file:
            move_file(recent_file, destination_folder)
        else:
            logging.warning("No file found to move.")
    finally:
        driver.quit()
