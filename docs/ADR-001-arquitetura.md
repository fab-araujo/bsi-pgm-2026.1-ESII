ADR-001 — Decisão Arquitetural
Contexto

O sistema atual possui vários problemas de organização que dificultam sua manutenção e testes.

De acordo com os requisitos:

RNF03: o sistema deve permitir adicionar novos tipos de equipamentos sem precisar modificar várias partes do código.
RNF04: as regras de negócio devem poder ser testadas separadamente, sem depender de entrada do usuário ou variáveis externas.

Na versão atual do código:

A lógica de cálculo de multa está repetida em mais de um lugar.
O código usa variáveis globais, o que dificulta testes.
Há mistura de responsabilidade (regra de negócio, interface e dados no mesmo lugar).
Opções consideradas

Arquivo único
É simples, porém mantém todos os problemas atuais. Não atende bem os requisitos, pois o código continua difícil de manter e testar.

Arquitetura em camadas
Organiza o sistema separando responsabilidades (dados, regras e interface). Isso facilita manutenção e testes, atendendo os dois requisitos.

MVC
Também resolve os problemas, porém é mais complexo e não é tão necessário para um sistema simples de linha de comando.

Decisão

A arquitetura escolhida foi a arquitetura em camadas.

O sistema será dividido da seguinte forma:

domain/: onde ficam as entidades do sistema, como Equipamento e Emprestimo.
services/: onde ficam as regras de negócio, como registrar empréstimo, devolver e calcular multa.
repositories/: responsável por armazenar os dados (por enquanto em memória).
interfaces/: responsável pela interação com o usuário (menu, inputs e prints).
main.py: ponto de entrada do sistema.
Consequências

Pontos positivos:

O código fica mais organizado
As regras de negócio ficam separadas, facilitando testes
Fica mais fácil adicionar novos tipos de equipamentos
Evita repetição de código

Pontos negativos:

O projeto fica um pouco mais complexo no início
Teremos mais arquivos e pastas para organizar