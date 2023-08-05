import sys
from src.use_cases.busca_cadernos import BuscaCadernos
from src.use_cases.leitura_cadernos import LeituraCadernos
from src.use_cases.gera_resultados import GeraResultados
from app.configuracao_logger import get_custom_logger


class Main:
    def __init__(self) -> None:
        self.logger = get_custom_logger()

    def __buscar_cadernos(self) -> None:
        busca_cadernos = BuscaCadernos(self.logger)
        busca_cadernos.executar()

    def __extrair_dados_cadernos(self) -> None:
        leitura_cadernos = LeituraCadernos(self.logger)
        leitura_cadernos.executar()

    def __gerar_resultados(self) -> None:
        gera_resultados = GeraResultados(self.logger)
        gera_resultados.executar()

    def executar(self) -> None:
        self.__buscar_cadernos()
        self.__extrair_dados_cadernos()
        self.__gerar_resultados()
        self.logger.info("Operação finalizada.")
        input("Tecle ENTER para finalizar o programa.")
        sys.exit()


if __name__ == '__main__':
    main = Main()
    main.executar()
