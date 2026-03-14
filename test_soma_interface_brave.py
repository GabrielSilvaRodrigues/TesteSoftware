import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSomaInterfaceBrave(unittest.TestCase):

    def setUp(self):
        brave_options = ChromeOptions()
        # O segredo está aqui: apontar para o binário do Brave
        brave_options.binary_location = "/usr/bin/brave-browser"
        brave_options.add_argument("--headless=new") 
        brave_options.add_argument("--no-sandbox")
        brave_options.add_argument("--disable-dev-shm-usage")

        # O Brave usa o mesmo ChromeDriver do Chrome
        chromedriver_path = ChromeDriverManager().install()
        service = ChromeService(executable_path=chromedriver_path)
        
        self.driver = webdriver.Chrome(service=service, options=brave_options)
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        html_file_path = os.path.abspath(os.path.join(base_dir, "soma.html"))
        self.driver.get(f"file://{html_file_path}")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_soma_interface(self):
        input1 = self.driver.find_element(By.ID, "num1")
        input2 = self.driver.find_element(By.ID, "num2")
        botao_soma = self.driver.find_element(By.ID, "somar")
        resultado_div = self.driver.find_element(By.ID, "resultado")

        input1.send_keys("5")
        input2.send_keys("3")
        botao_soma.click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.ID, 'resultado'), '8'))
        self.assertEqual(resultado_div.text, "8")

    def test_soma_interface_numeros_negativos(self):
        input1 = self.driver.find_element(By.ID, "num1")
        input2 = self.driver.find_element(By.ID, "num2")
        botao_soma = self.driver.find_element(By.ID, "somar")
        resultado_div = self.driver.find_element(By.ID, "resultado")

        input1.send_keys("-5")
        input2.send_keys("3")
        botao_soma.click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.ID, 'resultado'), '-2'))
        self.assertEqual(resultado_div.text, "-2")

if __name__ == "__main__":
    unittest.main()
