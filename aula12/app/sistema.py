from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador_email import NotificadorEmail
from services.servico_emprestimo import ServicoEmprestimo


class SistemaDeEmprestimos:
    """Fachada: esconde a montagem do subsistema e expõe operações simples.

    É a raiz de composição: o único lugar que conhece as classes concretas
    e as liga. Desde a Aula 11 é também quem COMPÕE os observers: cria o
    serviço (Subject) e registra os destinos de notificação. Os métodos
    apenas delegam ao serviço — sem regra de negócio aqui, para a fachada
    não virar um God Object.
    """

    def __init__(self):
        self._repositorio = RepositorioEmprestimo()
        self._servico = ServicoEmprestimo(self._repositorio)
        self._servico.registrar_observer(NotificadorEmail())
        # mais destinos? basta registrar mais um observer aqui.

    def registrar(self, equipamento_id, nome, email, dias):
        return self._servico.registrar(equipamento_id, nome, email, dias)

    def devolver(self, emprestimo_id):
        return self._servico.devolver(emprestimo_id)

    def listar_atrasados(self):
        return self._servico.listar_atrasados()
