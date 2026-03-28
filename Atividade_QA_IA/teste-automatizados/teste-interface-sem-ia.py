import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestFiltroTradicional(unittest.TestCase):
    def setUp(self):
        # Configura o driver automaticamente
        servico = Service(ChromeDriverManager().install())
        opcoes = Options()
        opcoes.add_argument("--headless=new")
        opcoes.add_argument("--no-sandbox")
        opcoes.add_argument("--disable-dev-shm-usage")
        opcoes.add_argument("--disable-gpu")
        opcoes.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(service=servico, options=opcoes)
        
        # Resolve o caminho do HTML relativo ao diretório da atividade
        raiz_atividade = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        caminho_principal = os.path.join(raiz_atividade, "app", "index.html")
        caminho_compat = os.path.join(raiz_atividade, "app", "index-sem-IA.html")
        caminho_file = caminho_principal if os.path.exists(caminho_principal) else caminho_compat

        if not os.path.exists(caminho_file):
            raise FileNotFoundError(
                "Arquivo da interface não encontrado em app/index.html ou app/index-sem-IA.html"
            )

        self.driver.get(f"file:///{caminho_file}")

    def test_ct01_bloqueio_animal_silvestre(self):
        """CT01: Deve bloquear a palavra proibida exata 'Arara-Azul'"""
        driver = self.driver
        campo = driver.find_element(By.ID, "texto-anuncio")
        botao = driver.find_element(By.ID, "btn-publicar")

        campo.send_keys("Vendo Arara-Azul mansa")
        botao.click()

        feedback = driver.find_element(By.ID, "mensagem-feedback").text
        self.assertEqual(feedback, "Conteúdo Bloqueado: Comercialização de animais silvestres é proibida.")

    def test_ct02_falha_por_evasao_pontuacao(self):
        """CT02: Demonstra falha de segurança (Evasão) com 'Ar.ara'"""
        driver = self.driver
        campo = driver.find_element(By.ID, "texto-anuncio")
        botao = driver.find_element(By.ID, "btn-publicar")

        campo.send_keys("Vendo Ar.ara rara")
        botao.click()

        feedback = driver.find_element(By.ID, "mensagem-feedback").text
        
        # Este assert prova que o sistema legado falhou na segurança:
        # Ele permitiu a publicação (contém 'sucesso') mesmo sendo um item proibido.
        self.assertIn("sucesso", feedback.lower())

    def test_ct03_falso_positivo_bloqueio_indevido(self):
        """CT03: Demonstra erro de usabilidade (Falso Positivo) com móvel doméstico"""
        driver = self.driver
        campo = driver.find_element(By.ID, "texto-anuncio")
        botao = driver.find_element(By.ID, "btn-publicar")

        campo.send_keys("Vendo Arara de roupas em aço")
        botao.click()

        feedback = driver.find_element(By.ID, "mensagem-feedback").text
        
        # Aqui provamos que o sistema legado prejudica o usuário comum:
        # Ele bloqueia um móvel doméstico só porque a palavra 'arara' está contida no texto.
        self.assertIn("bloqueado", feedback.lower())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()