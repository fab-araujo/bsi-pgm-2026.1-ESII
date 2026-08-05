from dataclasses import dataclass

from models.multa_strategy import MultaStrategy


@dataclass
class Equipamento:
    """Context do Strategy: recebe a estratégia de multa e delega o cálculo.

    Deixou de ser abstrata na Aula 11 — o que variava por subtipo (o algoritmo
    de multa) agora vive nas estratégias, injetadas pela fábrica.
    """

    id: int
    nome: str
    tipo: str                  # mantido — referenciado por Emprestimo como dado histórico
    multa: MultaStrategy       # a estratégia injetada (sem default: antes de 'disponivel')
    disponivel: bool = True

    def calcular_multa(self, dias_atraso: int) -> float:
        return self.multa.calcular(dias_atraso)


# Subclasses esvaziadas pelo Strategy: viram só rótulos de tipo. Custo
# consciente de trocar herança por composição (a Aula 12 discute por que
# NÃO devem ser "consertadas" — falso positivo de Data Class).
@dataclass
class Notebook(Equipamento):
    pass


@dataclass
class Projetor(Equipamento):
    pass


@dataclass
class Cabo(Equipamento):
    pass
