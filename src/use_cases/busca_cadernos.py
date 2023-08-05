from time import sleep
from src.utils.config import driver
from src.utils import navegacao, sistema_arquivos
from src.entidades.datas import DatasSemanaAnterior
import constantes


class BuscaCadernos:
    def __init__(self) -> None:
        self.driver = driver.abrir_navegador(constantes.CAMINHO_PASTA_DOWNLOADS)
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

    def __esvaziar_pasta_downloads(self) -> None:
        sistema_arquivos.remover_arquivos_diretorio(constantes.CAMINHO_PASTA_DOWNLOADS)

    def __baixar_cadernos(self) -> None:
        botoes_download = navegacao.encontrar_elementos(self.driver, 'xpath', constantes.XPATH_BOTOES_DOWNLOAD)
        if len(botoes_download) == 0:
            print("Nenhum caderno encontrado para download.")
            raise AttributeError("Nenhum caderno encontrado para download.")
        for botao in botoes_download:
            navegacao.clicar_elemento(botao)
            sleep(1)

    def executar(self) -> None:
        self.__acessar_pagina_cadernos()
        [self.__preencher_campo_data(sufixo, data) for sufixo, data in self.datas_semana_anterior.items()]
        self.__selecionar_tst()
        self.__clicar_botao_pesquisar()
        self.__esvaziar_pasta_downloads()
        self.__baixar_cadernos()
