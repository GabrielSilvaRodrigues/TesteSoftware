@echo off
echo Criando ambiente virtual...
python -m venv venv
echo Ativando ambiente e instalando dependencias...
call venv\Scripts\activate
pip install -r testes_automatizados/requirements.txt
echo Pronto! Ambiente configurado.
pause