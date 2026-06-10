from multa import calcular_multa_com_carencia


def test_sem_atraso_nao_gera_multa():
    # Arrange / Act
    multa = calcular_multa_com_carencia(dias_atraso=0, valor_dia=10.0)
    # Assert
    assert multa == 0.0


def test_cobra_dias_excedentes_alem_da_carencia():
    # 5 dias de atraso, carência de 2 -> cobra 3 dias × 10
    multa = calcular_multa_com_carencia(dias_atraso=5, valor_dia=10.0, carencia=2)
    assert multa == 30.0
