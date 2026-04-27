# ADR-001-EXEMPLO: Usar padrão de fila de mensagens para processamento assíncrono

**Status:** Aceito  
**Data:** 2025-03-15

## Contexto

O sistema de notificações estava bloqueando a interface do usuário durante o envio de e-mails. Usuários relatavam delays ao registrar empréstimos ou devoluções. A equipe é pequena (3 pessoas) e precisa de uma solução simples de manter.

**Requisitos impactados:**
- RNF01 (Desempenho): Operações > 1 segundo causadas por bloqueios de rede
- RNF02 (Usabilidade): Menu responsivo

## Opções consideradas

### 1. **Manter arquitetura síncrona atual**
- Continuar enviando e-mail dentro da mesma função que registra o empréstimo
- **Rejeitada:** Não resolve o problema de bloqueio. Não atende RNF01.

### 2. **Usar threads com Queue (fila local)**
- Criar thread dedicada que processa fila de mensagens em memória
- Registrar empréstimo enfileira mensagem e retorna imediatamente
- **Escolhida:** Simples de implementar, sem dependências externas, resolve bloqueio.

### 3. **Usar broker de mensagens (RabbitMQ, Redis)**
- Outsourcing de fila para ferramenta profissional
- **Rejeitada:** Overcomplicated para 3 pessoas. Cria dependência externa (RNF05).

## Decisão

Implementar **arquitetura em camadas com fila local**:

```
src/
├── modelo/          # Estruturas de dados (Emprestimo, Equipamento)
├── regras/          # Lógica de negócio (cálculo multa, disponibilidade)
├── notificador/     # Fila e processamento assíncrono de e-mails
└── interface/       # Menu CLI
```

**Fluxo:**
1. `interface` valida entrada e chama `regras.registrar()`
2. `regras.registrar()` adiciona empréstimo ao modelo
3. `regras.registrar()` enfileira mensagem em `notificador.fila`
4. Retorna imediatamente para interface
5. Thread daemon do `notificador` processa fila continuamente

## Consequências

**Benefícios:**
- ✅ Menu responsivo (RNF01)
- ✅ Sem dependências externas (RNF05)
- ✅ Testabilidade: `regras` pode ser testado sem mock de thread
- ✅ Compreensível para equipe iniciante

**Custos:**
- Mensagens na fila podem ser perdidas se processo morrer (inaceitável para produção)
- Requer sync cuidadoso entre threads
- Monitoramento de fila é manual

**Trade-off:** Simplicidade vs. Garantia de entrega. Para MVP em ambiente acadêmico, aceitável.
