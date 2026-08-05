from abc import ABC, abstractmethod

from services.evento import Evento


class Observer(ABC):
    """Quem quiser reagir aos eventos do sistema implementa update()."""

    @abstractmethod
    def update(self, evento: Evento) -> None: ...


class Subject:
    """Mantém a lista de observers e anuncia eventos para todos.

    O Subject não conhece nenhum observer concreto — só a abstração.
    Desde a Aula 12 o evento é uma `@dataclass Evento` tipada (o dict
    da Aula 11 era Primitive Obsession, refatorado com
    Replace Primitive with Object).
    """

    def __init__(self):
        self._observers: list[Observer] = []

    def registrar_observer(self, obs: Observer) -> None:
        self._observers.append(obs)

    def notificar(self, evento: Evento) -> None:
        for obs in self._observers:
            obs.update(evento)
