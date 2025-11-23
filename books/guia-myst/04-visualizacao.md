---
title: Visualização e Diagramas
description: Figuras, subfiguras e diagramas com Mermaid
keywords: [figures, images, mermaid, diagrams, visualization]
kernelspec:
  name: python3
  display_name: Python 3
---

# Visualização e Diagramas

Uma imagem vale mais que mil palavras. O MyST oferece ferramentas robustas para incluir figuras, organizar layouts de imagens e criar diagramas via código.

## Figuras e Imagens

O MyST estende o Markdown padrão com diretivas para figuras legendadas e referenciáveis.

### Figura Básica

:::{figure} https://placehold.co/200x100.png
:label: fig-myst-logo
:width: 200px
:align: center

O logotipo do MyST Markdown.
:::

Podemos referenciar a Figura {numref}`fig-myst-logo` em qualquer lugar do texto.

### Subfiguras (Grid de Imagens)

Você pode agrupar múltiplas imagens usando um grid.

:::{figure} https://placehold.co/100x100.png?text=A
:label: fig-logo-a
:width: 100%
Logotipo A
:::

:::{figure} https://placehold.co/100x100.png?text=B
:label: fig-logo-b
:width: 100%
Logotipo B
:::

Comparação entre dois logotipos (veja {numref}`fig-logo-a` e {numref}`fig-logo-b`).

## Diagramas com Mermaid

O MyST suporta nativamente diagramas Mermaid, permitindo criar fluxogramas, diagramas de sequência e muito mais usando apenas texto.

### Fluxogramas

```{mermaid}
graph TD
    A[Início] --> B{Decisão}
    B -->|Sim| C[Processo 1]
    B -->|Não| D[Processo 2]
    C --> E[Fim]
    D --> E
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style E fill:#ccf,stroke:#333,stroke-width:2px
```

### Diagramas de Sequência

```{mermaid}
sequenceDiagram
    participant U as Usuário
    participant S as Sistema
    participant DB as Banco de Dados
    
    U->>S: Solicita dados
    S->>DB: Query SQL
    DB-->>S: Resultados
    S-->>U: Resposta JSON
```

### Diagramas de Classe

```{mermaid}
classDiagram
    Animal <|-- Duck
    Animal <|-- Fish
    Animal : +String name
    Animal : +int age
    
    class Duck{
        +String beakColor
        +swim()
        +quack()
    }
```

### Gráficos de Gantt

```{mermaid}
gantt
    title Cronograma do Projeto
    dateFormat  YYYY-MM-DD
    section Fase 1
    Pesquisa           :a1, 2025-01-01, 30d
    Análise            :a2, after a1, 20d
    section Fase 2
    Desenvolvimento    :2025-02-20, 45d
```

## Gráficos Interativos (Vega-Lite)

Você também pode incluir especificações Vega-Lite diretamente.

```{code-cell} python
:tags: [remove-input]
import altair as alt
from vega_datasets import data

source = data.cars()

alt.Chart(source).mark_circle(size=60).encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()
```
