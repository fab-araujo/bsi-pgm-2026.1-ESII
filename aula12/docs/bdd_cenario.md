# Cenário BDD — Aula 9

Um dos testes do kata (multa com carência) reescrito como cenário
**Given-When-Then** (Gherkin). É apenas especificação em linguagem de negócio —
não roda ferramenta. O objetivo é traduzir o `assert` do TDD para um
comportamento observável que qualquer pessoa do negócio consiga ler e validar.

```gherkin
# language: pt
Funcionalidade: Multa de empréstimo com carência

  Cenário: devolução dentro do período de carência
    Dado um atraso de 1 dia
    E uma carência de 2 dias
    Quando a multa é calculada
    Então a multa deve ser R$ 0,00

  Cenário: devolução além da carência
    Dado um atraso de 5 dias
    E uma carência de 2 dias
    E um valor de R$ 10,00 por dia
    Quando a multa é calculada
    Então a multa deve ser R$ 30,00
```

> O primeiro cenário corresponde ao teste
> `test_atraso_dentro_da_carencia_nao_gera_multa_negativa` (em `tests/test_multa.py`) —
> o mesmo comportamento, agora legível para quem não programa.
