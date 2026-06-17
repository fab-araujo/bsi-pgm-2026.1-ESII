from models.equipamento import Equipamento, Notebook, Projetor, Cabo


class FabricaEquipamento:
    """Centraliza a criação de equipamentos a partir de um tipo (string).

    Mantém num único lugar o mapeamento de tipo para a classe concreta, para
    que o restante do sistema (em especial o repositório) não precise conhecer
    Notebook, Projetor ou Cabo diretamente. Acrescentar um tipo novo passa a
    ser uma alteração só aqui.
    """

    _registro = {
        "notebook": Notebook,
        "projetor": Projetor,
        "cabo": Cabo,
    }

    @classmethod
    def criar(cls, tipo: str, id: int, nome: str) -> Equipamento:
        classe = cls._registro.get(tipo)
        if classe is None:
            raise ValueError(f"Tipo de equipamento desconhecido: {tipo}")
        return classe(id, nome, tipo)
