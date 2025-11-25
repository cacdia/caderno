---
title: Análise Computacional de Algoritmos de Ordenação
short_title: Algoritmos de Ordenação
authors:
  - name:
      given: Maria
      surname: Silva
    affiliations: [usp]
    corresponding: true
    email: maria.silva@usp.br
  - name:
      given: João
      surname: Santos
    affiliations: [usp, unicamp]
    email: joao.santos@unicamp.br

affiliations:
  - id: usp
    name: Universidade de São Paulo
    department: Instituto de Matemática e Estatística
    address: Rua do Matão, 1010
    city: São Paulo
    state: SP
    postal_code: 05508-090
    country: Brasil
  - id: unicamp
    name: Universidade Estadual de Campinas
    department: Instituto de Computação
    city: Campinas
    state: SP
    country: Brasil

keywords:
  - algoritmos
  - complexidade computacional
  - ordenação
  - análise de desempenho

bibliography:
  - references.bib

# Configuração de exports para diferentes formatos
exports:
  # Export 1: PDF estilo Springer (duas colunas, estilo matemático)
  # - format: pdf+tex
  #   template: springer
  #   output: exports/artigo-springer.pdf
  #   reference_style: mathphys
  #   formatting: twocolumn
  #   line_numbers: false
  #   numbered_referencing: true
  #   unnumbered_headings: false
  #   theorem_style: one
    
  # Export 2: PDF estilo ArXiv (preprint)
  #- format: tex
  #  template: arxiv_two_column
  #  output: exports/preprint-arxiv.tex
    
  # Export 3: Word para colaboração
  #- format: docx
  #  output: exports/rascunho.docx
    
  # Export 4: LaTeX fonte (para submissão)
  # - format: tex
  #   template: springer
  #   output: exports/source-latex/
    
  # Export 5: PDF com Typst (alternativa moderna ao LaTeX)
  - format: typst
    template: lapreprint-typst
    output: exports/artigo-typst.pdf
---

+++ {"part": "abstract"}
Este artigo apresenta uma análise comparativa rigorosa de algoritmos clássicos de ordenação,
incluindo QuickSort, MergeSort e HeapSort. Através de experimentos computacionais sistemáticos,
avaliamos o desempenho destes algoritmos em diferentes cenários: dados aleatórios, parcialmente
ordenados e ordenados inversamente. Os resultados demonstram que o QuickSort apresenta o melhor
desempenho médio em conjuntos aleatórios, enquanto o MergeSort mantém estabilidade superior
em todos os cenários. Propomos também uma variação híbrida que combina as vantagens de ambos
os algoritmos.
+++

# Introdução

Algoritmos de ordenação constituem um dos tópicos fundamentais em ciência da computação
{cite:p}`knuth1998art`. A escolha adequada do algoritmo pode impactar significativamente
o desempenho de sistemas computacionais.

## Motivação

A ordenação é uma operação frequente em sistemas de banco de dados, análise de dados
e processamento de informações {cite:p}`cormen2009introduction`.

## Objetivos

Este trabalho visa:

1. Comparar algoritmos clássicos de ordenação
2. Avaliar desempenho em cenários diversos
3. Propor otimizações baseadas em análise empírica

# Fundamentação Teórica

## Complexidade Computacional

:::{note}
A complexidade de tempo é medida em notação Big-O, representando o crescimento
assintótico do tempo de execução em função do tamanho da entrada.
:::

### Definição

::::{prf:definition} Notação Big-O
:label: def-bigo

Dizemos que $f(n) = O(g(n))$ se existem constantes $c > 0$ e $n_0 > 0$ tais que:

$$
f(n) \leq c \cdot g(n), \quad \forall n \geq n_0
$$
::::

## Algoritmos Analisados

### QuickSort

O QuickSort é um algoritmo de divisão e conquista com complexidade média $O(n \log n)$.

::::{prf:theorem} Complexidade Média do QuickSort
:label: thm-quicksort

Seja $T(n)$ o número esperado de comparações do QuickSort para ordenar $n$ elementos
distintos e aleatórios. Então:

$$
T(n) = 2(n+1)H_n - 4n \approx 1.39n \log n
$$

onde $H_n = \sum_{i=1}^{n} \frac{1}{i}$ é o $n$-ésimo número harmônico.
::::

### MergeSort

O MergeSort garante complexidade $O(n \log n)$ no pior caso, com estabilidade.

### HeapSort

O HeapSort utiliza uma estrutura de heap binária, garantindo $O(n \log n)$ no pior caso.

# Metodologia

## Implementação

```{code-cell} python
:tags: [hide-output]

import numpy as np
import time
from typing import List, Callable

def quicksort(arr: List[int]) -> List[int]:
    """Implementação do QuickSort."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def mergesort(arr: List[int]) -> List[int]:
    """Implementação do MergeSort."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    """Combina duas listas ordenadas."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print("Algoritmos implementados com sucesso!")
```

## Cenários de Teste

Avaliamos os algoritmos em três cenários:

1. **Aleatório**: Dados gerados com distribuição uniforme
2. **Parcialmente Ordenado**: 80% dos dados em ordem crescente
3. **Inversamente Ordenado**: Dados em ordem decrescente

```{code-cell} python
def gerar_dados_aleatorios(n: int) -> List[int]:
    """Gera lista aleatória de n elementos."""
    return list(np.random.randint(0, 10000, n))

def gerar_dados_parcialmente_ordenados(n: int) -> List[int]:
    """Gera lista 80% ordenada."""
    arr = sorted(gerar_dados_aleatorios(n))
    indices = np.random.choice(n, size=int(0.2*n), replace=False)
    for i in indices:
        arr[i] = np.random.randint(0, 10000)
    return arr

def gerar_dados_invertidos(n: int) -> List[int]:
    """Gera lista em ordem decrescente."""
    return sorted(gerar_dados_aleatorios(n), reverse=True)
```

# Resultados

## Análise de Desempenho

```{code-cell} python
:tags: [hide-input]

import pandas as pd
import matplotlib.pyplot as plt

# Executar testes
tamanhos = [1000, 5000, 10000, 20000]
resultados = []

for n in tamanhos:
    dados = gerar_dados_aleatorios(n)
    
    # QuickSort
    start = time.time()
    _ = quicksort(dados.copy())
    tempo_quick = time.time() - start
    
    # MergeSort
    start = time.time()
    _ = mergesort(dados.copy())
    tempo_merge = time.time() - start
    
    resultados.append({
        'Tamanho': n,
        'QuickSort': tempo_quick,
        'MergeSort': tempo_merge
    })

df = pd.DataFrame(resultados)
print("Tempos de execução (segundos):")
print(df.to_string(index=False))
```

```{code-cell} python
:tags: [hide-input]
:label: fig-desempenho
:caption: Comparação de desempenho dos algoritmos em dados aleatórios. Observe que ambos crescem de forma aproximadamente logarítmica, confirmando a complexidade teórica esperada.

plt.figure(figsize=(10, 6))
plt.plot(df['Tamanho'], df['QuickSort'], 'o-', label='QuickSort', linewidth=2)
plt.plot(df['Tamanho'], df['MergeSort'], 's-', label='MergeSort', linewidth=2)
plt.xlabel('Tamanho da entrada (n)', fontsize=12)
plt.ylabel('Tempo de execução (s)', fontsize=12)
plt.title('Comparação de Desempenho: QuickSort vs MergeSort', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

A {numref}`fig-desempenho` apresenta os resultados experimentais.

## Discussão dos Resultados

::::{admonition} Observações Importantes
:class: tip

1. **QuickSort**: Melhor desempenho em dados aleatórios (~15% mais rápido)
2. **MergeSort**: Comportamento mais previsível e estável
3. **Pivô**: A escolha do pivô no QuickSort impacta significativamente
::::

# Conclusão

Este estudo demonstrou empiricamente que:

1. O QuickSort apresenta melhor desempenho médio em dados aleatórios
2. O MergeSort garante estabilidade superior
3. A combinação híbrida pode otimizar ambos os aspectos

## Trabalhos Futuros

Pretendemos investigar:

- Algoritmos paralelos de ordenação
- Otimizações específicas para GPUs
- Ordenação externa para grandes volumes

+++ {"part": "acknowledgments"}
Agradecemos o apoio da FAPESP (Proc. 2024/00000-0) e CNPq (Proc. 123456/2024-0)
para a realização desta pesquisa. Agradecemos também aos revisores anônimos
cujos comentários melhoraram significativamente este trabalho.
+++

+++ {"part": "declarations"}
**Financiamento:** Esta pesquisa foi financiada pela FAPESP e CNPq.

**Conflito de interesses:** Os autores declaram não haver conflito de interesses.

**Disponibilidade de dados:** Os dados e código utilizados estão disponíveis em:
https://github.com/exemplo/algoritmos-ordenacao
+++

```{bibliography}
```
