from abc import ABC, abstractmethod
from typing import Optional, List

from models.equipamento import Equipamento
from models.emprestimo import Emprestimo


class IRepositorioEmprestimo(ABC):
    """Contrato de persistência consumido pelo ServicoEmprestimo (DIP).

    Declara os 8 métodos que o serviço usa hoje. Qualquer implementação
    — a concreta de produção ou um dublê de teste — precisa fornecer
    todos eles: o Python recusa instanciar uma subclasse que esqueça
    algum `@abstractmethod`. É isso que torna os dublês seguros.
    """

    @abstractmethod
    def buscar_equipamento(self, id: int) -> Optional[Equipamento]: ...

    @abstractmethod
    def salvar_emprestimo(self, emprestimo: Emprestimo) -> None: ...

    @abstractmethod
    def buscar_emprestimo(self, id: int) -> Optional[Emprestimo]: ...

    @abstractmethod
    def marcar_indisponivel(self, equip_id: int) -> None: ...

    @abstractmethod
    def marcar_disponivel(self, equip_id: int) -> None: ...

    @abstractmethod
    def marcar_devolvido(self, emprestimo_id: int) -> None: ...

    @abstractmethod
    def listar_em_atraso(self) -> List[Emprestimo]: ...

    @abstractmethod
    def proximo_id_emprestimo(self) -> int: ...
