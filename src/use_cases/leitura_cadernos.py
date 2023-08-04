from src.utils import manipulacao_pdf
from src.utils import sistema_arquivos
from src.utils import datas
import constantes


class LeituraCadernos:
    def __init__(self) -> None:
        # self.lista_caminhos_arquivos_pdf: list[str] = 
        pass

    def __obter_lista_arquivos(self) -> list[str]:
        return sistema_arquivos.listar_arquivos_diretorio_por_extensao(constantes.CAMINHO_PASTA_DOWNLOADS, 'pdf')
    
    def __obter_conteudo_primeira_pagina_arquivo_pdf(self, caminho_arquivo_pdf: str) -> list[str]:
        return manipulacao_pdf.obter_texto_arquivo_pdf(caminho_arquivo_pdf)[0]
    
    def __encontrar_padrao_numero_processo(self, conteudo_arquivo: str) -> str | None:
        padrao_data_disponibilizacao = manipulacao_pdf.encontrar_padrao_regex_arquivo(conteudo_arquivo, constantes.PADRAO_ENCONTRAR_NUMERO_PROCESSO_DATA)
        if padrao_data_disponibilizacao is None or len(padrao_data_disponibilizacao) == 0:
            print("Padrão não encontrado.")
            return
        return padrao_data_disponibilizacao[0]
    
    def __extrair_numero_processo_data(self, conteudo_arquivo: str) -> tuple[str]:
        texto_numero_processo_data = self.__encontrar_padrao_numero_processo(conteudo_arquivo)
        separador_numero_processo_data = manipulacao_pdf.encontrar_padrao_regex_arquivo(texto_numero_processo_data, 
                                                                                        constantes.PADRAO_SPLIT_DATA_DISPONIBILIZACAO)[0]
        numero_processo, data_distribuicao = texto_numero_processo_data.split(separador_numero_processo_data)
        numero_processo = numero_processo.lstrip('Nº')
        data_distribuicao = datas.converter_formatos_data(data_distribuicao, constantes.FORMATO_DATA_ARQUIVO_ENTRADA, 
                                                          constantes.FORMATO_DATA_ARQUIVO_SAIDA)
        return numero_processo, data_distribuicao
    
    def __deletar_arquivos_resultados(self) -> None:
        sistema_arquivos.remover_arquivo(constantes.CAMINHO_JSON_RESULTADOS)
    
    def __salvar_dados_arquivo(self, numero_processo: str, data_distribuicao: str) -> None:
        dados_atualizados = sistema_arquivos.obter_dados_arquivo_json(constantes.CAMINHO_JSON_RESULTADOS)
        if data_distribuicao in dados_atualizados:
            dados_atualizados[data_distribuicao].extend([numero_processo])
        else:
            dados_atualizados[data_distribuicao] = [numero_processo]
        sistema_arquivos.escrever_dados_arquivo_json(constantes.CAMINHO_JSON_RESULTADOS, dados_atualizados)

    def executar(self) -> None:
        lista_caminhos_arquivos_pdf = self.__obter_lista_arquivos()
        self.__deletar_arquivos_resultados()
        for caminho_pdf in lista_caminhos_arquivos_pdf:
            conteudo_caderno = self.__obter_conteudo_primeira_pagina_arquivo_pdf(caminho_pdf)
            numero_processo, data_distribuicao = self.__extrair_numero_processo_data(conteudo_caderno)
            self.__salvar_dados_arquivo(numero_processo, data_distribuicao)
        # self.__deletar_arquivos_resultados()
