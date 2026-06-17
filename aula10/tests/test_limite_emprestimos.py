def test_bloqueia_novo_emprestimo_ao_atingir_o_limite(servico):
    # Arrange — Ana abre 2 empréstimos simultâneos (o limite)
    servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)
    servico.registrar(2, "Ana", "ana@ufra.edu.br", 7)
    # Act / Assert — o 3º empréstimo deve ser bloqueado
    assert servico.registrar(3, "Ana", "ana@ufra.edu.br", 7) is False


def test_emprestimo_devolvido_libera_vaga_no_limite(servico):
    # Arrange — Ana atinge o limite com 2 empréstimos abertos
    servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)
    servico.registrar(2, "Ana", "ana@ufra.edu.br", 7)
    # devolve um -> deve abrir uma vaga
    servico.devolver(1)
    # Act / Assert — com a vaga livre, Ana consegue registrar de novo
    assert servico.registrar(3, "Ana", "ana@ufra.edu.br", 7) is True
