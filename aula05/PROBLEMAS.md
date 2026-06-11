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
