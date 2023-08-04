import os
import json
from glob import glob


def listar_arquivos_diretorio_por_extensao(caminho_diretorio: str, extensao_arquivos: str = '.*') -> list[str]:
    padrao_extensao_arquivos = rf'{caminho_diretorio}/*{extensao_arquivos}'
    return glob(padrao_extensao_arquivos)


def remover_arquivos_diretorio(caminho_diretorio: str) -> None:
    for arquivo in listar_arquivos_diretorio_por_extensao(caminho_diretorio):
        remover_arquivo(arquivo)


def remover_arquivo(caminho_arquivo: str) -> None:
    try:
        os.remove(caminho_arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado para deletar.")


def obter_dados_arquivo_json(caminho_arquivo_json: str) -> dict:
    try:
        dados_arquivo = {}
        with open(caminho_arquivo_json, '+r') as arquivo:
            dados_arquivo = json.load(arquivo)
        return dados_arquivo
    except FileNotFoundError:
        print("Arquivo não existe.")
        return {}
    

def escrever_dados_arquivo_json(caminho_arquivo_json: str, dicionario_dados: dict[str, str]) -> dict:
    try:
        json_serializado = json.dumps(dicionario_dados, indent=4)
        with open(caminho_arquivo_json, 'w') as arquivo:
            arquivo.write(json_serializado)
    except FileNotFoundError:
        print("Arquivo não existe.")

def atualizar_arquivo_json(caminho_arquivo_json: str, dicionario_dados: dict[str, str]) -> None:
    json_serializado = json.dumps(dicionario_dados, indent=4)
    with open(caminho_arquivo_json, "+w") as arquivo:
        dados_arquivo = json.load(arquivo)
        dados_arquivo.update
        arquivo.write(json_serializado)
