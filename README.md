# Sistema de Empréstimo de Equipamentos — Repositório de Referência por Aula

> **Gabarito navegável da disciplina.** Cada pasta contém o **projeto inteiro** no
> estado esperado **ao final daquela aula**. Para ver o que mudou de uma aula para a
> outra, compare duas pastas (ex.: `aula04/` vs `aula05/`) — sem precisar de git.

## Organização

| Pasta | Estado do projeto |
|-------|-------------------|
| `aula00-inicial/` | Sistema legado v1.0 herdado (ponto de partida) |
| `aula01/` | + diagnóstico do código (`PROBLEMAS.md`) |
| `aula02/` | + ADR-001 e estrutura de pastas em camadas |
| `aula03/` | + resenha crítica (UML e design) |
| `aula04/` | + SRP: camadas implementadas, dataclasses (sai o `emprestimos.py`) |
| `aula05/` | + OCP: hierarquia polimórfica |
| `aula06/` | + DIP: injeção de dependência |
| `aula08/` | + testes (unidade/integração) + CI |
| `aula09/` | + TDD: kata, funcionalidade nova e BDD |

> Não há `aula07/` — a Aula 7 é a prova escrita (sem entrega de código).

## Como **você** deve trabalhar

Aqui as **pastas** existem só para comparar aulas. **Você não trabalha assim.**
No seu repositório, você evolui **um único projeto** por **branches e commits** — o
seu `git log` é a sua evidência. O histórico **deste** repositório (cada aula entrou
por um **branch** e um **Pull Request**) é, ele próprio, um exemplo do fluxo profissional.

> O histórico linear original (evolução commit-a-commit) está preservado na tag `historico-linear`.
