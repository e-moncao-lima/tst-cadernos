import pandas as pd


def criar_dataframe_de_lista(lista_dados: list[str], nome_colunas: list[str]) -> pd.DataFrame:
    return pd.DataFrame(lista_dados, columns=nome_colunas)


def salvar_dataframe_excel(dataframe: pd.DataFrame, caminho_arquivo_excel: str) -> None:
    dataframe.to_excel(caminho_arquivo_excel)
