from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


def abrir_url(driver, url: str) -> None:
    driver.get(url)


def fechar_navegador(driver) -> None:
    driver.quit()


def encontrar_elemento(driver, logger, tag_elemento: str, nome_elemento: str) -> None:
    try:
        atributo = getattr(By, tag_elemento.upper())
        elemento = driver.find_element(atributo, nome_elemento)
        return elemento
    except:
        logger.error("Elemento não encontrado.")


def encontrar_elementos(driver, logger, tag_elemento: str, nome_elementos: str) -> None:
    try:
        atributo = getattr(By, tag_elemento.upper())
        elementos = driver.find_elements(atributo, nome_elementos)
        return elementos
    except:
        logger.error("Elemento não encontrado.")


def esperar_elemento_existir(driver, logger, tag_elemento: str, nome_elemento: str, tempo_espera: int = 10) -> None:
    try:
        atributo = getattr(By, tag_elemento.upper())
        element = WebDriverWait(driver, tempo_espera).until(
            EC.presence_of_element_located((atributo, nome_elemento))
        )
        return element
    except:
        logger.error("Elemento não encontrado.")


def limpar_campo(logger, webelemento) -> None:
    try:
        webelemento.clear()
    except:
        logger.error("Erro ao limpar campo.")


def enviar_caracteres(logger, webelemento, caracteres: str) -> None:
    try:
        webelemento.send_keys(caracteres)
    except:
        logger.error("Erro ao enviar caracteres para o campo.")


def clicar_elemento(logger, webelemento) -> None:
    try:
        webelemento.click()
    except:
        logger.error("Erro ao clicar em elemento.")


def encontrar_selecionador(driver, logger, nome_elemento: str) -> None:
    elemento = encontrar_elemento(driver, logger, 'id', nome_elemento)
    return Select(elemento)


def selecionar_opcao_por_texto(selecionador: Select, texto: str) -> None:
    selecionador.select_by_visible_text(texto)
