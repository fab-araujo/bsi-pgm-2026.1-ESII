# ADR-001: Escolha da Arquitetura do Sistema de Biblioteca

**Status:** Accepted
**Data:** 2025-08-10

## Contexto

O sistema de gerenciamento de biblioteca (v1.0) foi desenvolvido como um script único (`biblioteca.py`). Com o crescimento do acervo, surgiram dois problemas claros:

- Adicionar um novo tipo de material (e-book, periódico) exige abrir o script e modificar múltiplos trechos.
- Não é possível testar as regras de empréstimo sem simular a entrada do usuário manualmente.

## Opções consideradas

| Estilo        | Extensível? | Testável? | Complexidade |
|---------------|-------------|-----------|--------------|
| Arquivo único | Não         | Não       | Baixa        |
| Em camadas    | Sim         | Sim       | Média        |
| MVC           | Parcial     | Parcial   | Alta         |

- **Arquivo único:** descartado — os dois problemas persistem.
- **MVC:** descartado — adequado para interfaces gráficas; o sistema usa CLI e não justifica a separação View/Controller.
- **Em camadas:** resolve os dois problemas com complexidade proporcional ao tamanho da equipe (2 desenvolvedores).

## Decisão

Adotar arquitetura em camadas:

- `main.py` — interface CLI, sem lógica de negócio
- `services/` — regras de empréstimo, multas e reservas
- `repositories/` — persistência do acervo e dos empréstimos
- `models/` — representação de Livro, Periodico, Usuario

## Consequências

- Adicionar novo tipo de material = nova classe em `models/`, sem tocar em `services/`
- Regras de negócio em `services/` podem ser testadas com repositório falso, sem precisar de dados reais
- Se o sistema migrar para leitura de arquivo CSV no futuro, só `main.py` precisa mudar