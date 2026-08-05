# Autodiagnóstico — Aula 12 (Refactoring e Code Smells)

Smells identificados no meu próprio código (estado pós-Aula 11), com o
refactoring aplicado — ou a justificativa para **não** aplicar.

| # | Arquivo:linha | Smell (nome técnico) | Refactoring proposto | Justificativa |
|---|---|---|---|---|
| 1 | `services/servico_emprestimo.py` (emissões) e `services/observer.py` | *Primitive Obsession* | **Replace Primitive with Object** → `@dataclass Evento` (aplicado) | O evento era um `dict`: chave digitada errada (`evento["emial"]`) só explodia em runtime e nenhum contrato documentava os campos. Com `Evento`, o contrato é explícito e a IDE verifica. |
| 2 | `services/servico_emprestimo.py:62` | *Mysterious Name* | **Rename** `atraso` → `dias_atraso` (aplicado) | `atraso` era ambíguo (o atraso? a multa do atraso?); `dias_atraso` diz a unidade e o significado — o mesmo nome que a estratégia de multa já usava. |
| 3 | `repositories/repositorio_emprestimo.py` | *Mysterious Name* | **Rename** `e`/`emp`/`equip` → `emprestimo`/`equipamento` (aplicado) | Variáveis de uma letra ou truncadas obrigavam o leitor a deduzir o tipo pelo contexto. Renomeadas pela IDE (Refactor → Rename), sem alteração de comportamento. |
| 4 | `services/servico_emprestimo.py:72` | *Long Method* | **Extract Function** → `_imprimir_atraso` (aplicado) | `listar_atrasados` iterava, calculava, imprimia e notificava. O fluxo principal agora só itera e delega; o detalhe de cada linha vive numa função com nome próprio. |
| 5 | `models/equipamento.py:28-38` | **Smell aparente — não refatorado** (*Data Class* aparente) | *Inline Class* / *Move Function* — **rejeitados** | As subclasses `Notebook`/`Projetor`/`Cabo` ficaram vazias após o Strategy, mas são rótulos de tipo **por design**: o sistema distingue os tipos, e a fábrica associa a estratégia por eles. Dissolvê-las (*Inline Class*) ou devolver o cálculo a elas (*Move Function*) reverteria o Strategy e o OCP obtidos na Aula 11. Falso positivo reconhecido e mantido. |

**Verificação:** após cada refactoring, `pytest -v` — suíte integralmente verde;
`python main.py` imprime exatamente as mesmas mensagens de antes (comportamento
observável preservado, critério de Fowler para chamar a mudança de *refactoring*).
