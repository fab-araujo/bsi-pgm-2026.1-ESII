import datetime

import pytest


def test_registrar_devolve_true_quando_equipamento_disponivel(servico):
    # Arrange — equipamento 1 começa disponível no Fake
    # Act
    sucesso = servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)
    # Assert
    assert sucesso is True


def test_registrar_devolve_false_quando_equipamento_indisponivel(servico, repositorio_fake):
    # Arrange — deixa o equipamento 1 indisponível antes de registrar
    repositorio_fake.marcar_indisponivel(1)
    # Act
    sucesso = servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)
    # Assert
    assert sucesso is False


def test_registrar_notifica_usuario_apos_sucesso(servico, notificador_spy):
    # Arrange / Act
    servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)
    # Assert — o Spy (observer) recebeu exatamente um evento de empréstimo
    assert len(notificador_spy.eventos) == 1
    evento = notificador_spy.eventos[0]
    assert evento["tipo"] == "emprestimo"
    assert evento["email"] == "ana@ufra.edu.br"


@pytest.mark.parametrize("equip_id, dias, multa_esperada", [
    (1, 3, 30.0),   # Notebook 10/dia × 3
    (1, 1, 10.0),   # Notebook 10/dia × 1
    (2, 2, 30.0),   # Projetor 15/dia × 2
    (2, 1, 15.0),   # Projetor 15/dia × 1
    (3, 5, 10.0),   # Cabo 2/dia × 5
    (3, 3, 6.0),    # Cabo 2/dia × 3
])
def test_devolver_calcula_multa_correta_para_atraso(
        servico, repositorio_fake, notificador_spy, equip_id, dias, multa_esperada):
    # Arrange — registra e força o atraso retrocedendo a data de devolução
    servico.registrar(equip_id, "Ana", "ana@ufra.edu.br", 7)
    emp = repositorio_fake.buscar_emprestimo(1)
    emp.data_devolucao = datetime.date.today() - datetime.timedelta(days=dias)
    # Act
    servico.devolver(1)
    # Assert — a multa chega ao usuário via evento de devolução
    devolucoes = [e for e in notificador_spy.eventos if e["tipo"] == "devolucao"]
    assert devolucoes[-1]["multa"] == multa_esperada


def test_devolver_marca_equipamento_como_disponivel(servico, repositorio_fake):
    # Arrange — após registrar, o equipamento fica indisponível
    servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)
    assert repositorio_fake.buscar_equipamento(1).disponivel is False
    # Act
    servico.devolver(1)
    # Assert — devolver libera o equipamento
    assert repositorio_fake.buscar_equipamento(1).disponivel is True


def test_devolver_falha_silenciosamente_para_emprestimo_inexistente(servico, notificador_spy):
    # Arrange / Act — empréstimo 999 não existe; não deve lançar exceção
    servico.devolver(999)
    # Assert — nenhum evento de devolução foi emitido
    assert all(e["tipo"] != "devolucao" for e in notificador_spy.eventos)
