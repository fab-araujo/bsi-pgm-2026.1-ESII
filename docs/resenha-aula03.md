# Resenha Aula 3 — Modelos UML e Design de Componentes

**Aluno:** [ADRIO SANTOS DOS SANTOS]  
**Data:** [29 / ABRIL / 2026]

## Questão 1 — Modelos UML como ferramentas de modelagem

### (a) Estrutura × comportamento

Quando a gente fala de UML como modelo (Cap. 4 de Valente), a ideia central é que você nunca está mostrando "tudo", mas sim escolhendo o que importa para aquele momento. No caso do diagrama de classes, o foco é estrutural: ele evidencia quais são as entidades do sistema, seus atributos e os relacionamentos entre elas. Ou seja, ele responde "quem existe" e "como estão conectados". Só que ele deixa invisível o comportamento dinâmico: não mostra em que ordem as mensagens são trocadas, quando cada chamada acontece, ou sob quais condições um objeto chama outro. Já o diagrama de sequência faz exatamente o oposto: ele ignora a estrutura detalhada e foca no fluxo temporal de mensagens, deixando claro quem chama quem, em qual sequência, e até que ponto cada participante depende do outro. É por isso que são complementares: um mostra "o quê existe", o outro mostra "como funciona em tempo real". Sem os dois, tem-se uma visão incompleta do sistema.

### (b) Consequência prática

Na prática, isso impacta direto nas decisões de projeto. O diagrama de classes ajuda a definir responsabilidades e organização do sistema, como decidir se uma regra de negócio fica na classe "Empréstimo" ou "Cliente", ou ainda como evitar acoplamento excessivo entre partes do sistema. Já o diagrama de sequência entra quando você precisa validar cenários reais de uso, ajudando a perceber gargalos, chamadas desnecessárias ou até violações de encapsulamento. Ele força você a pensar no fluxo real da execução, o que muitas vezes revela problemas que não aparecem na estrutura estática.

### (c) Aplicação ao UC01

Aplicando isso ao UC01 (Registrar Empréstimo), o documento de casos_de_uso.md textual deixa uma ambiguidade crítica: diz que "o sistema valida se o equipamento está disponível" e "registra o empréstimo", mas não deixa explícito a ordem exata (primeiro valida, depois registra? Ou registra logo?) nem quem (qual classe/objeto) é responsável por cada ação. Um diagrama de sequência revelaria isso sem margem pra interpretação: Controlador recebe requisição → chama validarDisponibilidade() no Equipamento → registra Empréstimo no Repositório. Deixa claro: ordem, dependências, qual classe tem qual responsabilidade, onde o fluxo pode falhar. Além disso, força a existência de métodos concretos (não apenas "validação" abstrata, mas um método real que precisa ser implementado). Isso evita interpretações divergentes entre desenvolvedores e já começa a desenhar a arquitetura quase que automaticamente.

## Questão 2 — Arquitetura, design e os princípios de decomposição

### (a) Definições

Quando você sai da teoria e tenta projetar algo de verdade, esses três conceitos viram praticamente seu "radar" de qualidade. Coesão, pra mim, é o quão focada uma parte do sistema é em uma única responsabilidade — uma classe coesa faz poucas coisas, mas faz bem feito e com sentido entre si. Já acoplamento é o nível de dependência entre partes: quanto mais uma classe precisa conhecer detalhes de outra, mais acoplado o sistema fica (e mais frágil também). Ocultamento de informação é o instrumento que torna os outros dois viáveis: esconder os detalhes internos e expor só o necessário, tipo uma interface limpa que protege o resto da bagunça interna e permite que classes se relacionem sem depender de implementação alheia.

### (b) Relações entre os princípios

Esses conceitos se conectam direto. Quando você aplica bem o ocultamento de informação, você naturalmente reduz o acoplamento, porque outras partes não precisam saber "como" algo funciona, só "o que" ele faz. Isso também ajuda a manter a coesão, porque cada módulo fica responsável por seu próprio comportamento interno, sem espalhar lógica por todo o sistema. Mas nem tudo é perfeito: às vezes, tentar deixar um módulo super coeso pode fazer ele depender de outros para completar tarefas, aumentando o acoplamento. Então é sempre um equilíbrio — você ajusta conforme o contexto do projeto.

### (c) Aplicação ao projeto v2.0

Pensando no projeto v2.0 com camadas: **em models/**, classes como Cliente, Livro e Emprestimo — são entidades do domínio com alta coesão, cada uma responsável por seus dados e regras internas, sem depender de persistência. **Em repositories/**, ClienteRepository e LivroRepository isolam o acesso ao banco de dados, aplicando ocultamento de informação para que nenhuma outra classe precise saber como os dados são armazenados, reduzindo acoplamento ao banco. **Em services/**, EmprestimoService coordena regras de negócio complexas (validar disponibilidade, registrar empréstimo), mantendo models coesos e a interface desacoplada da persistência. **Em main.py**, a orquestração inicial — entrada do usuário e chamadas aos serviços — mantém baixo acoplamento porque não conhece detalhes de como as coisas funcionam internamente, só o contrato de cada serviço.

## Questão 3 — Crítica fundamentada à documentação do sistema legado

### (a) Pontos frágeis

Lendo docs/projeto.md com o "óculos" do Cap. 7, dois pontos são claramente frágeis. Primeiro: a classe `Sistema` **acessa diretamente variáveis globais** (`equipamentos[]` e `emprestimos_registrados[]` — registrado como DT02), o que viola **ocultamento de informação** e configura **acoplamento por variável global**. Qualquer mudança na estrutura dessas listas quebra a classe. Segundo: a mesma classe `Sistema` trata tanto do registro de empréstimos quanto da **notificação de usuário** (DT03), o que é **baixa coesão** — responsabilidades sem relação direta misturadas no mesmo lugar. Quando algo falha, fica impossível diagnosticar se foi problema de negócio ou de comunicação. O sistema "funciona", mas é frágil: pequenas mudanças causam grandes impactos.

### (b) Ponto forte

Um ponto positivo é que o próprio documento reconhece explicitamente em DP01: "A equipe reconhece que a ausência de separação em camadas representa **dívida técnica intencional**. A refatoração para arquitetura em camadas está planejada para a v2.0." Isso já aponta para uma intenção de separação de responsabilidades, mesmo que ainda não implementada. Isso é uma boa decisão porque mostra maturidade — não é ignorância de que o código é frágil, é **decisão consciente de trocar qualidade por prazo**. À luz de Valente, isso é exatamente o que um desenvolvedor maturo faz: reconhece a dívida e a registra para cobrar juros depois, em vez de fingir que o sistema é perfeito ou deixar surpresa para quem vai herdar.

### (c) Síntese

Sobre a parte mais interessante: a tabela de dívida técnica (DT01–DT07). Isso aqui é quase um "sinal verde" de maturidade. Reconhecer dívida técnica explicitamente mostra que o desenvolvedor sabe que fez concessões — provavelmente por prazo ou simplicidade — e não está fingindo que o sistema está perfeito. Conectando com o Cap. 1, dívida técnica não é o problema em si; o problema é ignorá-la. Essa transparência já muda totalmente a postura para a v2.0: em vez de sair refatorando no escuro, você tem um mapa claro do que precisa melhorar. Ou seja, não é só um sistema para evoluir — é um sistema com direção.

## Questão 4 — Tipos como contratos: dicionários × classes

### (a) Prevenção de erros

Quando o Valente fala que classes são "contratos tipados" (Cap. 4 e 5), ele tá dizendo que elas não servem só pra guardar dados, mas pra definir regras claras sobre o que pode existir e como pode ser usado. No caso do emprestimos.py, usar dicionários tipo `equipamento["disponivel"]` abre espaço pra vários erros silenciosos: um simples typo na chave ("disponivel" vs "disponível") já quebra tudo em tempo de execução, ou pior, passa despercebido dependendo do contexto. Também não há garantia de que aquela chave existe ou de que o valor tem o tipo certo. Se fosse uma classe Equipamento, esses problemas diminuem bastante: o atributo teria um nome fixo, poderia ser validado no construtor e até protegido com regras (tipo não deixar um valor inválido entrar). Ou seja, você troca erros imprevisíveis por falhas mais controladas e fáceis de rastrear.

### (b) Capacidade de evolução

Sobre evolução, a diferença fica ainda mais clara. Uma classe pode crescer "pra dentro" sem impactar quem usa. Se você adiciona um método como `calcular_multa()`, quem já usa a classe continua funcionando normalmente, porque o contrato público não foi quebrado — você só estendeu comportamento. Já com dicionário, qualquer nova lógica precisa ser implementada fora, espalhando regras pelo sistema. Isso aumenta acoplamento e dificulta manutenção, porque não existe um lugar central que "manda" no comportamento daquele dado.

### (c) Comunicação do design

E aí entra o ponto mais sutil: comunicação. Quando você vê um tipo chamado Equipamento, isso já transmite significado — você sabe que aquilo representa uma entidade do domínio, com regras e responsabilidades. Um `dict`, por outro lado, não diz nada por si só; você precisa ler o código inteiro pra entender o que ele representa. É por isso que o Valente trata clareza de modelo como parte do projeto: não é só estética, é sobre tornar o sistema compreensível, previsível e mais fácil de evoluir sem dor.
