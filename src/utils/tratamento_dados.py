import pandas as pd


def criar_dataframe_de_lista(lista_dados: list[str], nome_colunas: list[str]) -> pd.DataFrame:
    return pd.DataFrame(lista_dados, columns=nome_colunas)


def criar_dataframe_de_dicionario(dicionario_dados: dict[str, list[str]], nome_colunas: list[str]) -> pd.DataFrame:
    return pd.DataFrame.from_dict(dicionario_dados, columns=nome_colunas, orient='index')


def salvar_dataframe_excel(dataframe: pd.DataFrame, caminho_arquivo_excel: str, index: bool = False) -> None:
    dataframe.to_excel(caminho_arquivo_excel, index=index)
