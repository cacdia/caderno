---
title: Fundamentos do MyST
description: Conceitos básicos, sintaxe e estrutura de documentos MyST.
keywords: [sintaxe, basico, introducao, markdown, referencias]
kernelspec:
  name: python3
  display_name: Python 3
  language: python
---

(fundamentos)=
# Fundamentos do MyST

O MyST (Markedly Structured Text) estende o Markdown padrão com recursos poderosos para documentação técnica e científica, trazendo a flexibilidade do reStructuredText para a simplicidade do Markdown.

## Sintaxe Básica

O MyST suporta toda a sintaxe padrão do CommonMark (negrito, itálico, listas, links), mas adiciona **Diretivas** e **Roles**.

### Diretivas e Admonições

As diretivas são blocos de conteúdo especial cercados por `:::`. As admonições são as mais comuns.

:::{note} Título da Nota
Este é o conteúdo de uma nota. Pode conter *markdown* e até outras diretivas.
:::

Tipos disponíveis: `note`, `warning`, `tip`, `important`, `attention`, `caution`, `danger`, `error`, `hint`, `seealso`.

:::{tip} Dica Pro
:class: dropdown
Você pode criar admonições colapsáveis adicionando a classe `dropdown`.
:::

### Matemática

O MyST suporta LaTeX nativamente.

**Inline:** $e^{i\pi} + 1 = 0$

**Bloco:**
$$
\frac{\partial \rho}{\partial t} + \nabla \cdot \vec{j} = 0
$$

Você pode rotular equações para referência:

```{math}
:label: eq-maxwell
\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}
```

Veja a equação {eq}`eq-maxwell`.

## Referências Cruzadas

O MyST possui um sistema robusto de referências cruzadas.

(minha-secao)=
### Referenciando Seções

Você pode adicionar um rótulo (label) antes de qualquer cabeçalho:

```markdown
(minha-secao)=
## Minha Seção
```

E referenciar depois:
- Usando o título da seção: [Minha Seção](#minha-secao)
- Usando texto personalizado: {ref}`clique aqui <minha-secao>`

### Referenciando Figuras e Tabelas

Use a role `{numref}` para referências numeradas automáticas (ex: "Figura 1", "Tabela 2").

- Veja a {numref}`fig-myst-logo` no capítulo de Visualização.
- Consulte a Tabela {numref}`tab-comparacao`.

:::{list-table} Comparação de Recursos
:label: tab-comparacao
:header-rows: 1

* - Recurso
  - Markdown Padrão
  - MyST
* - Diretivas
  - Não
  - Sim
* - Matemática
  - Limitado
  - Nativo (LaTeX)
:::

## Código

Blocos de código podem ter títulos, numeração de linhas e destaque.

```{code-block} python
:linenos:
:emphasize-lines: 2
:caption: hello.py
def hello_world():
    print("Hello, MyST!")
```

## Exportação

O MyST permite exportar seu projeto para diversos formatos profissionais.

- **HTML**: Sites estáticos com interatividade.
- **JATS XML**: Para arquivamento científico.
- **Markdown**: Para portabilidade.

A configuração é feita no `myst.yml`:

```yaml
project:
  exports:
    - format: html
      output: _build/html
    - format: jats
      output: _build/jats.xml
```
