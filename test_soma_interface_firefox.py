import os
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSomaInterfaceVisivel(unittest.TestCase):

    def setUp(self):
        firefox_options = FirefoxOptions()
        # firefox_options.add_argument("--headless") # Opcional para rodar sem janela
        
        # Instala e obtém o caminho do GeckoDriver (driver do Firefox)
        geckodriver_path = GeckoDriverManager().install()
        service = FirefoxService(executable_path=geckodriver_path)
        
        print(f"GeckoDriver instalado em: {geckodriver_path}")
        self.driver = webdriver.Firefox(service=service, options=firefox_options)
        
        # Ajuste para caminho relativo
        base_dir = os.path.dirname(os.path.abspath(__file__))
        html_file_path = os.path.abspath(os.path.join(base_dir, "soma.html"))
        
        # No Linux/macOS, use file:// + caminho. No Windows, file:/// + caminho.
        prefix = "file://" if os.name != 'nt' else "file:///"
        self.driver.get(f"{prefix}{html_file_path}")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_soma_interface(self):
        input1 = self.driver.find_element(By.ID, "num1")
        input2 = self.driver.find_element(By.ID, "num2")
        botao_soma = self.driver.find_element(By.ID, "somar")
        
        input1.send_keys("5")
        input2.send_keys("3")
        botao_soma.click()

        wait = WebDriverWait(self.driver, 10)
        resultado_div = wait.until(EC.visibility_of_element_located((By.ID, 'resultado')))
        
        wait.until(EC.text_to_be_present_in_element((By.ID, 'resultado'), '8'))
        self.assertEqual(resultado_div.text, "8")

    def test_soma_interface_numeros_negativos(self):
        input1 = self.driver.find_element(By.ID, "num1")
        input2 = self.driver.find_element(By.ID, "num2")
        botao_soma = self.driver.find_element(By.ID, "somar")

        input1.send_keys("-5")
        input2.send_keys("3")
        botao_soma.click()

        wait = WebDriverWait(self.driver, 10)
        resultado_div = wait.until(EC.visibility_of_element_located((By.ID, 'resultado')))
        
        wait.until(EC.text_to_be_present_in_element((By.ID, 'resultado'), '-2'))
        self.assertEqual(resultado_div.text, "-2")

if __name__ == "__main__":
    unittest.main()