# Problemas Identificados — Leitura Inicial do Código

Este arquivo é preenchido pelos estudantes na Aula 1 após a leitura do código legado.

---

## Minha leitura inicial

- **`emprestimos.py`, classe `Sistema` inteira:** a classe faz muita coisa ao mesmo tempo — registra empréstimo, calcula multa, manda e-mail e exibe o menu. Tudo no mesmo lugar.
- **`emprestimos.py`, linhas 42–43, 75–76 e 96–97:** código de e-mail misturado dentro dos métodos `registrar`, `devolver` e `listar_atrasados`. Se a forma de notificar mudar, é preciso mexer em três lugares diferentes dentro da lógica de negócio.
- **`emprestimos.py`, linhas 62–69 (`devolver`) e linhas 86–92 (`listar_atrasados`):** o mesmo cálculo de multa com `if/elif` (notebook, projetor, cabo) aparece duas vezes. Se a regra de multa mudar, é preciso atualizar os dois blocos.
- **`emprestimos.py`, linhas 4–9:** as listas `equipamentos` e `emprestimos_registrados` estão fora da classe, soltas no arquivo — qualquer parte do código pode modificá-las diretamente sem nenhum controle.
- **`emprestimos.py`, linhas 100–118, função `main`:** o menu (`while True` com `input`) está no mesmo arquivo que a lógica de negócio. São responsabilidades completamente diferentes.
- **`emprestimos.py`, linhas 62–69 e 86–92:** para adicionar um novo tipo de equipamento (ex.: tablet), seria preciso abrir o código nesses dois blocos `if/elif` e acrescentar mais um `elif` em cada um.
- **`emprestimos.py`, linhas 28–38 e 4–8:** os dados de equipamento e empréstimo são dicionários — não há como saber quais campos existem sem ler o código inteiro. Um erro de digitação numa chave não é detectado pelo Python.
- **`emprestimos.py`, ausência de arquivo `tests/`:** não existe nenhum teste automatizado — impossível saber se uma mudança quebrou algo sem rodar o programa manualmente.
- **`emprestimos.py`, método `listar_atrasados`, linhas 79–97:** o método identifica empréstimos em atraso mas não marca o equipamento como disponível — se o equipamento fosse recuperado sem passar por `devolver`, ficaria indisponível para sempre.
- **`emprestimos.py`, método `devolver`, linhas 71–73:** depois de registrar a devolução, o código percorre a lista `equipamentos` inteira de novo só para marcar disponível — sendo que o equipamento poderia ter sido buscado antes, junto com o restante da lógica.
- **`emprestimos.py` como um todo:** os dados somem ao fechar o programa — não há persistência. A cada execução o sistema começa do zero com os três equipamentos fixos nas linhas 4–8.

---

## Revisão com vocabulário técnico

*(Este espaço será preenchido após a Aula 4, quando os termos técnicos corretos forem aprendidos)*
