from os.path import join
from src.utils import sistema_arquivos, tratamento_dados
import constantes


class GeraResultados:

    def __init__(self) -> None:
        self.dataframes_por_dia = [tratamento_dados.pd.DataFrame]

    def __obter_arquivo_resultado(self) -> None:
        self.dados_resultado = sistema_arquivos.obter_dados_arquivo_json(constantes.CAMINHO_JSON_RESULTADOS)

    def __gerar_planilha_dia(self, dia: str, processos: list[str]) -> None:
        caminho_arquivo = join(constantes.CAMINHO_PASTA_RESULTADOS, f'{constantes.TRIBUNAL} {dia}.xlsx')
        df_dados = tratamento_dados.criar_dataframe_de_lista(processos, ['Numero Processo'])
        self.dataframes_por_dia.append(df_dados)
        tratamento_dados.salvar_dataframe_excel(df_dados, caminho_arquivo)

    def 

    def executar(self) -> None:
        self.__obter_arquivo_resultado()
        for dia, processos in self.dados_resultado.items():
            self.__gerar_planilha_dia(dia, processos)
