# Diagramas de Sequência — v2.0

> Este arquivo é a **solução-guia das Partes 2 e 3 da Atividade 4a**: traz os 3 diagramas
> de sequência prontos (UC01 já estava no `comando.md`; UC02 e UC03 aqui como referência
> opcional para você comparar depois) e as **assinaturas dos métodos** que viram os stubs.
>
> Para a **Parte 1 da Atividade 4a (decomposição em camadas com justificativa)**,
> consulte a Q2(c) da resenha modelo (`solucao/docs/resenha-aula03.md`).

## UC01 — Registrar Empréstimo

```mermaid
sequenceDiagram
    actor Atendente
    participant main as main.py
    participant servico as ServicoEmprestimo
    participant repo as RepositorioEmprestimo
    participant notif as Notificador

    Atendente->>main: informa equip_id, nome, email, dias
    main->>servico: registrar(equip_id, nome, email, dias)
    servico->>repo: buscar_equipamento(equip_id)
    repo-->>servico: Equipamento
    alt equipamento disponível
        servico->>repo: salvar_emprestimo(emprestimo)
        servico->>repo: marcar_indisponivel(equip_id)
        servico->>notif: notificar_emprestimo(email, data_devolucao)
        servico-->>main: True
        main-->>Atendente: exibe data de devolução
    else equipamento indisponível ou inválido
        servico-->>main: False
        main-->>Atendente: "Equipamento inválido ou indisponível"
    end
```

## UC02 — Registrar Devolução

```mermaid
sequenceDiagram
    actor Atendente
    participant main as main.py
    participant servico as ServicoEmprestimo
    participant repo as RepositorioEmprestimo
    participant notif as Notificador

    Atendente->>main: informa emprestimo_id
    main->>servico: devolver(emprestimo_id)
    servico->>repo: buscar_emprestimo(emprestimo_id)
    repo-->>servico: Emprestimo
    alt empréstimo válido e não devolvido
        servico->>repo: buscar_equipamento(equip_id)
        repo-->>servico: Equipamento
        servico->>servico: calcular atraso e multa
        servico->>repo: marcar_devolvido(emprestimo_id)
        servico->>repo: marcar_disponivel(equip_id)
        servico->>notif: notificar_devolucao(email, multa)
        main-->>Atendente: exibe multa
    else inválido ou já devolvido
        main-->>Atendente: "Empréstimo inválido ou já devolvido"
    end
```

## UC03 — Listar Empréstimos em Atraso

```mermaid
sequenceDiagram
    actor Coordenador
    participant main as main.py
    participant servico as ServicoEmprestimo
    participant repo as RepositorioEmprestimo
    participant notif as Notificador

    Coordenador->>main: seleciona "3 - Atrasados"
    main->>servico: listar_atrasados()
    servico->>repo: listar_em_atraso()
    repo-->>servico: list[Emprestimo]
    loop para cada empréstimo em atraso
        servico->>repo: buscar_equipamento(equip_id)
        repo-->>servico: Equipamento
        servico->>servico: calcular multa
        servico->>notif: notificar_atraso(email)
        main-->>Coordenador: exibe nome, dias, multa
    end
```

## Assinaturas extraídas dos diagramas

### ServicoEmprestimo
- `registrar(equipamento_id, usuario_nome, usuario_email, dias) -> bool`
- `devolver(emprestimo_id) -> None`
- `listar_atrasados() -> None`

### RepositorioEmprestimo
- `buscar_equipamento(id) -> Equipamento`
- `salvar_emprestimo(emprestimo) -> None`
- `buscar_emprestimo(id) -> Emprestimo`
- `marcar_indisponivel(equip_id) -> None`
- `marcar_disponivel(equip_id) -> None`
- `marcar_devolvido(emprestimo_id) -> None`
- `listar_em_atraso() -> list`
- `proximo_id_emprestimo() -> int`

### Notificador
- `notificar_emprestimo(email, data_devolucao) -> None`
- `notificar_devolucao(email, multa) -> None`
- `notificar_atraso(email) -> None`
