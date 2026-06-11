import datetime
from abc import ABC, abstractmethod


class INotificador(ABC):
    """Contrato de notificação consumido pelo ServicoEmprestimo (DIP).

    Declara os 3 métodos que o serviço usa. Um dublê de teste
    (ex.: NotificadorSpy) implementa esta interface e o Python
    garante, na instanciação, que nenhum método ficou de fora.
    """

    @abstractmethod
    def notificar_emprestimo(self, email: str, data_devolucao: datetime.date) -> None: ...

    @abstractmethod
    def notificar_devolucao(self, email: str, multa: float) -> None: ...

    @abstractmethod
    def notificar_atraso(self, email: str) -> None: ...
