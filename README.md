# TesteSoftware
Matéria focada em teste de software.

## Como rodar

1. (Opcional) Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instale as dependências:

```bash
python3 -m pip install -r requirements.txt
```

3. Rode os testes:

```bash
xvfb-run -a python3 -m unittest -v test_soma_interface.py
```

4. Instalar navegadores:

```bash
sudo install -d -m 0755 /etc/apt/keyrings
wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null

# Adiciona o repositório oficial da Mozilla à sua lista de fontes
echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
```


```bash
sudo install -d -m 0755 /etc/apt/keyrings
wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null

# Adiciona o repositório oficial da Mozilla à sua lista de fontes
echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
```
```bash
echo '
Package: *
Pin: origin packages.mozilla.org
Pin-Priority: 1000
' | sudo tee /etc/apt/preferences.d/mozilla

sudo apt-get update && sudo apt-get install -y firefox

firefox --version

sudo apt-get install -y firefox

xvfb-run -a python3 -m unittest -v test_soma_interface_firefox.py
```
5. Para Edge:
```bash

# Garanta que a chave GPG da Microsoft esteja no local correto
curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | sudo tee /usr/share/keyrings/microsoft-edge.gpg > /dev/null

# Adicione o repositório estável do Edge
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-edge.gpg] https://packages.microsoft.com/repos/edge stable main" | sudo tee /etc/apt/sources.list.d/microsoft-edge.list > /dev/null

```

```bash

sudo apt-get update
sudo apt-get install -y microsoft-edge-stable

```

```bash

microsoft-edge --version

```

> Observação: o teste abre o Chrome em modo visível. Em Linux/container, `xvfb-run` fornece um display virtual para permitir a execução.
