def test_bloqueia_novo_emprestimo_ao_atingir_o_limite(servico):
    # Arrange — Ana abre 2 empréstimos simultâneos (o limite)
    servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)
    servico.registrar(2, "Ana", "ana@ufra.edu.br", 7)
    # Act / Assert — o 3º empréstimo deve ser bloqueado
    assert servico.registrar(3, "Ana", "ana@ufra.edu.br", 7) is False
