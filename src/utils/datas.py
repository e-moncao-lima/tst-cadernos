from datetime import datetime
import locale


def converter_formatos_data(texto_data: str, formato_data_entrada: str, formato_data_saida: str) -> str:
    locale.setlocale(locale.LC_TIME, 'pt_BR')
    data_traduzida = datetime.strptime(texto_data.lower(), formato_data_entrada)
    return data_traduzida.strftime(formato_data_saida)
