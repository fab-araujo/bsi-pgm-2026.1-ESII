import datetime
from models.emprestimo import Emprestimo
from models.fabrica_equipamento import FabricaEquipamento
from repositories.interfaces import IRepositorioEmprestimo


class RepositorioEmprestimo(IRepositorioEmprestimo):
    def __init__(self):
        criar = FabricaEquipamento.criar
        self._equipamentos = [
            criar("notebook", 1, "Notebook Dell"),
            criar("projetor", 2, "Projetor Epson"),
            criar("cabo",     3, "Cabo HDMI"),
        ]
        self._emprestimos = []

    def buscar_equipamento(self, id: int):
        return next((equipamento for equipamento in self._equipamentos
                     if equipamento.id == id), None)

    def salvar_emprestimo(self, emprestimo: Emprestimo) -> None:
        self._emprestimos.append(emprestimo)

    def buscar_emprestimo(self, id: int):
        return next((emprestimo for emprestimo in self._emprestimos
                     if emprestimo.id == id), None)

    def marcar_indisponivel(self, equip_id: int) -> None:
        equipamento = self.buscar_equipamento(equip_id)
        if equipamento:
            equipamento.disponivel = False

    def marcar_disponivel(self, equip_id: int) -> None:
        equipamento = self.buscar_equipamento(equip_id)
        if equipamento:
            equipamento.disponivel = True

    def marcar_devolvido(self, emprestimo_id: int) -> None:
        emprestimo = self.buscar_emprestimo(emprestimo_id)
        if emprestimo:
            emprestimo.devolvido = True

    def listar_em_atraso(self):
        hoje = datetime.date.today()
        return [emprestimo for emprestimo in self._emprestimos
                if not emprestimo.devolvido and emprestimo.data_devolucao < hoje]

    def proximo_id_emprestimo(self) -> int:
        return len(self._emprestimos) + 1

    def contar_emprestimos_abertos(self, usuario_email: str) -> int:
        return sum(1 for emprestimo in self._emprestimos
                   if emprestimo.usuario_email == usuario_email
                   and not emprestimo.devolvido)
