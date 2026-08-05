from models.equipamento import Equipamento, Notebook, Projetor, Cabo
from models.multa_strategy import MultaPorDia


class FabricaEquipamento:
    """Centraliza a criação de equipamentos a partir de um tipo (string).

    Desde a Aula 11 a fábrica também associa, por tipo, a ESTRATÉGIA de multa:
    é o único lugar que decide qual algoritmo cada equipamento usa. Acrescentar
    um tipo novo (ou trocar a política de multa de um tipo) continua sendo uma
    alteração só aqui.
    """

    _config = {
        "notebook": (Notebook, MultaPorDia(10.0)),
        "projetor": (Projetor, MultaPorDia(15.0)),
        "cabo":     (Cabo,     MultaPorDia(2.0)),
    }

    @classmethod
    def criar(cls, tipo: str, id: int, nome: str) -> Equipamento:
        entrada = cls._config.get(tipo)
        if entrada is None:
            raise ValueError(f"Tipo de equipamento desconhecido: {tipo}")
        classe, estrategia = entrada
        return classe(id, nome, tipo, estrategia)
