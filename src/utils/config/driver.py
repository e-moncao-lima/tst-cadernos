from selenium import webdriver
from selenium.webdriver import ChromeOptions, ChromeService, Chrome
from webdriver_manager.chrome import ChromeDriverManager


def configurar_servico() -> ChromeService:
    return ChromeService(ChromeDriverManager().install())


def configurar_opcoes(caminho_pasta_download: str) -> ChromeOptions:
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : caminho_pasta_download}
    options.add_experimental_option("prefs",prefs)
    return options


def abrir_navegador(caminho_pasta_download: str) -> None:
    options = configurar_opcoes(caminho_pasta_download)
    # servico = configurar_servico()
    return webdriver.Chrome(options=options) #, service=servico)