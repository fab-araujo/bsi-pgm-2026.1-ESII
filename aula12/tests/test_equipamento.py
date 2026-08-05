import pytest

from models.fabrica_equipamento import FabricaEquipamento


# Desde a Aula 11 o Equipamento exige uma estratégia de multa no construtor.
# Criar pela fábrica injeta a estratégia certa por tipo — como no sistema real.
@pytest.mark.parametrize("tipo, dias, multa_esperada", [
    ("notebook", 3, 30.0),   # 3 × 10.0
    ("notebook", 1, 10.0),
    ("projetor", 2, 30.0),   # 2 × 15.0
    ("projetor", 4, 60.0),
    ("cabo",     5, 10.0),   # 5 × 2.0
    ("cabo",     3,  6.0),
])
def test_calcular_multa_atraso_positivo(tipo, dias, multa_esperada):
    equipamento = FabricaEquipamento.criar(tipo, 1, "Equipamento Teste")
    assert equipamento.calcular_multa(dias) == multa_esperada


@pytest.mark.parametrize("tipo", ["notebook", "projetor", "cabo"])
def test_calcular_multa_atraso_negativo_retorna_zero(tipo):
    # Invariante max(0.0, ...) — devolução antecipada nunca gera multa negativa.
    equipamento = FabricaEquipamento.criar(tipo, 1, "Equipamento Teste")
    assert equipamento.calcular_multa(-2) == 0.0
