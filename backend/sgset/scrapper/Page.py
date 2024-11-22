from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        """Navega até uma URL"""
        self.driver.get(url)

    def wait_for_element(self, by, value, timeout=10):
        """Espera por um elemento ser visível na página"""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def get_element_text(self, by, value):
        """Obtém o texto de um elemento"""
        element = self.driver.find_element(by, value)
        return element.text
