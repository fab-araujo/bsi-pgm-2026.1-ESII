# Estrutura do ADR (Architecture Decision Record)

Um ADR documenta uma decisão arquitetural importante que afeta como o sistema será construído.

## Campos obrigatórios:

### 1. **Contexto**
Descreva o problema ou situação que exigiu uma decisão. Cite os requisitos que motivam essa decisão.

### 2. **Opções consideradas**
Liste as alternativas avaliadas. Para cada uma:
- Descreva a opção
- Explique por que foi descartada (ou por que foi escolhida)

Use a tabela de avaliação para justificar cada rejeição.

### 3. **Decisão**
Declare claramente qual estilo foi escolhido. Se a decisão envolve estrutura de pastas ou componentes:
- Nomeie cada camada/módulo concretamente
- Descreva a responsabilidade de cada um
- Mostre como os dados e controle fluem entre eles

### 4. **Consequências**
Descreva o impacto dessa decisão:
- Benefícios esperados
- Custos ou dificuldades introduzidos
- Trade-offs (o que ganhamos vs. o que perdemos)

## Formato:

```markdown
# ADR-NNN: [Título conciso]

## Contexto
[Problema + Requisitos relevantes]

## Opções consideradas
- **Opção A**: Descrição + por que foi descartada
- **Opção B**: Descrição + por que foi descartada  
- **Opção C (escolhida)**: Descrição + por que foi escolhida

## Decisão
[Estilo escolhido com nomes concretos de pastas/módulos]

## Consequências
- Benefício 1
- Benefício 2
- Custo 1
- Custo 2
```
