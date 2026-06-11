# Documento de Requisitos
## Sistema de Gestão de Empréstimo de Equipamentos — UFRA Paragominas

**Versão:** 1.0
**Data:** Março de 2025
**Responsável:** Maria Souza (Analista de Requisitos)

---

## 1. Requisitos Funcionais

### RF01 — Registrar Empréstimo

**Descrição:** O sistema deve permitir o registro de um empréstimo de equipamento.

**Entradas:** identificador do equipamento, nome do solicitante, e-mail do solicitante, quantidade de dias do empréstimo.

**Saída:** confirmação do registro com data de devolução prevista.

**Regras de negócio:**

- RN01: Um equipamento só pode ser emprestado se estiver disponível.
- RN02: O prazo mínimo de empréstimo é 1 dia.
- RN03: Ao registrar, o sistema notifica o solicitante por e-mail com a data de devolução prevista.

---

### RF02 — Registrar Devolução

**Descrição:** O sistema deve permitir o registro da devolução de um equipamento emprestado.

**Entradas:** identificador do empréstimo.

**Saída:** confirmação da devolução com valor de multa (se houver atraso).

**Regras de negócio:**

- RN04: Um empréstimo não pode ser devolvido duas vezes.
- RN05: Se a devolução ocorrer após a data prevista, o sistema calcula multa por atraso conforme o tipo de equipamento:

| Tipo de equipamento | Multa por dia de atraso |
|---|---|
| Notebook | R$ 10,00 |
| Projetor | R$ 15,00 |
| Cabo HDMI | R$ 2,00 |

- RN06: Ao registrar a devolução, o sistema notifica o solicitante por e-mail com o valor da multa.
- RN07: Após a devolução, o equipamento volta a ficar disponível para novos empréstimos.

---

### RF03 — Listar Empréstimos em Atraso

**Descrição:** O sistema deve exibir todos os empréstimos cujo prazo de devolução já passou e que ainda não foram devolvidos.

**Saída:** lista com nome do solicitante, quantidade de dias em atraso e valor de multa acumulada.

**Regras de negócio:**

- RN08: Para cada empréstimo em atraso, o sistema envia notificação por e-mail ao solicitante.
- RN09: O cálculo de multa para listagem segue as mesmas regras de RN05.

---

## 2. Requisitos Não Funcionais

### RNF01 — Desempenho

O sistema deve responder a qualquer operação em menos de 1 segundo para um volume de até 100 equipamentos cadastrados.

### RNF02 — Usabilidade

A interface de linha de comando deve apresentar menu textual claro, com opções numeradas. Mensagens de erro devem ser descritivas.

### RNF03 — Manutenibilidade

O código deve estar organizado de forma que a adição de um novo tipo de equipamento não exija alterações em mais de um módulo do sistema.

> **Observação do analista:** Esta restrição não foi atendida na versão 1.0 entregue — ver PROBLEMAS.md.

### RNF04 — Testabilidade

Os módulos de regra de negócio devem poder ser testados de forma isolada, sem dependência de entrada do usuário ou estado externo.

> **Observação do analista:** Esta restrição não foi atendida na versão 1.0 entregue — ver PROBLEMAS.md.

### RNF05 — Portabilidade

O sistema deve executar em qualquer sistema operacional com Python 3.11 instalado, sem dependências externas adicionais.

---

## 3. Requisitos de Interface

### RI01 — Menu principal

```
1-Registrar  2-Devolver  3-Atrasados  0-Sair
Opção:
```

### RI02 — Mensagens de confirmação

Toda operação concluída com sucesso deve exibir mensagem de confirmação explícita ao usuário.

### RI03 — Mensagens de erro

Toda operação inválida deve exibir mensagem de erro descritiva sem encerrar o sistema.

---

## 4. Rastreabilidade Requisitos × Funcionalidades

| Requisito | Método responsável | Arquivo |
|---|---|---|
| RF01, RN01, RN02, RN03 | `Sistema.registrar()` | `emprestimos.py` |
| RF02, RN04–RN07 | `Sistema.devolver()` | `emprestimos.py` |
| RF03, RN08, RN09 | `Sistema.listar_atrasados()` | `emprestimos.py` |
