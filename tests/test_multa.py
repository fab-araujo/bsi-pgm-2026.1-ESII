from multa import calcular_multa_com_carencia


def test_sem_atraso_nao_gera_multa():
    # Arrange / Act
    multa = calcular_multa_com_carencia(dias_atraso=0, valor_dia=10.0)
    # Assert
    assert multa == 0.0
