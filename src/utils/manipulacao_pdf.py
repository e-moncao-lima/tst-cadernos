import fitz
import re


def obter_texto_arquivo_pdf(caminho_arquivo_pdf: str) -> list[str]:
    try:
        documento = fitz.open(caminho_arquivo_pdf)
        conteudo_arquivo = []
        for pagina in documento:
            conteudo_arquivo.append(pagina.get_text())
        return conteudo_arquivo
    except:
        print(f"Não foi possível ler o conteúdo do arquivo pdf: {caminho_arquivo_pdf}")


def encontrar_padrao_regex_arquivo(conteudo_arquivo: str, padrao_regex: str) -> str | None:
    return re.findall(padrao_regex, conteudo_arquivo, flags=re.IGNORECASE | re.MULTILINE)


def separar_texto_regex(texto: str, padrao_regex: str) -> list[str] | None:
    return re.split(padrao_regex, texto)
