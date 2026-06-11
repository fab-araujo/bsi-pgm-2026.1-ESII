from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Equipamento(ABC):
    id: int
    nome: str
    tipo: str          # mantido — referenciado por Emprestimo como dado histórico
    disponivel: bool = True

    @abstractmethod
    def calcular_multa(self, dias_atraso: int) -> float: ...


@dataclass
class Notebook(Equipamento):
    def calcular_multa(self, dias_atraso: int) -> float:
        return max(0.0, dias_atraso * 10.0)


@dataclass
class Projetor(Equipamento):
    def calcular_multa(self, dias_atraso: int) -> float:
        return max(0.0, dias_atraso * 15.0)


@dataclass
class Cabo(Equipamento):
    def calcular_multa(self, dias_atraso: int) -> float:
        return max(0.0, dias_atraso * 2.0)
