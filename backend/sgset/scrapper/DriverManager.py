from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class DriverManager:
    def __init__(self):
        self.driver = None

    def start_driver(self):
        """Inicia o WebDriver para o Google Chrome com a configuração correta"""
        options = Options()
        # Executa o navegador sem interface gráfica (opcional)
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        return self.driver

    def stop_driver(self):
        """Fecha o WebDriver"""
        if self.driver:
            self.driver.quit()
            self.driver = None

    def get_driver(self):
        """Retorna a instância do driver"""
        return self.driver
