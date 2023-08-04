from src.utils.config import driver
from src.use_cases.busca_cadernos import BuscaCadernos
from src.use_cases.leitura_cadernos import LeituraCadernos
from constantes import CAMINHO_PASTA_DOWNLOADS


class Main:
    def __init__(self) -> None:
        self.driver = driver.abrir_navegador(CAMINHO_PASTA_DOWNLOADS)

    def __buscar_cadernos(self) -> None:
        busca_cadernos = BuscaCadernos(self.driver)
        busca_cadernos.executar()

    def __extrair_dados_cadernos(self) -> None:
        leitura_cadernos = LeituraCadernos()
        leitura_cadernos.executar()

    def __gerar_resultados(self) -> None:
        pass

    def executar(self) -> None:
        self.__buscar_cadernos()
        self.__extrair_dados_cadernos()
        print("Operação finalizada.")


if __name__ == '__main__':
    main = Main()
    main.executar()
