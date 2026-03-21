import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestContextoGame(unittest.TestCase):
    """Teste do jogo Contexto em https://contexto.me/pt/daily"""


    @classmethod
    def setUpClass(cls):
        """Configuração do Chrome uma única vez"""
        chrome_options = ChromeOptions()
        # Argumentos necessários para rodar em container sem display
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
       
        chromedriver_path = ChromeDriverManager().install()
        service = ChromeService(executable_path=chromedriver_path)
        print(f"\nChromeDriver instalado em: {chromedriver_path}")
       
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        cls.driver.set_page_load_timeout(30)
        cls.driver.implicitly_wait(10)


    @classmethod
    def tearDownClass(cls):
        """Fecha o navegador após todos os testes"""
        cls.driver.quit()


    def setUp(self):
        """Carrega a página antes do teste"""
        try:
            self.driver.get("https://contexto.me/pt/daily")
            time.sleep(3)
            print(f"Página carregada: {self.driver.current_url}")
        except Exception as e:
            print(f"Erro ao carregar página: {e}")
            raise


    def test_submit_cartola_and_validate_expected_format(self):
        """Envia 'cartola', extrai tentativa | palavra | posição e valida formato esperado"""
        wait = WebDriverWait(self.driver, 20)
        input_field = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text'], input"))
        )


        input_field.clear()
        input_field.send_keys("cartola")
        input_field.send_keys(Keys.ENTER)


        wait.until(
            lambda d: "cartola" in d.find_element(By.TAG_NAME, "body").text.lower()
        )


        page_text = self.driver.find_element(By.TAG_NAME, "body").text
        normalized = " ".join(page_text.split()).lower()


        matches = re.findall(r"\b(\d+)\s+cartola\s+(\d+)\b", normalized)
        self.assertTrue(matches, "Não foi possível extrair tentativa e posição para 'cartola'")


        tentativa, posicao = matches[0]
        retorno_formatado = f"{tentativa} | cartola | {posicao}"
        esperado = "1 | cartola | 1"


        print(f"RETORNO_CARTOLA: {retorno_formatado}")
        self.assertEqual(retorno_formatado, esperado)


if __name__ == "__main__":
    unittest.main()
