# ADR-001: Arquitetura em Camadas para Sistema de Empréstimos v2.0

**Status:** Proposto  
**Data:** 2026-04-26

---

## Contexto

A v1.0 do sistema apresenta problemas estruturais documentados em PROBLEMAS.md:
- Lógica de negócio misturada com interface e notificações
- Adicionar novo tipo de equipamento exige alterar múltiplos pontos no código
- Regras de negócio não podem ser testadas isoladamente

**Requisitos críticos a atender:**

- **RNF03 (Manutenibilidade):** Adição de novo tipo de equipamento sem alterar múltiplos módulos
- **RNF04 (Testabilidade):** Módulos de regra de negócio testáveis de forma isolada, sem dependência de entrada do usuário ou estado externo

O sistema precisa de uma organização clara que permita que uma equipe iniciante compreenda e mantenha o código com facilidade.

---

## Opções consideradas

### 1. **Arquivo único** (emprestimos.py)
- Todo o código em um único arquivo Python
- Menu, regras e dados no mesmo lugar

**Por que foi descartada:**
- ❌ RNF03: Cada novo tipo de equipamento exigirá editar o mesmo arquivo, em múltiplos pontos
- ❌ RNF04: Impossível testar cálculo de multa sem executar o menu
- ✅ Vantagem única: Muito simples inicialmente

**Veredicto:** Não atende aos requisitos críticos.

---

### 2. **Arquitetura em Camadas** ← **ESCOLHIDA**
- Separação clara em responsabilidades: Modelo, Regras de Negócio, Interface
- Cada camada em módulo/pasta separada

**Por que foi escolhida:**
- ✅ RNF03: Novo tipo de equipamento → adiciona apenas uma nova regra na camada de negócio
- ✅ RNF04: Camada de regras isolada → testável sem estado externo
- ✅ RNF02: CLI continua funcional e responsiva
- ✅ Familiar para equipe iniciante (conceito básico de camadas)
- ✅ Sem overcomplexity desnecessária

---

### 3. **MVC (Model-View-Controller)**
- Separação em Model (dados), View (interface), Controller (fluxo)

**Por que foi descartada:**
- ✅ Atende RNF03 e RNF04
- ⚠️ Overcomplicated para uma CLI simples (MVC é pensado para UIs gráficas)
- ❌ Maior curva de aprendizado para equipe iniciante
- ❌ Adiciona complexidade desnecessária ao escopo atual

**Veredicto:** Funciona, mas custa mais que o benefício neste projeto.

---

## Decisão

**Adotar Arquitetura em Camadas** com a seguinte estrutura:

```
src/
├── modelo/              # Estruturas de dados
│   ├── __init__.py
│   └── entidades.py     # Classes: Equipamento, Emprestimo
│
├── regras/              # Lógica de negócio (pura, sem UI/notificações)
│   ├── __init__.py
│   ├── disponibilidade.py  # Verifica se equip. está disponível
│   ├── multa.py            # Calcula multa por atraso (ISOLÁVEL EM TESTES)
│   └── servico.py          # Coordena registrar(), devolver(), etc.
│
├── interface/           # Menu e entrada/saída de usuário (CLI)
│   ├── __init__.py
│   └── menu.py          # Menu principal
│
├── notificacao/         # Notificações (integração externa)
│   ├── __init__.py
│   └── email.py         # Simulação de envio de e-mail
│
└── main.py             # Ponto de entrada
```

### Fluxo de dados e responsabilidades:

1. **`interface/menu.py`** (Camada de Apresentação)
   - Exibe menu
   - Captura entrada do usuário
   - Valida formato de entrada
   - Chama funções de `regras/`

2. **`regras/`** (Camada de Lógica de Negócio)
   - Verifica regras: equipamento disponível? Data válida?
   - Calcula multa
   - Atualiza estado (registra empréstimo, marca como devolvido)
   - **Não conhece interface, não envia e-mail, não faz print()**
   - Retorna resultado (sucesso/erro com mensagem descritiva)

3. **`modelo/`** (Camada de Dados)
   - Estrutura `Equipamento`, `Emprestimo`
   - Gerencia lista de equipamentos e empréstimos
   - Sem lógica: apenas get/set

4. **`notificacao/`** (Camada de Integração)
   - Separada para possível substituição futura
   - Atualmente simula e-mail com print
   - Não é chamada por `regras/` — apenas por `interface/`

### Adição de novo tipo de equipamento (ex: Impressora):

- **v1.0 (problema atual):** Edita `emprestimos.py` para adicionar "impressora" ao if de tipos
- **v2.0 (com ADR):** Adiciona entrada em `modelo/entidades.py` e regra de multa em `regras/multa.py`
- **Resultado:** Múltiplos módulos? Não, apenas dentro da camada de regras, isolado

---

## Consequências

### ✅ Benefícios

1. **Manutenibilidade (RNF03 atendido):**
   - Novo tipo de equipamento: adiciona regra em um só lugar
   - Modificação em multa não afeta menu
   - Fácil encontrar onde cada coisa é feita

2. **Testabilidade (RNF04 atendido):**
   - `regras/multa.py` pode ser testado com `import` simples:
     ```python
     from src.regras.multa import calcular_multa
     assert calcular_multa("notebook", 5) == 50
     ```
   - Sem mock de banco de dados, arquivo, ou interface

3. **Compreensibilidade:**
   - Conceito intuitivo para iniciantes
   - Cada arquivo tem uma responsabilidade clara

4. **Escalabilidade futura:**
   - Trocar notificação de print() para chamada a API sem tocar em `regras/`
   - Adicionar BD sem reescrever `interface/`

### ⚠️ Custos e Trade-offs

1. **Mais arquivos para gerenciar:**
   - v1.0: 1 arquivo
   - v2.0: ~7 arquivos + pastas
   - Mitigado por documentação e nomes claros

2. **Complexidade de data flow:**
   - Precisa ser cuidadoso com dependências entre camadas
   - Possibilidade de erros em integração entre camadas

3. **Verbosidade:**
   - Pode parecer "muito código" para operações simples
   - Ganho em clareza compensa para manutenção de longo prazo

---

## Próximos passos

1. Criar estrutura de pastas (Parte 3)
2. Implementar `modelo/entidades.py` com classes Equipamento e Emprestimo
3. Implementar `regras/` com lógica pura (testável)
4. Implementar `interface/menu.py` que orquestra as camadas
5. Criar testes unitários para `regras/multa.py` (demonstra testabilidade)
