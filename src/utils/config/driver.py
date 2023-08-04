from selenium import webdriver


def abrir_navegador() -> None:
    return webdriver.Chrome()