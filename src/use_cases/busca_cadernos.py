from src.utils import navegacao
from src.utils.datas import DatasSemanaAnterior
import constantes


class BuscaCadernos:
    def __init__(self, driver) -> None:
        self.driver = driver
        # self.logger
        self.datas_semana_anterior: dict[str, str] = DatasSemanaAnterior().obter_datas()

    def __acessar_pagina_cadernos(self) -> None:
        navegacao.abrir_url(self.driver, constantes.URL_BUSCA_CADERNO_TRIBUNAL)

    def __preencher_campo_data(self, sufixo_localizador: str, data: str) -> None:
        campo_data = navegacao.esperar_elemento_existir(self.driver, 'id', constantes.BASE_LOCALIZADOR_DATA + sufixo_localizador)
        navegacao.clicar_elemento(campo_data)
        navegacao.limpar_campo(campo_data)
        navegacao.clicar_elemento(campo_data)
        navegacao.enviar_caracteres(campo_data, data)

    def __selecionar_tst(self) -> None:
        selecionador_tribunal = navegacao.encontrar_selecionador(self.driver, constantes.LOCALIZADOR_SELECAO_TRIBUNAL)
        navegacao.selecionar_opcao_por_texto(selecionador_tribunal, constantes.TRIBUNAL)


    def __clicar_botao_pesquisar(self) -> None:
        botao_pesquisar = navegacao.encontrar_elemento(self.driver, 'id', constantes.LOCALIZADOR_BOTAO_PESQUISAR)
        navegacao.clicar_elemento(botao_pesquisar)

    def executar(self) -> None:
        self.__acessar_pagina_cadernos()
        [self.__preencher_campo_data(sufixo, data) for sufixo, data in self.datas_semana_anterior.items()]
        self.__selecionar_tst()
        self.__clicar_botao_pesquisar()
