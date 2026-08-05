# Sistema de Empréstimo de Equipamentos — Repositório de Referência por Aula

Gabarito **navegável** da disciplina **Engenharia de Software II** (BSI, UFRA Paragominas).
Cada pasta deste repositório contém o **projeto inteiro** no estado esperado **ao final
de uma aula**. A ideia é simples: para entender o que cada aula muda, você **compara
duas pastas**.

> ⚠️ **Atenção: este NÃO é o jeito de você trabalhar.** As pastas existem só para
> facilitar a comparação. No seu próprio repositório você evolui **um único projeto**
> por meio de **branches e commits** — o seu `git log` é a sua evidência de aprendizado.
> Veja a seção **"Como você deve trabalhar"** mais abaixo.

---

## 📂 Estrutura

| Pasta | Conceito da aula | O que esta aula acrescenta |
|---|---|---|
| `aula00-inicial/` | — | Sistema legado **v1.0** herdado (ponto de partida, com a dívida técnica) |
| `aula01/` | Qualidade e dívida técnica | Diagnóstico do código em `PROBLEMAS.md` |
| `aula02/` | Arquitetura + ADR | `ADR-001` + estrutura de pastas em camadas (stubs) |
| `aula03/` | UML e design de componentes | `resenha-aula03.md` |
| `aula04/` | **SRP** | Camadas implementadas + dataclasses + diagramas; **sai o `emprestimos.py`** |
| `aula05/` | **OCP** | Hierarquia polimórfica (`Notebook/Projetor/Cabo`) elimina o `if/elif` |
| `aula06/` | **DIP** | Injeção de dependência + interfaces `abc.ABC` |
| `aula08/` | Testes + CI | Suíte (unidade/integração) + pipeline de CI |
| `aula09/` | **TDD** | Kata `multa.py` + funcionalidade nova + cenário BDD |
| `aula10/` | **Factory + Facade** | `FabricaEquipamento` centraliza a criação + fachada `SistemaDeEmprestimos` (pacote `app/`) enxuga o `main.py` |
| `aula11/` | **Strategy + Observer** | Multa vira estratégia trocável (`models/multa_strategy.py`) + serviço emite eventos para observers (`services/observer.py`, `NotificadorEmail`) |
| `aula12/` | **Refactoring + Code Smells** | Evento-`dict` vira `@dataclass Evento` + renames e Extract Function; `docs/diagnostico_a12.md` cataloga os smells (incl. o falso positivo) |

> **Não existe `aula07/`** — a Aula 7 é a prova escrita, sem entrega de código.
> Este repositório vai **até a Aula 12** (o Bloco NAP 2 segue em andamento).

---

## 🔍 Como comparar duas aulas

**Opção 1 — no GitHub:** abra a aba **Pull requests** (filtre por *Closed*) e clique no
PR da aula que te interessa (ex.: *"Aula 05 — OCP…"*). A aba **Files changed** mostra
exatamente o que aquela aula adicionou ao projeto.

**Opção 2 — no seu computador (a mais útil):** use o `git diff` entre as duas pastas.
Ele mostra **só o que mudou** de uma aula para a outra — arquivos idênticos não aparecem:

```bash
# o que a Aula 5 (OCP) mudou em relação à Aula 4 (SRP):
git diff --no-index aula04 aula05

# comparar só um arquivo:
git diff --no-index aula04/services/servico_emprestimo.py \
                    aula05/services/servico_emprestimo.py
```

**Opção 3 — visual (VS Code):** clique com o botão direito numa pasta → *"Select for
Compare"*; depois na outra pasta → *"Compare with Selected"*.

---

## ▶️ Como rodar o projeto de uma aula

```bash
cd aula05            # entre na pasta da aula que quiser
```

- **`aula00-inicial` … `aula03`** — ainda é o arquivo único da v1.0:
  ```bash
  python emprestimos.py
  ```
- **`aula04` … `aula10`** — já é o projeto organizado em camadas:
  ```bash
  python main.py
  ```
- **`aula08` … `aula10`** — têm testes automatizados:
  ```bash
  pip install -r requirements-dev.txt
  pytest -v
  ```

> Requer **Python 3.11+**.

---

## 🧑‍💻 Como você deve trabalhar

No **seu** repositório (o que você entrega), **não** crie pastas por aula. Evolua o
**mesmo projeto** ao longo do semestre, com **um branch por atividade** e **commits
descritivos**. O seu `git log` conta a história do seu aprendizado — e é ele que a
prova (a *questão integradora*) vai te pedir para explicar, citando o commit pelo hash.

A diferença em uma tabela:

| Este repositório (referência) | O seu repositório (entrega) |
|---|---|
| Pastas por aula, para **comparar** | **Um** projeto só, evoluído por **branches/commits** |
| `git diff --no-index aulaX aulaY` | `git diff <commit-antigo> <commit-novo>` |
| Serve para você **conferir** seu resultado | É a sua **evidência** avaliada |

---

## 🧭 O histórico deste repositório também é material de estudo

Cada aula entrou aqui por um **branch** e um **Pull Request** real. Observe a topologia:

```bash
git log --graph --oneline
```

Você verá **um merge de Pull Request por aula** — um exemplo concreto do **fluxo
profissional** (branch → PR → merge) que vocês passam a adotar a partir da Aula 10.

### Histórico linear original (evolução commit a commit)

Antes de virar "pastas por aula", este projeto foi construído como um **único projeto
evoluído commit a commit** — exatamente como **você** deve fazer. Esse histórico está
preservado na tag **`historico-linear`**:

```bash
git fetch --tags
git log --oneline historico-linear      # a evolução real, um commit por entrega
git switch --detach historico-linear    # navegar o projeto naquele formato
git switch -                            # voltar para o repo de pastas
```

---

## ⚙️ Nota sobre o CI (GitHub Actions)

O arquivo de CI (`ci.yml`) aparece **dentro** das pastas `aula08/` e `aula09/`, como
parte do snapshot daquela aula. Como o GitHub Actions só executa workflows na **raiz**
do repositório, o pipeline **não roda** neste repo de pastas — o que é esperado para
um gabarito de comparação. No seu repositório (um projeto só), o `ci.yml` fica na raiz
e o pipeline roda de verdade a cada push.

---

## 🗺️ Mapa: dívida técnica da v1.0 → aula que resolve

| Problema na v1.0 | Resolvido em | Conceito |
|---|---|---|
| Dados como dicionários · classe que faz tudo · variáveis globais | `aula04` | SRP |
| `if/elif` por tipo + cálculo de multa duplicado | `aula05` | OCP |
| Dependências criadas internamente (não testável) | `aula06` | DIP |
| Zero testes automatizados | `aula08` | Testes + CI |
| Criação de objetos espalhada (cliente conhece classes concretas) | `aula10` | Factory + Facade |

> Os itens restantes (algoritmo de multa acoplado à hierarquia, notificação direta e
> *code smells*) são tratados nas **Aulas 11–12** e entrarão aqui em ofertas futuras.
