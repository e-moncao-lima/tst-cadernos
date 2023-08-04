from src.utils.config import driver
from src.use_cases.busca_cadernos import BuscaCadernos
import constantes


class Main:
    def __init__(self) -> None:
        self.driver = driver.abrir_navegador()

    def __buscar_cadernos(self) -> None:
        busca_cadernos = BuscaCadernos(self.driver)
        busca_cadernos.executar()

    def __baixar_cadernos(self) -> None:
        pass

    def __ler_cadernos(self) -> None:
        pass

    def __salvar_processos(self) -> None:
        pass

    def __gerar_relatorio_duplicatas(self) -> None:
        pass

    def executar(self) -> None:
        self.__buscar_cadernos()


if __name__ == '__main__':
    main = Main()
    main.executar()