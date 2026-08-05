from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador_email import NotificadorEmail
from services.servico_emprestimo import ServicoEmprestimo


def test_fluxo_registrar_devolver_com_componentes_reais():
    # Arrange — componentes REAIS (sem dublês): serviço como Subject,
    # com o observer de e-mail real registrado
    repositorio = RepositorioEmprestimo()
    servico = ServicoEmprestimo(repositorio)
    servico.registrar_observer(NotificadorEmail())

    # Act
    sucesso = servico.registrar(1, "Ana", "ana@ufra.edu.br", dias=7)

    # Assert
    assert sucesso is True
    emprestimo = repositorio.buscar_emprestimo(1)
    assert emprestimo is not None
    assert emprestimo.equipamento_id == 1
    assert repositorio.buscar_equipamento(1).disponivel is False
