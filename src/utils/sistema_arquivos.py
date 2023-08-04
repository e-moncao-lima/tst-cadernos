import os
from glob import glob


def listar_arquivos_diretorio_por_extensao(caminho_diretorio: str, extensao_arquivos: str = '.*') -> list[str]:
    padrao_extensao_arquivos = rf'{caminho_diretorio}/*{extensao_arquivos}'
    return glob(padrao_extensao_arquivos)


def remover_arquivos_diretorio(caminho_diretorio: str) -> None:
    for arquivo in listar_arquivos_diretorio_por_extensao(caminho_diretorio):
        os.remove(arquivo)
