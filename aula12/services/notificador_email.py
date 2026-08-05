from services.evento import Evento
from services.observer import Observer


class NotificadorEmail(Observer):
    """O antigo Notificador, agora um Observer: escuta eventos e envia e-mail.

    Desde a Aula 12 o evento chega tipado (`Evento`): acesso por atributo,
    com contrato documentado — não mais por chave de dict.
    """

    def update(self, evento: Evento) -> None:
        if evento.tipo == "emprestimo":
            print(f"[EMAIL] {evento.email} — empréstimo até {evento.data}")
        elif evento.tipo == "devolucao":
            print(f"[EMAIL] {evento.email} — multa R${evento.multa:.2f}")
        elif evento.tipo == "atraso":
            print(f"[EMAIL] {evento.email} — você está em atraso!")
