---
title: Exportação e Templates
description: Como exportar documentos MyST para PDF, DOCX e outros formatos usando templates profissionais
---

# Exportação e Templates

MyST permite exportar seus documentos para diversos formatos profissionais usando templates.

## Formatos Disponíveis

### Exportação para PDF

MyST pode gerar PDFs de alta qualidade usando LaTeX ou Typst como backend:

```yaml
exports:
  - format: pdf
    template: arxiv_two_column
    output: exports/artigo.pdf
    
  - format: typst
    template: lapreprint-typst
    output: exports/artigo-typst.pdf
```

#### Templates Populares para PDF

**Templates Acadêmicos:**
- `springer` - Revistas Springer Nature
- `arxiv_two_column` - ArXiv preprint em duas colunas
- `plain_latex_book` - Livros em LaTeX
- `agu2019` - American Geophysical Union
- `volcanica` - Revista Volcanica

**Exemplo completo no frontmatter:**

```markdown
---
title: Meu Artigo Científico
short_title: Artigo MyST
authors:
  - name: João Silva
    affiliations: [aff1]
    corresponding: true
    email: joao@exemplo.com
    
affiliations:
  - id: aff1
    department: Departamento de Computação
    institution: Universidade Federal
    city: São Paulo
    state: SP
    country: Brasil
    
keywords:
  - MyST
  - Documentação
  - LaTeX

bibliography:
  - references.bib

exports:
  - format: pdf+tex
    template: springer
    output: exports/artigo-springer.pdf
    reference_style: mathphys
    formatting: twocolumn
    line_numbers: false
---
```

### Exportação para Word (DOCX)

MyST também suporta exportação para Microsoft Word:

```yaml
exports:
  - format: docx
    output: exports/documento.docx
```

## Uso de Templates

### 1. Templates Públicos

Liste templates disponíveis:

```bash
myst templates list --pdf
myst templates list --pdf --tag preprint
```

Use um template público configurando-o no **frontmatter** do arquivo:

```yaml
# No frontmatter do artigo.md
exports:
  - format: pdf
    template: springer  # Template é configurado AQUI, não na linha de comando
    output: exports/artigo.pdf
```

Depois execute:

```bash
# O template já está definido no frontmatter
myst build artigo.md --pdf
```

:::{note}
**IMPORTANTE:** O comando `myst build` **não aceita** `--template` como parâmetro CLI.
Templates devem ser sempre configurados no frontmatter via seção `exports`.
:::

### 2. Templates Locais

Crie seu próprio template LaTeX customizado:

```yaml
exports:
  - format: pdf
    template: ./meu-template  # Pasta com template.yml e template.tex
    output: exports/custom.pdf
```

### 3. Estrutura de um Template

Um template MyST consiste em:

**template.yml:**
```yaml
jtex: v1
title: Meu Template
description: Template customizado
version: 1.0.0
authors:
  - name: Autor do Template
license: MIT
tags:
  - paper
  - article

parts:
  - id: abstract
    required: true
    description: Resumo do artigo
  - id: acknowledgments
    required: false
    
options:
  - id: line_numbers
    type: boolean
    default: false
    description: Mostrar números de linha
  - id: formatting
    type: choice
    default: onecolumn
    choices: [onecolumn, twocolumn]
```

**template.tex:**
```latex
\documentclass[
  [#- if options.formatting == "twocolumn" -#]twocolumn[#- endif -#]
]{article}

[#- if options.line_numbers -#]
\usepackage{lineno}
\linenumbers
[#- endif -#]

\begin{document}

\title{[-doc.title-]}
\author{[-doc.authors | join(", ", "name")-]}

[#- if parts.abstract -#]
\begin{abstract}
[-parts.abstract-]
\end{abstract}
[#- endif -#]

[-CONTENT-]

[#- if parts.acknowledgments -#]
\section*{Agradecimentos}
[-parts.acknowledgments-]
[#- endif -#]

\end{document}
```

## Parts (Partes do Documento)

Parts são seções especiais que podem ser extraídas e posicionadas em locais específicos do template:

### Definindo Parts no Frontmatter

```markdown
---
title: Meu Artigo
abstract: |
  Este é o resumo do artigo que aparecerá
  em uma caixa especial no PDF.
---
```

### Definindo Parts como Blocos

Use a sintaxe de fence com metadados:

```markdown
+++ {"part": "abstract"}
Este é o resumo do artigo definido como um bloco separado.
Pode conter múltiplos parágrafos e **formatação**.
+++

+++ {"part": "acknowledgments"}
Agradecemos o suporte da agência de fomento XYZ.
+++
```

### Parts Comuns

- `abstract` - Resumo/Abstract
- `acknowledgments` - Agradecimentos
- `data_availability` - Disponibilidade de dados
- `declarations` - Declarações éticas
- `supplementary_information` - Material suplementar
- `appendix` - Apêndices

## Options (Opções de Template)

Options controlam aspectos visuais e estruturais:

### Template Springer - Opções Disponíveis

| Option | Type | Default | Descrição |
|--------|------|---------|-----------|
| `reference_style` | choice | default | Estilo bibliográfico: default, apa, aps, basic, chicago, nature, mathphys, vancouver |
| `formatting` | choice | onecolumn | Layout: onecolumn, twocolumn |
| `line_numbers` | boolean | false | Números de linha na margem |
| `referee` | boolean | false | Espaçamento duplo para revisão |
| `pdf_latex` | boolean | true | Compilar com pdflatex/xelatex |
| `numbered_referencing` | boolean | false | Referências numeradas |
| `unnumbered_headings` | boolean | false | Títulos sem numeração |
| `theorem_style` | choice | one | Estilo de teoremas: none, one, two, three |

### Exemplo de Uso de Options

```yaml
exports:
  - format: pdf+tex
    template: springer
    output: exports/artigo.pdf
    # Options específicas do template:
    reference_style: mathphys
    formatting: twocolumn
    line_numbers: true
    theorem_style: one
```

## Comandos Úteis

### Build Local

```bash
# Build para HTML
myst build --html

# Build para PDF (template configurado no frontmatter)
myst build artigo.md --pdf

# Build todos os exports configurados no arquivo
myst build artigo.md

# Build todo o projeto
myst build
```

### Listar Templates

```bash
# Ver todos templates PDF
myst templates list --pdf

# Buscar templates por tag
myst templates list --pdf --tag journal

# Ver detalhes de um template
myst templates list springer --tex
```

### Criar Template Customizado

```bash
# Validar template local
jtex check ./meu-template

# Auto-detectar pacotes
jtex check --fix
```

## Multi-Article Exports

Para combinar múltiplos documentos em um único PDF (livros, teses):

```yaml
exports:
  - format: pdf
    template: plain_latex_book
    output: exports/minha-tese.pdf
    articles:
      - introducao.md
      - capitulo1.md
      - capitulo2.md
      - conclusao.md
```

Ou usando TOC file:

```yaml
exports:
  - format: pdf
    template: plain_latex_book
    output: exports/livro.pdf
    toc: _toc.yml
```

## Exclusão de Conteúdo

Para excluir conteúdo de exports específicos, use tags:

````markdown
```{code-cell}
:tags: [no-pdf]

# Este código não aparecerá no PDF
print("Apenas no HTML")
```
````

Tags disponíveis:
- `no-tex` - Exclui de PDFs LaTeX
- `no-typst` - Exclui de PDFs Typst  
- `no-pdf` - Exclui de todos PDFs

## Conteúdo Específico de Export

Para incluir conteúdo apenas em certos exports:

````markdown
```{raw} latex
\newpage
```

```{raw} typst
#pagebreak()
```
````

## Próximos Passos

- [Referências e Citações](./07-referencias.md) - Como gerenciar bibliografia
- [Plugins e Extensões](./08-plugins.md) - Estender funcionalidades do MyST
- [MyST Documentation](https://mystmd.org/guide/creating-pdf-documents) - Documentação oficial
