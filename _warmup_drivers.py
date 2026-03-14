"""Pré-aquece o cache do webdriver-manager durante o build Docker."""
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

drivers = [
    ("Chrome",  ChromeDriverManager),
    ("Firefox", GeckoDriverManager),
    ("Edge",    EdgeChromiumDriverManager),
]

for name, Mgr in drivers:
    try:
        path = Mgr().install()
        print(f"[OK] {name}: {path}")
    except Exception as e:
        print(f"[WARN] {name}: {e}")
