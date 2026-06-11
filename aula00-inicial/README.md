# Sistema de Gestão de Empréstimo de Equipamentos — UFRA Paragominas

Sistema desenvolvido para controle de empréstimo de equipamentos do campus
(notebooks, projetores, cabos HDMI) para uso em aulas e eventos institucionais.

## Equipe

| Nome         | Função                  |
|--------------|-------------------------|
| João Silva   | Desenvolvedor Backend   |
| Maria Souza  | Analista de Requisitos  |
| Pedro Lima   | Testador / QA           |

## Documentação

- [Documento de Visão](docs/visao.md)
- [Documento de Requisitos](docs/requisitos.md)
- [Casos de Uso](docs/casos_de_uso.md)
- [Documento de Projeto](docs/projeto.md)
- [Histórico de Problemas Identificados](PROBLEMAS.md)

## Pré-requisitos

- Python 3.11 ou superior

## Como instalar

```bash
git clone https://github.com/ufra-paragominas/emprestimo-equipamentos.git
cd emprestimo-equipamentos
```

## Como executar

```bash
python emprestimos.py
```

## Funcionalidades

- Registrar empréstimo de equipamento
- Registrar devolução com cálculo automático de multa por atraso
- Listar empréstimos em atraso

## Observações

Este sistema foi desenvolvido como versão inicial (v1.0).
Melhorias de arquitetura e qualidade de código estão previstas para as próximas versões.
