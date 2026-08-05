import datetime

import pytest

from models.fabrica_equipamento import FabricaEquipamento
from repositories.interfaces import IRepositorioEmprestimo
from services.evento import Evento
from services.observer import Observer
from services.servico_emprestimo import ServicoEmprestimo


# Fake — implementação simplificada funcional (salva e busca de verdade, em memória).
class RepositorioFake(IRepositorioEmprestimo):
    def __init__(self):
        # semeia pela fábrica: ganha de brinde a estratégia certa por tipo,
        # refletindo como o sistema real cria os equipamentos.
        self._equipamentos = [
            FabricaEquipamento.criar("notebook", 1, "Notebook Dell"),
            FabricaEquipamento.criar("projetor", 2, "Projetor Epson"),
            FabricaEquipamento.criar("cabo",     3, "Cabo HDMI"),
        ]
        self._emprestimos = []

    def buscar_equipamento(self, id):
        return next((e for e in self._equipamentos if e.id == id), None)

    def salvar_emprestimo(self, emprestimo):
        self._emprestimos.append(emprestimo)

    def buscar_emprestimo(self, id):
        return next((e for e in self._emprestimos if e.id == id), None)

    def marcar_indisponivel(self, equip_id):
        equip = self.buscar_equipamento(equip_id)
        if equip:
            equip.disponivel = False

    def marcar_disponivel(self, equip_id):
        equip = self.buscar_equipamento(equip_id)
        if equip:
            equip.disponivel = True

    def marcar_devolvido(self, emprestimo_id):
        emp = self.buscar_emprestimo(emprestimo_id)
        if emp:
            emp.devolvido = True

    def listar_em_atraso(self):
        hoje = datetime.date.today()
        return [e for e in self._emprestimos
                if not e.devolvido and e.data_devolucao < hoje]

    def proximo_id_emprestimo(self):
        return len(self._emprestimos) + 1

    def contar_emprestimos_abertos(self, usuario_email):
        return sum(1 for e in self._emprestimos
                   if e.usuario_email == usuario_email and not e.devolvido)


# Spy — Observer que guarda os Eventos recebidos; os asserts leem atributos.
class NotificadorSpy(Observer):
    def __init__(self):
        self.eventos = []

    def update(self, evento: Evento):
        self.eventos.append(evento)


@pytest.fixture
def repositorio_fake():
    return RepositorioFake()


@pytest.fixture
def notificador_spy():
    return NotificadorSpy()


@pytest.fixture
def servico(repositorio_fake, notificador_spy):
    s = ServicoEmprestimo(repositorio_fake)      # sem notificador no construtor
    s.registrar_observer(notificador_spy)        # o spy escuta como observer
    return s
