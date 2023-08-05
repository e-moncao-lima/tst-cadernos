from os.path import join
from src.utils import sistema_arquivos, tratamento_dados
import constantes


class GeraResultados:
    def __init__(self) -> None:
        self.processos_duplicados: dict = {}

    def __obter_arquivo_resultado(self) -> None:
        self.dados_resultado = sistema_arquivos.obter_dados_arquivo_json(constantes.CAMINHO_JSON_RESULTADOS)

    def __gerar_planilha_dia(self, dia: str, processos: list[str]) -> None:
        caminho_arquivo = join(constantes.CAMINHO_PASTA_RESULTADOS, f'{constantes.TRIBUNAL} {dia}.xlsx')
        df_dados = tratamento_dados.criar_dataframe_de_lista(processos, ['Numero Processo'])
        tratamento_dados.salvar_dataframe_excel(df_dados, caminho_arquivo)

    def __verificar_duplicatas(self) -> None:
        lista_datas_resultado = list(self.dados_resultado.keys())
        lista_valores_resultado = list(self.dados_resultado.values())
        for indice in range(len(lista_valores_resultado)):
            for indice_comparador in range(indice+1, len(lista_valores_resultado)):
                processos_repetidos = set(lista_valores_resultado[indice]).intersection(lista_valores_resultado[indice_comparador])
                if processos_repetidos is None:
                    continue
                datas_coincidentes = {lista_datas_resultado[indice], lista_datas_resultado[indice_comparador]}
                for processo in processos_repetidos:
                    if processo in self.processos_duplicados:
                        self.processos_duplicados[processo] |= datas_coincidentes
                    else:
                        self.processos_duplicados[processo] = datas_coincidentes
        self.processos_duplicados = {processo: ['; '.join(list(datas))] for processo, datas in self.processos_duplicados.items()}

    def __gerar_relatorio_duplicatas(self) -> None:
        df_duplicatas = tratamento_dados.criar_dataframe_de_dicionario(self.processos_duplicados, ['Datas'])
        tratamento_dados.salvar_dataframe_excel(df_duplicatas, constantes.CAMINHO_RELATORIO_DUPLICATAS)

    def executar(self) -> None:
        self.__obter_arquivo_resultado()
        for dia, processos in self.dados_resultado.items():
            self.__gerar_planilha_dia(dia, processos)
        self.__verificar_duplicatas()
        if self.processos_duplicados != {}:
            self.__gerar_relatorio_duplicatas()
