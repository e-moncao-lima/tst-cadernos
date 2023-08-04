from datetime import datetime, timedelta
from dataclasses import dataclass
from constantes import FORMATO_DATA_STRING


@dataclass
class DatasSemanaAnterior:
    _data_atual: datetime.date = datetime.today()
    data_inicio: datetime.date = _data_atual - timedelta(days=_data_atual.weekday() + 8)
    data_fim: datetime.date = data_inicio + timedelta(days=6)

    def obter_datas(self) -> dict[str, str]:
        return {'Ini': self.data_inicio.strftime(FORMATO_DATA_STRING),
                'Fim': self.data_fim.strftime(FORMATO_DATA_STRING)}
