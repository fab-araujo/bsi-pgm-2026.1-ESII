# Problemas Identificados — Leitura Inicial do Código

---

## Minha leitura inicial

- A classe `Sistema` faz muita coisa ao mesmo tempo: registra empréstimo, calcula multa, manda e-mail e exibe o menu — tudo no mesmo lugar.
- Tem código de e-mail misturado com o cálculo de multa dentro dos métodos `devolver` e `listar_atrasados`.
- O mesmo cálculo de multa aparece duas vezes no código: dentro de `devolver` e dentro de `listar_atrasados`.
- As listas de equipamentos e empréstimos estão fora da classe, soltas no arquivo.
- O menu está misturado no mesmo arquivo que a lógica de negócio.
- Para adicionar um novo tipo de equipamento, precisaria abrir o código em pelo menos dois lugares.
- Os dados são dicionários — um erro de digitação numa chave não é detectado.
- Não existe nenhum teste automatizado.

---

## Revisão com vocabulário técnico

| Descrição em linguagem livre | Termo técnico |
|---|---|
| "A classe faz muita coisa ao mesmo tempo" | `Sistema` tem **baixa coesão**: regra de negócio, notificação, cálculo de multa e interface no mesmo módulo — viola **SRP** |
| "E-mail misturado com cálculo de multa" | Responsabilidades misturadas: notificação e negócio no mesmo método — viola **SRP** |
| "Listas soltas no arquivo" | **Acoplamento por variável global**: `Sistema` depende de `equipamentos` e `emprestimos_registrados` — qualquer módulo pode alterar o estado |
| "Menu no mesmo arquivo que tudo" | Ausência de separação de responsabilidades: interface e negócio no mesmo módulo |
| "Mesmo cálculo em dois lugares" | Violação de **DRY** (Don't Repeat Yourself) — lógica duplicada é onde os bugs se escondem |
| "Adicionar tipo exige mexer em dois lugares" | Violação de **OCP** (Open-Closed Principle) — modificação em código existente para estender comportamento |
| "Dados como dicionários" | Ausência de **classes de domínio** — sem tipagem, sem encapsulamento de comportamento |
| "Sem testes" | Violação de **RNF04** (testabilidade) — impossível testar de forma isolada |

---

## Divergências entre a documentação herdada e o código v1.0

Além dos problemas de design acima, a leitura cruzada entre a documentação
recebida (`docs/requisitos.md`) e a implementação entregue (`emprestimos.py`)
revela pontos em que **o que está escrito não corresponde ao que o código faz**.
Cada linha abaixo é uma divergência verificável.

| # | O que a documentação promete | O que o código v1.0 realmente faz | Fonte |
|---|---|---|---|
| 1 | **RN02** — "O prazo mínimo de empréstimo é 1 dia." | `Sistema.registrar()` não valida o parâmetro `dias`: aceita `0`, valores negativos ou qualquer número, sem checagem. | `requisitos.md` §RF01 |
| 2 | **RN03 / RN06 / RN08** — o sistema "notifica o solicitante **por e-mail**". | Não há envio de e-mail algum: os três métodos apenas executam `print("[EMAIL] …")` no console. A documentação descreve um canal (e-mail) que o código não implementa. | `requisitos.md` §RF01–RF03 |
| 3 | **RNF03** — adicionar um novo tipo de equipamento "não deve exigir alterações em mais de um módulo". | Um novo tipo obriga a editar o `if/elif` de multa em **dois** métodos (`devolver` e `listar_atrasados`) e ainda a lista global `equipamentos`. | `requisitos.md` §RNF03 |
| 4 | **RNF04** — as regras de negócio devem ser "testáveis de forma isolada, sem entrada do usuário ou estado externo". | `Sistema` lê e escreve as variáveis globais `equipamentos` e `emprestimos_registrados` e mistura `input()`/`print()` com a regra de negócio — não há como testar em isolamento. | `requisitos.md` §RNF04 |
| 5 | **RI02** — "Toda operação concluída com sucesso deve exibir mensagem de confirmação explícita." | `registrar()` conclui sem emitir confirmação de sucesso ("empréstimo registrado"); apenas `devolver()` confirma. A operação de registro viola a regra de interface. | `requisitos.md` §RI02 |
| 6 | **RI03 / RNF02** — mensagens de erro devem ser "descritivas". | `registrar()` funde dois erros distintos numa única mensagem ("Equipamento inválido **ou** indisponível"), sem informar ao usuário qual dos dois ocorreu. | `requisitos.md` §RI03 |

> **Observação.** A tabela de multas de **RN05** (Notebook R$ 10, Projetor R$ 15,
> Cabo R$ 2) **confere** com o código — não é divergência, e por isso não foi
> listada. O objetivo do diagnóstico é apontar onde doc e código discordam,
> não inflar a contagem.

Essas seis divergências, somadas aos *code smells* da seção anterior, formam o
ponto de partida da refatoração: as Aulas 2–8 atacam justamente RNF03
(OCP/camadas) e RNF04 (DIP + testes).
