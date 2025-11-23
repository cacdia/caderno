---
title: Escrita Científica
description: Teoremas, provas, algoritmos e citações bibliográficas
keywords: [science, math, proofs, theorems, citations, bibliography]
---

# Escrita Científica Avançada

O MyST brilha na escrita científica, suportando nativamente estruturas complexas como teoremas, provas, algoritmos e citações.

## Teoremas e Provas

O MyST suporta ambientes de prova estruturados (semelhante ao `amsthm` do LaTeX).

### Teoremas

:::{prf:theorem} Teorema do Limite Central
:label: thm-clt

Seja $\{X_1, \ldots, X_n\}$ uma amostra aleatória de tamanho $n$ — isto é, uma sequência de variáveis aleatórias independentes e identicamente distribuídas (i.i.d.) extraídas de uma distribuição com média $\mu$ e variância finita $\sigma^2$. Suponha que estamos interessados na média da amostra:

$$
S_n := \frac{X_1 + \cdots + X_n}{n}
$$

Então, quando $n \to \infty$, a variável aleatória $\sqrt{n}(S_n - \mu)$ converge em distribuição para uma normal $\mathcal{N}(0, \sigma^2)$.
:::

### Provas

:::{prf:proof}
:label: proof-clt

A prova deste teorema é deixada como exercício para o leitor, mas geralmente envolve o uso de funções características.
:::

### Definições e Lemas

:::{prf:definition} Espaço de Hilbert
:label: def-hilbert

Um espaço de Hilbert é um espaço vetorial com produto interno que é completo em relação à norma induzida pelo produto interno.
:::

:::{prf:lemma} Desigualdade de Cauchy-Schwarz
:label: lemma-cs

Para todos os vetores $u$ e $v$ em um espaço com produto interno:

$$
|\langle u, v \rangle|^2 \leq \langle u, u \rangle \cdot \langle v, v \rangle
$$
:::

Podemos referenciar o {prf:ref}`thm-clt` e a {prf:ref}`def-hilbert` facilmente.

## Algoritmos

Você pode descrever algoritmos usando a diretiva `prf:algorithm`.

:::{prf:algorithm} Algoritmo de Euclides
:label: alg-euclides

**Entrada:** Dois inteiros positivos $a$ e $b$.
**Saída:** O maior divisor comum (MDC) de $a$ e $b$.

1. Enquanto $b \neq 0$:
    1. $t \leftarrow b$
    2. $b \leftarrow a \ (\text{mod}\ b)$
    3. $a \leftarrow t$
2. Retorne $a$
:::

Veja o {prf:ref}`alg-euclides` para calcular o MDC.

## Citações e Bibliografia

O MyST gerencia citações bibliográficas de forma robusta.

### Citando no Texto

Podemos citar trabalhos seminais como o artigo sobre NumPy {cite:p}`harris2020array` ou o livro de Data Science do VanderPlas {cite:t}`vanderplas2016python`.

O ecossistema Python científico foi descrito por Perez et al. {cite:p}`perez2011python`. Matplotlib é a biblioteca base para visualização {cite:p}`hunter2007matplotlib`.

### Lista de Referências

As referências são geradas automaticamente a partir do arquivo `.bib`.

:::{bibliography}
:::

## Matemática Avançada

### Equações Numeradas

$$
e^{i\pi} + 1 = 0
$$ (eq:euler)

A equação {eq}`eq:euler` é a identidade de Euler.

### Alinhamento de Equações

$$
\begin{aligned}
  f(x) &= (x+a)(x+b) \\
       &= x^2 + (a+b)x + ab
\end{aligned}
$$

### Matrizes

$$
\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{pmatrix}
$$

## Exercícios

:::{exercise} Cálculo de Derivada
:label: ex-derivada

Calcule a derivada de $f(x) = x^2 \sin(x)$.

:::{solution} ex-derivada
:class: dropdown

Usando a regra do produto:
$$
f'(x) = 2x \sin(x) + x^2 \cos(x)
$$
:::
:::

:::{exercise} Algebra Linear
:label: ex-algebra

Dada a matriz $\mathbf{A}$ acima, calcule seu determinante.

:::{solution} ex-algebra
:class: dropdown

$$
\det(\mathbf{A}) = a_{11}a_{22} - a_{12}a_{21}
$$
:::
:::

Responda ao {numref}`ex-derivada` e ao {numref}`ex-algebra`.
