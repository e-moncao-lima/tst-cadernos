import re
from src.utils import manipulacao_pdf
from src.utils import sistema_arquivos
import constantes


class LeituraCadernos:
    def __init__(self) -> None:
        # self.lista_caminhos_arquivos_pdf: list[str] = 
        pass

    def __obter_lista_arquivos(self) -> list[str]:
        return sistema_arquivos.listar_arquivos_diretorio_por_extensao(constantes.CAMINHO_PASTA_DOWNLOADS, 'pdf')
    
    def __obter_conteudo_primeira_pagina_arquivo_pdf(self, caminho_arquivo_pdf: str) -> list[str]:
        return str(manipulacao_pdf.obter_texto_arquivo_pdf(caminho_arquivo_pdf)[0])
    
    def __encontrar_padrao_numero_processo(self, conteudo_arquivo: str) -> str:
        padrao_data_disponibilizacao = manipulacao_pdf.encontrar_padrao_regex_arquivo(conteudo_arquivo, constantes.PADRAO_ENCONTRAR_NUMERO_PROCESSO_DATA)
        if padrao_data_disponibilizacao is None or len(padrao_data_disponibilizacao) == 0:
            print("Padrão não encontrado.")
            return
        return padrao_data_disponibilizacao[0]
    
    def __extrair_numero_processo(self, conteudo_arquivo: str) -> None:
        texto_numero_processo_data = self.__encontrar_padrao_numero_processo(conteudo_arquivo)
        texto_split = manipulacao_pdf.separar_texto_regex(texto_numero_processo_data, constantes.PADRAO_SPLIT_DATA_DISPONIBILIZACAO)
        print(texto_split)


    def executar(self) -> None:
        lista_caminhos_arquivos_pdf = self.__obter_lista_arquivos()
        for caminho_pdf in lista_caminhos_arquivos_pdf:
            conteudo_caderno = self.__obter_conteudo_primeira_pagina_arquivo_pdf(caminho_pdf)
            print(conteudo_caderno)
            self.__extrair_numero_processo(conteudo_caderno)
