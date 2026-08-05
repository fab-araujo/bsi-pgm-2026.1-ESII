from dataclasses import dataclass
from datetime import date


@dataclass
class Evento:
    """Evento de domínio emitido pelo ServicoEmprestimo (Subject).

    Substitui o dict da Aula 11 (Replace Primitive with Object): agora o
    contrato dos campos está documentado, a IDE autocompleta e um campo
    digitado errado falha na hora — não em produção.
    """

    tipo: str
    email: str
    data: date | None = None      # usado no emprestimo
    multa: float | None = None    # usado na devolucao
