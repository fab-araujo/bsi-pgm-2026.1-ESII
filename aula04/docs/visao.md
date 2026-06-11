# Documento de Visão
## Sistema de Gestão de Empréstimo de Equipamentos — UFRA Paragominas

**Versão:** 1.0
**Data:** Março de 2025
**Responsável:** Maria Souza (Analista de Requisitos)

---

## 1. Introdução

### 1.1 Propósito

Este documento descreve a visão geral do Sistema de Gestão de Empréstimo de Equipamentos da UFRA Paragominas. Seu objetivo é estabelecer os problemas que o sistema resolve, os envolvidos, as necessidades identificadas e as principais funcionalidades esperadas.

### 1.2 Escopo

O sistema controla o empréstimo de equipamentos audiovisuais e de informática do campus (notebooks, projetores e cabos HDMI) para professores e técnicos administrativos. O sistema não cobre contratos de longo prazo, empréstimos externos ao campus, nem controle de estoque ou manutenção.

---

## 2. Definição do Problema

| | |
|---|---|
| **O problema** | Ausência de controle formal dos empréstimos de equipamentos |
| **Afeta** | Coordenação de TI, professores, técnicos administrativos |
| **Impacto** | Equipamentos sem localização definida; atrasos não registrados; prejuízo ao patrimônio institucional |
| **Solução proposta** | Sistema informatizado de registro, acompanhamento e cobrança de multas por atraso |

---

## 3. Descrição dos Envolvidos (Stakeholders)

### 3.1 Usuários do sistema

| Perfil | Descrição | Responsabilidades |
|---|---|---|
| Atendente de TI | Servidor responsável pelo balcão de equipamentos | Registrar empréstimos e devoluções |
| Solicitante | Professor ou técnico que solicita o equipamento | Retirar e devolver no prazo |
| Coordenador de TI | Gestor do setor | Acompanhar atrasos e aplicar multas |

---

## 4. Visão Geral do Produto

### 4.1 Perspectiva do produto

O sistema é uma aplicação de linha de comando (CLI) executada localmente na máquina do atendente de TI. Não há acesso remoto ou interface web nesta versão.

### 4.2 Premissas e dependências

- Os dados são armazenados em memória durante a execução. Não há persistência entre sessões na versão 1.0 (previsto para v2.0).
- O envio de e-mail de notificação é simulado via terminal nesta versão.

### 4.3 Principais funcionalidades

- Registrar empréstimo de equipamento
- Registrar devolução com cálculo automático de multa por atraso
- Listar empréstimos em atraso com valor de multa acumulado

---

## 5. Restrições

- Desenvolvido em Python 3.11
- Interface exclusivamente via linha de comando
- Sem autenticação de usuários nesta versão
- Sem persistência de dados entre sessões nesta versão
