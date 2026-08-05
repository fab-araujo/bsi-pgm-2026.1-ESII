from abc import ABC, abstractmethod


class Observer(ABC):
    """Quem quiser reagir aos eventos do sistema implementa update()."""

    @abstractmethod
    def update(self, evento: dict) -> None: ...


class Subject:
    """Mantém a lista de observers e anuncia eventos para todos.

    O Subject não conhece nenhum observer concreto — só a abstração.
    Decisão consciente da Aula 11: o evento é um dict (simplicidade
    proposital para focar no padrão). Isso planta um smell de Primitive
    Obsession que a Aula 12 refatora para uma @dataclass Evento.
    """

    def __init__(self):
        self._observers: list[Observer] = []

    def registrar_observer(self, obs: Observer) -> None:
        self._observers.append(obs)

    def notificar(self, evento: dict) -> None:
        for obs in self._observers:
            obs.update(evento)
