import sys
from src.use_cases.busca_cadernos import BuscaCadernos
from src.use_cases.leitura_cadernos import LeituraCadernos
from src.use_cases.gera_resultados import GeraResultados


class Main:
    def __init__(self) -> None:
        pass

    def __buscar_cadernos(self) -> None:
        busca_cadernos = BuscaCadernos()
        busca_cadernos.executar()

    def __extrair_dados_cadernos(self) -> None:
        leitura_cadernos = LeituraCadernos()
        leitura_cadernos.executar()

    def __gerar_resultados(self) -> None:
        gera_resultados = GeraResultados()
        gera_resultados.executar()

    def executar(self) -> None:
        self.__buscar_cadernos()
        self.__extrair_dados_cadernos()
        self.__gerar_resultados()
        print("Operação finalizada.")
        sys.exit()


if __name__ == '__main__':
    main = Main()
    main.executar()
