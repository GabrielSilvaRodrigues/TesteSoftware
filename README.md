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

> Observação: o teste abre o Chrome em modo visível. Em Linux/container, `xvfb-run` fornece um display virtual para permitir a execução.
