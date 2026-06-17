# O que é um ADR

ADR significa *Architecture Decision Record* — um documento curto que registra uma decisão arquitetural importante: qual era o problema, quais opções foram consideradas, o que foi decidido e quais são as consequências.

O objetivo não é documentar *como* o código funciona — isso está no código. O objetivo é registrar *por que* o código foi organizado dessa forma, para que quem chegar depois entenda o raciocínio por trás das decisões.

---

## Estrutura

### Status
Indica o estado atual da decisão. Valores possíveis:
- `Proposed` — a decisão foi proposta mas ainda não aprovada
- `Accepted` — a decisão foi tomada e está em vigor
- `Deprecated` — a decisão foi substituída por outra

### Contexto
Descreve o problema que tornou necessária a decisão. Responde: *o que estava acontecendo que nos forçou a decidir algo?* Inclui os requisitos ou restrições que estavam em jogo.

### Opções consideradas
Lista as alternativas avaliadas. Para cada uma: por que foi considerada e por que foi aceita ou descartada. Não basta listar — é preciso justificar.

### Decisão
Descreve o que foi decidido e como o sistema ficará organizado como resultado. Deve ser concreto: nomes de pastas, responsabilidades de cada parte, regras que a estrutura impõe.

### Consequências
Descreve o que muda com a decisão: o que melhora, o que fica mais complexo, quais portas se abrem e quais se fecham.

---

## Template

```markdown
# ADR-NNN: Título da decisão

**Status:** Accepted
**Data:** YYYY-MM-DD

## Contexto

[Descreva o problema que motivou a decisão.]

## Opções consideradas

[Liste as alternativas com justificativa de aceite ou descarte.]

## Decisão

[Descreva o que foi decidido, com nomes e responsabilidades concretas.]

## Consequências

[Descreva o que muda, melhora e fica mais complexo.]
```
