# Casos de Uso
## Sistema de Gestão de Empréstimo de Equipamentos — UFRA Paragominas

**Versão:** 1.0
**Data:** Março de 2025

---

## Diagrama de Atores

```
┌────────────────────────────────────────────┐
│          Sistema de Empréstimos            │
│                                            │
│   [UC01 Registrar Empréstimo         ]     │
│   [UC02 Registrar Devolução          ]     │
│   [UC03 Listar Empréstimos em Atraso ]     │
│                                            │
└────────────────────────────────────────────┘
          ▲                    ▲
          │                    │
   Atendente de TI      Coordenador de TI
```

---

## UC01 — Registrar Empréstimo

**Ator principal:** Atendente de TI

**Pré-condição:** O equipamento solicitado está disponível no sistema.

**Pós-condição:** O empréstimo é registrado; o equipamento fica indisponível; o solicitante recebe notificação por e-mail.

### Fluxo Principal

1. Atendente seleciona a opção "1 - Registrar" no menu.
2. Sistema solicita o identificador do equipamento.
3. Atendente informa o identificador.
4. Sistema solicita nome do solicitante.
5. Atendente informa o nome.
6. Sistema solicita e-mail do solicitante.
7. Atendente informa o e-mail.
8. Sistema solicita a quantidade de dias do empréstimo.
9. Atendente informa a quantidade de dias.
10. Sistema registra o empréstimo, marca o equipamento como indisponível e exibe a data de devolução prevista.
11. Sistema notifica o solicitante por e-mail.

### Fluxo Alternativo A — Equipamento indisponível

No passo 3, se o equipamento estiver indisponível:

- Sistema exibe mensagem "Equipamento inválido ou indisponível".
- Caso de uso encerra sem registrar.

---

## UC02 — Registrar Devolução

**Ator principal:** Atendente de TI

**Pré-condição:** Existe um empréstimo ativo com o identificador informado.

**Pós-condição:** A devolução é registrada; o equipamento fica disponível; multa calculada (se houver atraso); solicitante notificado.

### Fluxo Principal

1. Atendente seleciona a opção "2 - Devolver" no menu.
2. Sistema solicita o identificador do empréstimo.
3. Atendente informa o identificador.
4. Sistema verifica se o empréstimo existe e não foi devolvido.
5. Sistema calcula atraso em dias (se houver).
6. Sistema calcula multa conforme tipo de equipamento (se houver atraso).
7. Sistema registra a devolução e marca o equipamento como disponível.
8. Sistema exibe confirmação com valor da multa.
9. Sistema notifica o solicitante por e-mail.

### Fluxo Alternativo A — Empréstimo inválido ou já devolvido

No passo 4, se o empréstimo não existir ou já tiver sido devolvido:

- Sistema exibe mensagem "Empréstimo inválido ou já devolvido".
- Caso de uso encerra sem registrar.

---

## UC03 — Listar Empréstimos em Atraso

**Ator principal:** Coordenador de TI

**Pré-condição:** Existem empréstimos com data de devolução vencida e não devolvidos.

**Pós-condição:** Lista exibida; solicitantes em atraso notificados por e-mail.

### Fluxo Principal

1. Atendente seleciona a opção "3 - Atrasados" no menu.
2. Sistema verifica todos os empréstimos ativos.
3. Para cada empréstimo com data de devolução anterior à data atual:
   - Sistema calcula dias de atraso.
   - Sistema calcula multa acumulada.
   - Sistema exibe linha com nome do solicitante, dias de atraso e multa.
   - Sistema notifica o solicitante por e-mail.
4. Se não houver atrasos, sistema exibe "Nenhum empréstimo em atraso".

---

## Matriz de Rastreabilidade Casos de Uso × Requisitos

| Caso de Uso | Requisitos Funcionais | Regras de Negócio |
|---|---|---|
| UC01 | RF01 | RN01, RN02, RN03 |
| UC02 | RF02 | RN04, RN05, RN06, RN07 |
| UC03 | RF03 | RN08, RN09 |
