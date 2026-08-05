from abc import ABC, abstractmethod


class MultaStrategy(ABC):
    """Estratégia de cálculo de multa (Strategy).

    Tira o algoritmo de multa da hierarquia de Equipamento: o equipamento
    passa a DELEGAR o cálculo a um objeto trocável. Política nova de multa
    vira uma classe nova aqui — sem tocar no Equipamento (OCP por composição).
    """

    @abstractmethod
    def calcular(self, dias_atraso: int) -> float: ...


class MultaPorDia(MultaStrategy):
    """Multa linear: valor fixo por dia de atraso."""

    def __init__(self, valor_dia: float):
        self.valor_dia = valor_dia

    def calcular(self, dias_atraso: int) -> float:
        return max(0.0, dias_atraso * self.valor_dia)


class MultaProgressiva(MultaStrategy):
    """Multa que dobra o valor-dia após um corte de dias.

    Prova viva do padrão: política nova = classe nova, sem tocar no Context.
    """

    def __init__(self, valor_dia: float, corte: int = 3, fator: float = 2.0):
        self.valor_dia = valor_dia
        self.corte = corte
        self.fator = fator

    def calcular(self, dias_atraso: int) -> float:
        if dias_atraso <= 0:
            return 0.0
        dias_normais = min(dias_atraso, self.corte)
        dias_dobrados = dias_atraso - dias_normais
        return dias_normais * self.valor_dia + dias_dobrados * self.valor_dia * self.fator
