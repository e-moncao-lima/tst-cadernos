import os


TRIBUNAL = 'TST'
CAMINHO_PASTA_DOWNLOADS = os.path.join(os.path.dirname(__file__), 'src', 'temp')

URL_BUSCA_CADERNO_TRIBUNAL = 'https://dejt.jt.jus.br/dejt/f/n/diariocon'
BASE_LOCALIZADOR_DATA = 'corpo:formulario:data'
LOCALIZADOR_SELECAO_TRIBUNAL = 'corpo:formulario:tribunal'
LOCALIZADOR_BOTAO_PESQUISAR = 'corpo:formulario:botaoAcaoPesquisar'
FORMATO_DATA_STRING = '%d%m%Y'

XPATH_BOTOES_DOWNLOAD = '//*[@class="bt af_commandButton"]'