from services.observer import Observer


class NotificadorEmail(Observer):
    """O antigo Notificador, agora um Observer: escuta eventos e envia e-mail.

    Quer um log também? Crie um LogObserver. Quer SMS? NotificadorSMS.
    O serviço não muda em nenhum dos casos — é o OCP cumprido.
    """

    def update(self, evento: dict) -> None:
        if evento["tipo"] == "emprestimo":
            print(f"[EMAIL] {evento['email']} — empréstimo até {evento['data']}")
        elif evento["tipo"] == "devolucao":
            print(f"[EMAIL] {evento['email']} — multa R${evento['multa']:.2f}")
        elif evento["tipo"] == "atraso":
            print(f"[EMAIL] {evento['email']} — você está em atraso!")
