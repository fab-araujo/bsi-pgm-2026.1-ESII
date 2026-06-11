# Documento de Projeto
## Sistema de Gestão de Empréstimo de Equipamentos — UFRA Paragominas

**Versão:** 1.0
**Data:** Março de 2025
**Responsável:** João Silva (Desenvolvedor Backend)

---

## 1. Visão Geral da Arquitetura

O sistema foi desenvolvido como uma aplicação Python de linha de comando. A versão 1.0 concentra toda a lógica em um único arquivo (`emprestimos.py`) por simplicidade de entrega no prazo estabelecido.

**Decisão de projeto registrada:** A equipe reconhece que a ausência de separação em camadas representa dívida técnica intencional. A refatoração para arquitetura em camadas está planejada para a v2.0.

---

## 2. Estrutura Atual (v1.0)

```
emprestimos/
└── emprestimos.py         ← toda a lógica do sistema em um único arquivo
```

---

## 3. Diagrama de Classes (v1.0)

```
┌─────────────────────────────────────────────────┐
│                    Sistema                       │
├─────────────────────────────────────────────────┤
│                                                  │
│ + registrar(equipamento_id, usuario_nome,        │
│             usuario_email, dias) : bool          │
│ + devolver(emprestimo_id) : void                 │
│ + listar_atrasados() : void                      │
│                                                  │
│ [acessa diretamente as variáveis globais         │
│  equipamentos[] e emprestimos_registrados[]]     │
└─────────────────────────────────────────────────┘

Variáveis globais (fora da classe):
  equipamentos             : list[dict]
  emprestimos_registrados  : list[dict]
```

> **Observação do desenvolvedor:** O uso de variáveis globais e dicionários em vez de classes de domínio foi uma decisão de velocidade de entrega. As consequências estão registradas na tabela de dívida técnica (seção 5).

---

## 4. Decisões de Projeto Registradas

| ID | Decisão | Justificativa | Consequência conhecida |
|---|---|---|---|
| DP01 | Código em arquivo único | Velocidade de entrega | Sem separação de responsabilidades — dívida técnica intencional |
| DP02 | Dados em listas de dicionários | Sem dependência de banco | Sem tipagem, sem validação automática |
| DP03 | Notificação via print() | Sem servidor SMTP no ambiente | Não envia e-mail real |
| DP04 | Sem testes automatizados | Prazo da v1.0 | Mudanças sem rede de segurança — risco alto de regressão |
| DP05 | Cálculo de multa com if/elif | Simplicidade inicial | Adicionar novo tipo exige modificar o método — violação de OCP |

---

## 5. Dívida Técnica Registrada

| ID | Problema | Prioridade para v2.0 |
|---|---|---|
| DT01 | Ausência de camadas de arquitetura | Alta |
| DT02 | Variáveis globais acessadas diretamente pela classe | Alta |
| DT03 | Notificação misturada com lógica de negócio | Alta |
| DT04 | Cálculo de multa duplicado em dois métodos | Alta |
| DT05 | Zero testes automatizados | Alta |
| DT06 | Cálculo de multa com if/elif por tipo | Média |
| DT07 | Dados sem tipagem (dicionários em vez de classes) | Média |

---

## 6. Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.11 | Linguagem de desenvolvimento |
| datetime | nativa | Cálculo de datas e atrasos |
| Git | 2.x | Controle de versão |
| GitHub | — | Hospedagem do repositório |

---

## 7. Como Executar os Testes

> Testes automatizados não implementados na v1.0. Previstos para v2.0 com pytest.

---

## 8. Histórico de Versões

| Versão | Data | Responsável | Descrição |
|---|---|---|---|
| 1.0 | Mar/2025 | João Silva | Versão inicial funcional — entrega com dívida técnica registrada |
