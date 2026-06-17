import pytest

from models.equipamento import Notebook, Projetor, Cabo
from models.fabrica_equipamento import FabricaEquipamento


def test_criar_devolve_a_subclasse_correta():
    assert isinstance(FabricaEquipamento.criar("notebook", 1, "Dell"), Notebook)
    assert isinstance(FabricaEquipamento.criar("projetor", 2, "Epson"), Projetor)
    assert isinstance(FabricaEquipamento.criar("cabo", 3, "HDMI"), Cabo)


def test_criar_propaga_os_atributos():
    equip = FabricaEquipamento.criar("notebook", 7, "Notebook Dell")
    assert equip.id == 7
    assert equip.nome == "Notebook Dell"
    assert equip.tipo == "notebook"
    assert equip.disponivel is True


def test_tipo_desconhecido_levanta_valueerror():
    with pytest.raises(ValueError):
        FabricaEquipamento.criar("impressora", 9, "HP LaserJet")
