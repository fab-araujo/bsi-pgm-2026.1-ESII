# Reflexões

## Aula 04 — SRP

A fronteira mais difícil de tomar foi a separação entre
**`ServicoEmprestimo` e `Notificador`**. Em uma primeira leitura do
`emprestimos.py`, parecia natural manter o envio de e-mail dentro do
método `devolver`: afinal, "notificar o usuário sobre a multa" parece
parte do mesmo fluxo de negócio. O critério que me fez decidir pela
separação veio de Valente Cap. 5, na seção sobre coesão: um módulo
coeso tem um único motivo para mudar. Olhando assim, ficou claro
que **o cálculo da multa muda por uma razão (regras de cobrança,
definidas pelo setor de patrimônio) e a notificação muda por outra
razão (canal de comunicação — hoje e-mail, amanhã SMS ou push)**.
Stakeholders distintos = motivos de mudança distintos = classes
distintas.

A dificuldade foi resistir à tentação de "facilitar agora": juntar
tudo no Service deixaria o código menor no curto prazo, mas qualquer
mudança futura em qualquer um dos lados (regra ou canal) forçaria
editar um método que faz duas coisas. Decidi pela separação aplicando
o "teste do *e*" — se preciso descrever a classe usando a palavra "e",
ela está fazendo demais. A versão final tem `ServicoEmprestimo`
coordenando regra de empréstimo e `Notificador` isolando o canal de
comunicação, conectados apenas pela chamada
`self.notificador.notificar_*` — interface mínima, evolução independente.

## Aula 05 — OCP

A hierarquia criada — `Notebook`, `Projetor` e `Cabo` herdando de
`Equipamento` — resolve o problema da variação por tipo: cada subclasse
fornece sua fórmula de multa sem que o `ServicoEmprestimo` precise
conhecer o tipo concreto. Para os equipamentos atuais, isso funciona e
atende o RNF01 (adição de novo tipo sem alterar o serviço).

O problema aparece quando o eixo de variação muda. Um equipamento com
multa calculada por hora, ou cuja política dependa do dia da semana,
não é uma nova subclasse do mesmo problema — é uma nova dimensão de
variação. Nesse caso, a hierarquia plana que criei precisaria ser
reestruturada: ou a lógica condicional voltaria ao `calcular_multa`, ou
haveria uma proliferação de subclasses como `NotebookFimDeSemana`.
Valente (Cap. 5) aponta esse risco ao lembrar que "o OCP é mais útil
quando existe um número limitado e conhecido de variações" — encapsular
variações hipotéticas viola YAGNI e gera complexidade sem retorno
imediato.

Para o cenário das multas por hora ou por dia da semana, uma solução
mais robusta seria separar a política de cobrança do tipo de
equipamento, talvez com um objeto `PoliticaMulta` injetado em
`Equipamento`. Com os tipos atuais — fixos e estáveis — a hierarquia
presente é suficiente e não exige reestruturação.

## Aula 06 — Verificação de LSP

O contrato de `Equipamento.calcular_multa(dias_atraso: int) -> float`
estabelece retorno do tipo `float >= 0.0`, sem lançamento de exceção.

**`Notebook`:** `calcular_multa(0)` → `max(0.0, 0 * 10.0)` = `0.0` ✓;
`calcular_multa(-5)` → `max(0.0, -50.0)` = `0.0` ✓. Nenhuma exceção
possível. LSP satisfeito.

**`Projetor`:** `calcular_multa(0)` → `0.0` ✓; `calcular_multa(-5)` →
`0.0` ✓. LSP satisfeito.

**`Cabo`:** `calcular_multa(0)` → `0.0` ✓; `calcular_multa(-5)` →
`0.0` ✓. LSP satisfeito.

As três subclasses honram o contrato. O `ServicoEmprestimo` pode
receber qualquer `Equipamento` e chamar `calcular_multa` com qualquer
inteiro sem risco de exceção ou valor negativo.

## Aula 06 — DIP

Antes da alteração, o `ServicoEmprestimo` criava internamente seu
repositório e seu notificador. Isso significa que ele não apenas
*usava* essas dependências — ele *decidia qual* usar. A dependência
era unidirecional e apontava para baixo: a camada de serviço
controlava quem a implementava.

Com a injeção, essa relação se inverte. O `ServicoEmprestimo` agora
descreve o que precisa (um objeto com `buscar_equipamento`,
`salvar_emprestimo` etc.; outro com `notificar_*`) sem determinar quem
vai fornecê-lo. Quem instancia e injeta passa a ser o `main.py`.
Valente (Cap. 5) descreve exatamente esse movimento: módulos de alto
nível não devem depender de módulos de baixo nível; ambos devem
depender de abstrações.

A mudança não é só técnica. Conceitualmente, o `ServicoEmprestimo`
deixou de ser criador de infraestrutura e se tornou consumidor de
contratos. Quem decide agora é a camada mais externa — `main.py` —
que escolhe qual repositório e qual notificador fornecer. Na prática,
isso abre espaço para instanciar o serviço com um `RepositorioFalso`
que armazena dados em listas e um `NotificadorFalso` que registra
chamadas em vez de enviar e-mails. As regras de negócio ficam isoladas
da infraestrutura, que era exatamente o que o RNF02 exigia e que a
Aula 5 ainda não resolvia por completo.

## Aula 08 — Testes

O teste de integração `test_fluxo_registrar_devolver_com_componentes_reais`
captura algo que os testes de unidade não capturam: a **colaboração real**
entre serviço, repositório e notificador concretos. Os testes de unidade
trocam o repositório por um `RepositorioFake` e o notificador por um
`NotificadorSpy`; eles provam que o `ServicoEmprestimo` se comporta certo
*dado* que as dependências cumprem o contrato. Mas não provam que a
implementação concreta cumpre esse contrato. O teste de integração fecha
essa lacuna: se a assinatura de um método do `RepositorioEmprestimo` real
divergisse do que o serviço espera, só a integração pegaria.

Em compensação, ele captura *menos* do que um teste de unidade quando se
trata de **casos de borda**. Para verificar a multa de um atraso, o teste
de unidade manipula diretamente a `data_devolucao` do empréstimo no Fake e
isola o cálculo; fazer isso com componentes reais seria mais frágil e
lento, e um eventual erro apontaria para um trecho maior, dificultando o
diagnóstico. A unidade localiza a falha com precisão; a integração garante
que as peças se encaixam. As duas se complementam — nenhuma substitui a outra.

## Aula 09 — TDD

Comparando o mesmo comportamento escrito como teste TDD (`assert multa == 0.0`)
e como cenário BDD (`Dado um atraso de 1 dia ... Então a multa deve ser R$ 0,00`),
o BDD comunica melhor com um cliente **não técnico**. O motivo é a linguagem: o
Given-When-Then descreve o comportamento observável em português corrente, sem
`assert`, sem nome de função, sem tipo de retorno — alguém do negócio lê o cenário
e concorda (ou discorda) com a regra. O teste TDD fala a língua do desenvolvedor:
é mais preciso, mas pressupõe ler código.

Eu preferiria **BDD** quando a especificação precisa ser validada por quem não
programa — o setor de patrimônio que define a regra da multa, por exemplo —, ou
quando o "o que" (o comportamento de negócio) importa mais que o "como". Preferiria
**TDD** para regras internas finas, algoritmos e código sem um "cliente de negócio"
claro, onde a precisão do `assert` rende mais que o alcance da linguagem natural.
Na prática os dois convivem: BDD nos fluxos de negócio, TDD nas unidades. Nos dois,
o teste vem antes e guia o design.

## Aula 10 — Factory e Facade

**Factory e o OCP.** A `FabricaEquipamento` ainda concentra uma decisão `tipo → classe`
(no meu caso, um mapa `dict`). Na Aula 5 combatemos o `if/elif` por tipo justamente
porque ele se **espalhava** pelos métodos do serviço — toda regra nova obrigava a
editar vários pontos. Aqui o acoplamento é aceitável porque mudou de natureza: deixou
de estar espalhado e passou a viver **num único lugar**, isolado do resto do sistema.
O papel da fábrica é exatamente esse — **absorver** a dependência das classes concretas
(`Notebook`, `Projetor`, `Cabo`) para que o repositório e os demais módulos fiquem
livres dela. Acrescentar um tipo novo agora é uma linha no mapa da fábrica, e nada mais
muda. Como diz Valente (Cap. 6), a fábrica encapsula a criação: o `if`/mapa não
desapareceu, foi confinado onde só ele tem motivo para existir.

**Facade e o DIP.** Extrair a `SistemaDeEmprestimos` **não** desfaz o DIP da Aula 6. A
fachada é a **raiz de composição**: o único ponto que conhece os concretos e os liga
(`RepositorioEmprestimo`, `Notificador`, `ServicoEmprestimo`). Essa montagem antes
estava no `main.py`; apenas mudou de lugar. O DIP continua intacto onde importa: o
`ServicoEmprestimo` segue dependendo das **abstrações** (`IRepositorioEmprestimo`,
`INotificador`), e por isso os testes continuam injetando dublês (`RepositorioFake`,
`NotificadorSpy`) **direto no serviço** — não na fachada. Nenhum teste precisou mudar,
o que confirma que a inversão de dependência permaneceu. A fachada só simplificou o
ponto de entrada: o `main.py` agora monta o subsistema inteiro em uma linha.

