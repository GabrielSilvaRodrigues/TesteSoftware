FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV WDM_LOG=0

WORKDIR /app

# Dependências de sistema + xvfb (display virtual para testes em modo visível)
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget curl gnupg unzip xvfb xauth ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub \
        | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] \
        http://dl.google.com/linux/chrome/deb/ stable main" \
        > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y --no-install-recommends google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Firefox
RUN apt-get update && apt-get install -y --no-install-recommends firefox-esr \
    && rm -rf /var/lib/apt/lists/*

# Microsoft Edge
RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc \
        | gpg --dearmor > /usr/share/keyrings/microsoft.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] \
        https://packages.microsoft.com/repos/edge stable main" \
        > /etc/apt/sources.list.d/microsoft-edge.list \
    && apt-get update && apt-get install -y --no-install-recommends microsoft-edge-stable \
    && rm -rf /var/lib/apt/lists/*

# Brave Browser
RUN curl -fsS https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg \
        | tee /usr/share/keyrings/brave-browser-archive-keyring.gpg > /dev/null \
    && echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] \
        https://brave-browser-apt-release.s3.brave.com/ stable main" \
        | tee /etc/apt/sources.list.d/brave-browser-release.list \
    && apt-get update && apt-get install -y --no-install-recommends brave-browser \
    && rm -rf /var/lib/apt/lists/*

# Dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Corrige a URL do Edge no webdriver-manager:
# azureedge.net pode ser inacessível em alguns ambientes;
# blob.core.windows.net é o endpoint alternativo oficial da Microsoft.
RUN SITE=$(python -c "import site; print(site.getsitepackages()[0])") \
    && sed -i 's|https://msedgedriver.azureedge.net|https://msedgewebdriverstorage.blob.core.windows.net/edgewebdriver|g' \
       "$SITE/webdriver_manager/microsoft.py" \
    && find "$SITE/webdriver_manager/__pycache__" -name "microsoft*" -delete 2>/dev/null || true

# Pré-aquece o cache dos drivers (Chrome, Firefox, Edge) durante o build
# para evitar downloads em tempo de execução dos testes.
COPY _warmup_drivers.py .
RUN python3 _warmup_drivers.py

COPY . .

CMD ["xvfb-run", "-a", "python3", "-m", "unittest", "discover", \
     "-v", "-p", "test_soma_interface*.py"]
