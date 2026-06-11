import datetime
from dataclasses import dataclass


@dataclass
class Emprestimo:
    id: int
    equipamento_id: int
    equipamento_nome: str
    tipo: str
    usuario_nome: str
    usuario_email: str
    data_emprestimo: datetime.date
    data_devolucao: datetime.date
    devolvido: bool = False
