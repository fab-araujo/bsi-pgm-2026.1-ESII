from models.multa_strategy import MultaPorDia, MultaProgressiva


# Testa as estratégias ISOLADAS, sem montar Equipamento — é a prova viva do
# Strategy: o algoritmo virou um objeto testável por conta própria.

def test_multa_por_dia_e_linear():
    assert MultaPorDia(10.0).calcular(3) == 30.0


def test_multa_por_dia_nunca_negativa():
    assert MultaPorDia(10.0).calcular(-2) == 0.0


def test_progressiva_e_linear_dentro_do_corte():
    # 2 dias, corte 3 -> ainda no valor normal: 2 × 10
    assert MultaProgressiva(10.0).calcular(2) == 20.0


def test_progressiva_dobra_apos_o_corte():
    # 5 dias, corte 3: 3 × 10 + 2 × 10 × 2 = 70
    assert MultaProgressiva(10.0).calcular(5) == 70.0


def test_progressiva_sem_atraso_nao_gera_multa():
    assert MultaProgressiva(10.0).calcular(0) == 0.0
