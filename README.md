# TesteSoftware

Projeto de testes de software com Selenium. Implementa testes de interface para validação de uma aplicação web simples de soma de números com suporte para múltiplos navegadores.

## Pré-requisitos

- Python 3.7+
- Navegador web instalado (Chrome, Firefox, Edge ou Brave)
- Em ambientes Linux sem display gráfico: `xvfb`

## Instalação

### 1. Configurar ambiente virtual (opcional, recomendado)

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate  # Windows
```

### 2. Instalar dependências

```bash
python3 -m pip install -r requirements.txt
```

## Testes

### Executar testes Chrome (padrão)

```bash
xvfb-run -a python3 -m unittest -v test_soma_interface.py
```

### Executar testes com Firefox

Primeiro, instale o Firefox:

```bash
sudo apt-get update && sudo apt-get install -y firefox
```

Depois execute:

```bash
xvfb-run -a python3 -m unittest -v test_soma_interface_firefox.py
```

### Executar testes com Edge

Instale o repositório da Microsoft:

```bash
curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | sudo tee /usr/share/keyrings/microsoft-edge.gpg > /dev/null
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-edge.gpg] https://packages.microsoft.com/repos/edge stable main" | sudo tee /etc/apt/sources.list.d/microsoft-edge.list > /dev/null
```

Instale e execute:

```bash
sudo apt-get update && sudo apt-get install -y microsoft-edge-stable
xvfb-run -a python3 -m unittest -v test_soma_interface_edge.py
```

### Executar testes com Brave

```bash
sudo apt-get install -y brave-browser
xvfb-run -a python3 -m unittest -v test_soma_interface_brave.py
```

## Observações

- **Display virtual (xvfb)**: Em ambientes Linux sem interface gráfica, `xvfb-run -a` fornece um display virtual para a execução dos testes.
- **Navegadores headless**: O código pode ser adaptado para execução headless adicionando a opção `--headless=new` nas ChromeOptions.
- **Timeout de espera**: Os testes usam `WebDriverWait` com timeout explícito para sincronização com elementos da página.
