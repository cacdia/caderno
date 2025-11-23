---
title: Componentes de Interface (UI)
description: Cards, grids, tabs e componentes interativos para layout
keywords: [cards, tabs, grids, design, ui, layout]
---

# Componentes de Interface (UI)

O MyST oferece componentes modernos para criar layouts ricos e interativos, indo muito além do documento linear tradicional.

## Cards (Cartões)

Cards são contêineres versáteis para destacar conteúdo.

### Card Simples

:::{card} Título do Card
Conteúdo do card com **formatação** markdown.
:::

### Card com Link

:::{card} Documentação MyST
:link: https://mystmd.org/guide

Acesse a documentação completa do MyST.
:::

### Card com Imagem de Cabeçalho

:::{card}
:link: https://mystmd.org

![MyST Logo](https://dummyimage.com/300x150/4A90E2/ffffff&text=MyST)

**MyST Markdown**
^^^
Sistema moderno de documentação técnica e científica.
:::

### Card com Rodapé

:::{card} Projeto Exemplo
:footer: Última atualização: 2025-11-22

Descrição do projeto com recursos interessantes.
:::

## Grids

Grids criam layouts responsivos com múltiplas colunas.

### Grid 2 Colunas

::::{grid} 2

:::{card} Coluna 1
Conteúdo da primeira coluna
:::

:::{card} Coluna 2
Conteúdo da segunda coluna
:::

::::

### Grid 3 Colunas com Gutter

::::{grid} 3

:::{card} Card 1

📊 **Análise**
:::

:::{card} Card 2

🔧 **Desenvolvimento**
:::

:::{card} Card 3

🚀 **Deploy**
:::

::::

### Grid Responsivo

::::{grid} 1 1 2 3

:::{card} Mobile: 1 coluna
Tablet: 1 coluna
Desktop: 2 colunas
Wide: 3 colunas
:::

:::{card} Adapta ao Tamanho
Automaticamente responsivo
:::

:::{card} Grid Inteligente
Layout fluido
:::

::::

## Tabs (Abas)

Tabs permitem organizar conteúdo alternativo ou relacionado.

### Tabs Básicos

::::{tab-set}

:::{tab-item} Python
```python
def hello():
    print("Hello from Python!")
```
:::

:::{tab-item} JavaScript
```javascript
function hello() {
    console.log("Hello from JavaScript!");
}
```
:::

:::{tab-item} Rust
```rust
fn hello() {
    println!("Hello from Rust!");
}
```
:::

::::

### Tabs Sincronizados

Use `sync:` para sincronizar múltiplos tab-sets:

::::{tab-set}

:::{tab-item} Python
Código Python
:::

:::{tab-item} JavaScript
Código JavaScript
:::

::::

::::{tab-set}

:::{tab-item} Python
Mais código Python
:::

:::{tab-item} JavaScript
Mais código JavaScript
:::

::::

## Dropdowns

Seções colapsáveis para economizar espaço.

### Dropdown Simples

:::{dropdown} Clique para expandir
Conteúdo oculto inicialmente.
:::

### Dropdown Aberto por Padrão

:::{dropdown} Detalhes Técnicos
:open:

Este dropdown começa aberto.
:::

### Admonições Colapsáveis

:::{note} Nota Importante
:class: dropdown

Esta nota pode ser recolhida.
:::

:::{warning} Atenção!
:class: dropdown
:open:

Aviso colapsável iniciando aberto.
:::

## Aside (Conteúdo Lateral)

O aside move conteúdo para a margem lateral (em telas grandes).

:::{aside}
Este é um comentário lateral que aparece na margem.
:::

O texto principal continua aqui normalmente.

## Subfigures (Figuras Múltiplas)

Agrupe imagens relacionadas usando um grid dentro de uma figure:

:::{figure}
:label: fig-antes
![](https://dummyimage.com/300x200/E74C3C/ffffff&text=Antes)

Antes
:::

:::{figure}
:label: fig-depois
![](https://dummyimage.com/300x200/27AE60/ffffff&text=Depois)

Depois
:::

Referência: Veja as Figuras {numref}`fig-antes` e {numref}`fig-depois`.

## Epígrafes

Citações decorativas no início de capítulos:

:::{epigraph}
"A melhor maneira de prever o futuro é inventá-lo."

-- Alan Kay
:::

## Listas de Tarefas

- [x] Tarefa concluída
- [ ] Tarefa pendente
- [x] Outra concluída
- [ ] Mais uma pendente

## Definições

Termo 1
: Definição do primeiro termo com explicação detalhada.

Termo 2
: Definição do segundo termo.
: Pode ter múltiplas definições.

## Tabelas Avançadas

### Tabela com Alinhamento

| Esquerda | Centro | Direita |
|:---------|:------:|--------:|
| Texto    | Texto  | Texto   |
| Mais     | Mais   | Mais    |

### Tabela com Label

```{list-table} Comparação de Linguagens
:label: tab-linguagens
:header-rows: 1

* - Linguagem
  - Vantagens
  - Desvantagens
* - Python
  - Fácil aprendizado, grande ecossistema
  - Performance relativa
* - Rust
  - Segurança de memória, alta performance
  - Curva de aprendizado íngreme
* - JavaScript
  - Onipresente na web
  - Inconsistências de linguagem
```

Referência: Veja a Tabela {numref}`tab-linguagens`.

## Ícones e Emojis

Use emojis Unicode diretamente:

✅ Sucesso | ❌ Erro | ⚠️ Aviso | ℹ️ Info | 🚀 Deploy | 📊 Analytics | 🔧 Config

## Blocos de Código com Recursos

### Com Título e Numeração

```{code-block} python
:linenos:
:emphasize-lines: 2,4
:caption: exemplo.py
:name: code-exemplo-completo

def calcular(a, b):
    resultado = a + b  # linha destacada
    print(f"Resultado: {resultado}")
    return resultado  # linha destacada
```

Referência: Veja {numref}`code-exemplo-completo`.

## Layout Complexo Combinado

::::{grid} 2
:class: no-pdf

:::{card} Área 1
:::::{tab-set}

::::{tab-item} Código
```python
print("Tabs dentro de cards!")
```
::::

::::{tab-item} Diagrama
```{mermaid}
graph LR
    A --> B
```
::::

:::::
:::

:::{card} Área 2
:::{dropdown} Mais Info
:open:

Dropdown dentro de card!
:::
:::

::::

## Próximos Passos

Explore combinações criativas desses componentes para criar documentação visualmente impressionante e funcionalmente rica!

:::{seealso}
- [Diagramas](https://mystmd.org/guide/diagrams)
- [Dropdowns, Cards e Tabs](https://mystmd.org/guide/dropdowns-cards-and-tabs)
- [Figuras](https://mystmd.org/guide/figures)
:::
