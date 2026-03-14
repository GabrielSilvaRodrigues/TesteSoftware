import os
import unittest
from selenium import webdriver
# Importações alteradas para Edge
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSomaInterfaceVisivel(unittest.TestCase):

    def setUp(self):
        edge_options = EdgeOptions()
        # edge_options.add_argument("--headless=new") # Opcional para rodar sem janela
        
        # Instala e obtém o caminho do EdgeDriver
        edgedriver_path = EdgeChromiumDriverManager().install()
        service = EdgeService(executable_path=edgedriver_path)
        
        print(f"EdgeDriver instalado em: {edgedriver_path}")
        self.driver = webdriver.Edge(service=service, options=edge_options)
        
        # Ajuste para caminho relativo
        base_dir = os.path.dirname(os.path.abspath(__file__))
        html_file_path = os.path.abspath(os.path.join(base_dir, "soma.html"))
        
        # Prefixo de arquivo local
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
        self.assertEqual(resultado_div.text, "-2")

if __name__ == "__main__":
    unittest.main()
