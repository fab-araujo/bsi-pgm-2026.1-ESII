# Resenha Aula 3 — Modelo de referência

> Este arquivo é a **solução-modelo** da Aula 3. Não copie. Use depois de
> entregar a sua para comparar profundidade e estrutura argumentativa.
> O que importa não são as palavras exatas — é a relação entre os
> conceitos de Valente e o projeto da disciplina.

---

## Questão 1 — Modelos UML como ferramentas de modelagem

### (a) Estrutura × comportamento

Valente apresenta no Cap. 4 que diagramas UML são **modelos** — abstrações
deliberadas que destacam aspectos relevantes para um propósito específico
ao custo de omitir outros. Esse posicionamento rompe com a visão de
modelos como "documentação universal" e os reposiciona como ferramentas
de pensamento dirigidas a perguntas específicas. O **diagrama de classes**
destaca a estrutura estática: que tipos existem, quais atributos têm,
como se relacionam por herança ou agregação. Omite a ordem de execução
e a temporalidade. O **diagrama de sequência** destaca o comportamento
dinâmico: como objetos trocam mensagens ao longo do tempo. Omite a
estrutura interna das classes envolvidas. Valente argumenta que são
complementares porque respondem a perguntas distintas — *como o sistema
é organizado?* vs. *como o sistema funciona?* — e nenhuma das duas
substitui a outra.

### (b) Consequência prática

Cada diagrama informa um tipo diferente de decisão. O diagrama de classes
apoia decisões sobre encapsulamento, hierarquia, tipos. O diagrama de
sequência apoia decisões sobre **alocação de responsabilidades** — quem
chama o quê, quem retorna o quê, em que ordem. Ao desenhar uma sequência,
o projetista descobre métodos que precisam existir e contratos que
precisam ser respeitados. O diagrama de classes, por sua vez, materializa
o resultado dessa alocação em estruturas concretas.

### (c) Aplicação ao UC01

O `casos_de_uso.md` textual diz apenas que o atendente fornece dados e
recebe confirmação — descrição no nível do ator. Não diz que o
`ServicoEmprestimo` precisa, em ordem, consultar o `RepositorioEmprestimo`
para validar disponibilidade do equipamento, construir o objeto
`Emprestimo` com data de devolução calculada, persistir o empréstimo,
marcar o equipamento indisponível e acionar o `Notificador`. Cada uma
dessas mensagens vira um método do contrato. O diagrama de sequência
torna esses passos — invisíveis no texto — visíveis ao projetista.

---

## Questão 2 — Arquitetura, design e os princípios de decomposição

Valente trata arquitetura no **Cap. 7** como a decomposição do sistema em
módulos e camadas com responsabilidades distintas e dependências
controladas; os **critérios** dessa decomposição — coesão, acoplamento e
ocultamento de informação — são os discutidos no Cap. 5. Esta questão
articula os dois: o Cap. 7 dá o *o quê* (separar em camadas), o Cap. 5 dá
o *porquê* (qualidade do design).

### (a) Definições

**Coesão** é o grau em que os elementos internos de um módulo trabalham
juntos para um único propósito; alta coesão significa que o módulo tem
uma responsabilidade clara e bem-definida. **Acoplamento** é o grau de
dependência entre módulos distintos; baixo acoplamento significa que
mudanças em um módulo dificilmente exigem mudanças em outros.
**Ocultamento de informação** é o princípio segundo o qual cada módulo
deve esconder de seus clientes as decisões de projeto suscetíveis a
mudança — expondo apenas uma interface estável.

### (b) Relações entre os princípios

O ocultamento de informação **habilita** o acoplamento baixo: se um
módulo expõe apenas o que é estável, seus clientes dependem só dessa
interface, não dos detalhes internos. Mudar a implementação interna não
afeta os clientes. Coesão e ocultamento se reforçam: um módulo coeso tem
menos detalhes a esconder, e o que ele esconde é internamente
consistente. Há tensão também: aumentar a coesão pode exigir dividir um
módulo em dois, o que pode aumentar o acoplamento aparente entre eles.
O design busca o equilíbrio — coesão alta o suficiente para que cada
módulo seja compreensível, acoplamento baixo o suficiente para que
mudanças sejam locais.

### (c) Aplicação ao projeto v2.0

A decomposição em camadas do ADR-001 é a aplicação direta da visão de
arquitetura de Valente (**Cap. 7**) — separar o sistema em módulos de
responsabilidade única e dependência controlada. A partir dela e dos
UC01–UC03:

- **`models/`:** `Equipamento` e `Emprestimo` como dataclasses. Coesão
  por entidade; ocultamento via tipos explícitos. Sem regras de negócio.
- **`services/ServicoEmprestimo`:** as três regras dos UCs (registrar,
  devolver, listar atrasados). Coesão alta — todas relacionadas a
  empréstimos.
- **`services/Notificador`:** apenas envio de notificações. Separação
  justificada por **coesão**: notificar tem motivo de mudança distinto
  de regra de empréstimo (mudar canal não muda regra).
- **`repositories/RepositorioEmprestimo`:** acesso a dados. Aplica
  **ocultamento de informação** — o serviço não sabe se os dados estão
  em memória, arquivo ou banco; depende só da interface.
- **`main.py`:** apenas leitura/exibição CLI. Acoplamento baixo com o
  restante: mudanças na interface não afetam o negócio.

---

## Questão 3 — Crítica fundamentada à documentação do sistema legado

### (a) Pontos frágeis no `docs/projeto.md`

1. **DP01 (estrutura monolítica).** O documento registra que "todas as
   funcionalidades estão concentradas em uma única classe `Sistema`".
   Em vocabulário de Valente: a classe `Sistema` tem **baixa coesão**
   (múltiplos motivos para mudar — regras de empréstimo, cálculo de
   multa, notificação, interface) e **viola ocultamento de informação**
   (não há separação entre dados, regras e apresentação). O documento
   reconhece o fato mas o classifica como "decisão de projeto", quando
   é uma fragilidade estrutural.

2. **DT03 (notificação acoplada à lógica).** Registrado como dívida, mas
   o documento não nomeia o problema com precisão: trata-se de **alta
   dependência entre módulos**. Mudar o canal de notificação (e-mail →
   SMS) força mudanças em todos os métodos do `Sistema` que notificam.
   Esse acoplamento poderia ter sido evitado desde a v1.0 com um módulo
   `Notificador` separado, expondo uma interface estável.

### (b) Ponto que antecipa boa prática

A presença explícita da tabela DT01–DT07 antecipa o conceito de **dívida
técnica registrada** que Valente apresenta no Cap. 1. O autor da v1.0
reconheceu suas próprias decisões frágeis em vez de mascará-las. Essa
postura — explicitar fragilidades em vez de escondê-las — é compatível
com o que Valente chama de engenharia honesta. A documentação do
sistema legado oferece à v2.0 um inventário pronto de pontos a corrigir.

### (c) Síntese

A explicitação da dívida no `projeto.md` revela uma postura amadurecida:
o desenvolvedor da v1.0 não tentou esconder fragilidades — ele as nomeou.
Isso inverte a lógica defensiva comum em código legado, onde fragilidades
são minimizadas ou apagadas. Em vocabulário do Cap. 1 de Valente, isso
caracteriza **dívida técnica deliberada**: o desenvolvedor sabia o custo
e registrou. Para a v2.0, essa postura inaugura um caminho concreto:
cada item DT01–DT07 vira um alvo de correção com critério técnico
associado. A documentação deixa de ser cerimônia administrativa e passa
a ser **instrumento de planejamento de manutenção**. Sem ela, a v2.0
começaria sem mapa.

---

## Questão 4 — Tipos como contratos: dicionários × classes

### (a) Prevenção de erros

No `emprestimos.py`, `equipamento["dispnoivel"]` (digitação errada de
"disponivel") não é detectada pelo Python até a hora da execução —
quando levanta `KeyError`. Substituindo por `Equipamento` como dataclass,
a mesma digitação errada — `equipamento.dispnoivel` — vira erro de
atributo capturável por verificação estática (mypy, Pyright) ou pelo
IDE em tempo de digitação. O contrato passa do *runtime* para o
*desenvolvimento*, antecipando o erro. Em uma equipe de três pessoas,
isso elimina uma classe inteira de bugs silenciosos.

### (b) Capacidade de evolução

Uma classe pode ganhar métodos sem afetar quem a consome porque os
clientes existentes continuam usando atributos por nome. Quando, na
Aula 5, eu adiciono `calcular_multa()` em subclasses de `Equipamento`,
o `RepositorioEmprestimo` que retorna `Equipamento` não muda — ele só
deixa de ignorar uma capacidade que agora existe. Em um dicionário não
há esse caminho: para adicionar `calcular_multa`, eu teria que mudar
de tipo (de `dict` para outra coisa) — refatoração externa em todos
os lugares que usam o dado. A classe permite **evolução por extensão**;
o dicionário força **evolução por substituição**.

### (c) Comunicação do design

Valente argumenta no Cap. 4 que o nome de um tipo carrega significado:
`Equipamento` declara o que aquele dado representa no domínio; `dict` é
genérico, exige que o leitor procure no código o que aquilo significa.
Em uma equipe, o tipo é o **primeiro vetor de comunicação** entre quem
escreve e quem lê. Isso é decisão de **projeto** — afeta como o time
pensa sobre o sistema — e não estilo cosmético. Um sistema com tipos
semânticos é fundamentalmente mais legível que um sistema com tipos
genéricos, ainda que a sintaxe pareça similar.
