import os


TRIBUNAL = 'TST'
CAMINHO_PASTA_PROJETO = os.path.dirname(__file__)
CAMINHO_PASTA_LOGS = os.path.join(CAMINHO_PASTA_PROJETO, 'app', 'logs')
CAMINHO_PASTA_RESULTADOS = os.path.join(CAMINHO_PASTA_PROJETO, 'resultados')
CAMINHO_PASTA_DOWNLOADS = os.path.join(CAMINHO_PASTA_RESULTADOS, 'arquivos')
CAMINHO_JSON_RESULTADOS = os.path.join(CAMINHO_PASTA_RESULTADOS, 'resultado.json')
CAMINHO_RELATORIO_DUPLICATAS = os.path.join(CAMINHO_PASTA_RESULTADOS, 'relatorio_duplicatas.xlsx')

URL_BUSCA_CADERNO_TRIBUNAL = 'https://dejt.jt.jus.br/dejt/f/n/diariocon'
BASE_LOCALIZADOR_DATA = 'corpo:formulario:data'
LOCALIZADOR_SELECAO_TRIBUNAL = 'corpo:formulario:tribunal'
LOCALIZADOR_BOTAO_PESQUISAR = 'corpo:formulario:botaoAcaoPesquisar'
FORMATO_DATA_STRING = '%d%m%Y'

XPATH_BOTOES_DOWNLOAD = '//*[@class="bt af_commandButton"]'
PADRAO_ENCONTRAR_NUMERO_PROCESSO_DATA = r'n.\s*\d{4}\/\d{4}\s+data\s+da\s+disponibilização:\s+\w+-\w+,\s+\d{1,2}\s+\w+\s+\w+\s+\w+\s+\d{4}'
PADRAO_SPLIT_DATA_DISPONIBILIZACAO = r'\s+data\s+da\s+disponibilização:\s+\w+-*\w+,\s+'
FORMATO_DATA_ARQUIVO_ENTRADA = '%d de %B de %Y'
FORMATO_DATA_ARQUIVO_SAIDA = '%d-%m-%Y'