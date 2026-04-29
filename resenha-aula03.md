# Resenha Aula 3 – Modelos UML e Design de Componentes

**Aluno:** Thiago Araujo  
**Data:** <29/04/2026>

## Questão 1 – Modelos UML como ferramentas de modelagem

### (a) Estrutura x comportamento
Os modelos UML são uma forma de entender melhor os sistemas, mas não devem ser usados em excesso. A partir da abordagem de Valente, o objetivo não é criar diagramas muito longos, e sim pensar por meio deles para conseguir transmitir como o sistema vai funcionar.

Existe uma diferença importante entre estrutura e comportamento. A estrutura é representada pelo diagrama de classes, que mostra como o sistema é formado, quais elementos existem e como se relacionam. Já o comportamento é mostrado no diagrama de sequência, que apresenta como os objetos interagem ao longo do tempo.

Esses dois tipos de diagramas respondem perguntas diferentes. Apenas o diagrama de classes pode não ser suficiente para entender como as ações acontecem. Por outro lado, o diagrama de sequência sozinho também pode não ser tão intuitivo. Por isso, o uso conjunto dos dois torna a compreensão mais completa e menos confusa.

### (b) Consequência prática
Na prática, usar apenas um tipo de diagrama pode gerar entendimento incompleto do sistema. Quando combinamos estrutura e comportamento, conseguimos ter uma visão mais clara tanto da organização quanto do funcionamento do sistema.

Isso ajuda principalmente na comunicação entre desenvolvedores, já que cada diagrama complementa o outro. Assim, fica mais fácil entender o que o sistema faz e como ele faz.

### (c) Aplicação ao UC01
No caso do UC01, o diagrama de sequência mostra claramente a funcionalidade que se deseja alcançar, como quem chama quem e em quais etapas.

Já o diagrama de classes mostra onde essa funcionalidade acontece dentro do sistema. Ou seja, um explica o fluxo e o outro mostra a base estrutural. Juntos, eles dão uma visão mais completa do sistema.

---

## Questão 2 – Arquitetura, design e os princípios de decomposição

### (a) Definições
O design de software envolve como o sistema é estruturado. Segundo Valente, essa organização não serve apenas para deixar o sistema “bonito”, mas também para facilitar manutenção e evolução.

Coesão é o quanto um módulo é focado em uma única responsabilidade. Quanto maior a coesão, mais fácil entender e corrigir aquele módulo.

Acoplamento é o nível de dependência entre módulos. Quando é muito alto, pequenas mudanças podem causar efeitos inesperados em várias partes do sistema.

Ocultamento de informação serve para esconder os detalhes internos de um módulo, expondo apenas o necessário. Isso evita que outras partes dependam da implementação interna.

### (b) Relações entre os princípios
Esses conceitos estão diretamente ligados. Quando há bom ocultamento de informação, o acoplamento tende a diminuir.

Além disso, módulos com responsabilidades bem definidas (alta coesão) facilitam a manutenção. Porém, é importante não dividir demais a ponto de prejudicar a comunicação entre os módulos.

### (c) Aplicação ao projeto V2.0
Pensando no projeto V2.0, faz sentido organizar o sistema em camadas. Isso melhora não só a organização, mas também facilita evolução e escalabilidade.

Separar por camadas evita confusão de responsabilidades e deixa o sistema mais preparado para mudanças futuras.

---

## Questão 3 – Crítica fundamentada à documentação do sistema legado

### (a) Pontos frágeis
Um ponto frágil é a baixa coesão, onde um mesmo módulo faz muitas coisas ao mesmo tempo. Isso dificulta a manutenção e torna o sistema mais confuso.

Outro problema é o alto acoplamento. Sem uma boa separação, os módulos ficam muito dependentes uns dos outros, dificultando mudanças.

Também há falha no ocultamento de informações, com muitos dados expostos e uso de estruturas globais. Isso aumenta o risco de erros e dificulta a evolução do sistema.

### (b) Ponto forte
Um ponto positivo é que a documentação deixa claro que existem problemas no sistema. Ou seja, a dívida técnica está identificada.

Isso é importante porque permite saber por onde começar as melhorias, facilitando a evolução do sistema.

### (c) Síntese
No geral, o sistema legado apresenta problemas clássicos como baixa coesão, alto acoplamento e falta de encapsulamento.

Por outro lado, a existência de documentação que aponta esses problemas já é um avanço, pois direciona futuras melhorias.

---

## Questão 4 – Tipos como contratos: dicionários x classes

### (a) Prevenção de erros
Dicionários são mais simples, mas estão mais sujeitos a erros, como uso de chaves incorretas ou tipos inesperados, que só aparecem em tempo de execução.

Já as classes funcionam como contratos, definindo claramente quais dados existem e como devem ser usados, reduzindo erros.

### (b) Capacidade de evolução
Classes são mais fáceis de evoluir, pois permitem adicionar novos comportamentos sem quebrar o que já existe.

Dicionários apenas armazenam dados e não possuem comportamento, o que limita sua evolução.

### (c) Comunicação do design
Classes também melhoram a comunicação entre desenvolvedores, pois deixam claro como o sistema deve ser utilizado.

Dicionários genéricos podem gerar confusão, já que não deixam explícito quais dados são esperados nem como devem ser usados.

Além disso, pensar nos tipos como contratos ajuda na robustez do sistema, na prevenção de erros e na manutenibilidade, além de melhorar a legibilidade do código.