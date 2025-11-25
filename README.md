# Caderno Parahyba

[![MyST](https://img.shields.io/badge/MyST-1.6.6+-orange)](https://mystmd.org)
[![Python](https://img.shields.io/badge/Python-3.12+-blue)](https://python.org)
[![uv](https://img.shields.io/badge/uv-package%20manager-green)](https://docs.astral.sh/uv/)

Ferramentas e documentação técnica de classe mundial construída com MyST Markdown.

## 🎯 Visão Geral

O **Caderno Parahyba** é um projeto de documentação moderna que utiliza [MyST Markdown](https://mystmd.org) para criar livros e documentação técnica interativa. O projeto demonstra as capacidades completas do MyST, incluindo:

- 📚 **Documentação Organizada**: Livros estruturados semanticamente em `books/`
- 🔬 **Conteúdo Científico**: Equações matemáticas, citações, referências cruzadas e figuras
- 🎨 **Componentes Visuais**: Cards, grids, tabs, diagramas Mermaid e layouts responsivos
- 🚀 **Notebooks Interativos**: Integração completa com Jupyter, execução in-page (Thebe/Pyodide)
- 📤 **Exportação Flexível**: HTML estático, JATS XML
- ⚡ **Gestão Moderna**: `uv` para gerenciamento rápido de dependências Python
- 🛠️ **CLI Integrada**: Ferramenta de linha de comando para build, dev server e qualidade de código

## 📁 Estrutura do Projeto

```
caderno/
├── .github/
│   └── instructions/             # Instruções para AI agents
│       ├── uv.instructions.md    # Uso do UV
│       └── ___.instructions.md   # Regras gerais
├── books/                        # Diretório raiz do MyST
│   ├── myst.yml                  # Configuração do projeto MyST
│   ├── index.md                  # Landing page principal
│   └── guia-myst/                # Guia MyST Moderno
│       ├── index.md              # Introdução do guia
│       ├── 01-fundamentos.md     # Sintaxe básica
│       ├── 02-notebooks-intro.ipynb
│       ├── 03-notebooks-build.ipynb
│       ├── 03-notebooks-client.ipynb
│       ├── 04-visualizacao.md    # Gráficos e diagramas
│       ├── 05-componentes-ui.md  # Cards, grids, tabs
│       ├── 06-cientifico.md      # Teoremas, provas
│       ├── 07-referencias.md     # Bibliografia
│       ├── 08-plugins.md         # Extensões
│       ├── qrcode.mjs            # Plugin JS customizado
│       └── references.bib        # BibTeX
├── _build/                       # Diretório de build (auto-gerado)
├── cli.py                        # CLI customizada (Typer)
├── pyproject.toml                # Dependências Python (uv)
└── README.md                     # Este arquivo
```

## 🚀 Início Rápido

### Pré-requisitos

- **Python 3.12+**: [Download](https://python.org)
- **uv**: Gerenciador de pacotes Python rápido
  ```powershell
  # Windows
  pip install uv
  
  # Ou com pipx
  pipx install uv
  ```

### Instalação

```powershell
# Clonar repositório
git clone <repository-url>
cd caderno

# Instalar todas as dependências (prod + dev)
uv sync
```

### Desenvolvimento

#### Usando a CLI customizada (recomendado)

```powershell
# Iniciar servidor de desenvolvimento (hot-reload)
uv run python cli.py start

# Build completo
uv run python cli.py build

# Build HTML estático
uv run python cli.py build --html

# Build com execução de notebooks
uv run python cli.py build --execute

# Verificar qualidade do código
uv run python cli.py check

# Formatar código
uv run python cli.py format

# Limpar builds
uv run python cli.py clean

# Ver informações do ambiente
uv run python cli.py info
```

#### Usando comandos MyST diretos

```powershell
# Entrar no diretório books
cd books

# Iniciar servidor
uv run myst start

# Build
uv run myst build --html
```

**Acesse:**
- Site principal: http://localhost:3000
- Guia MyST: http://localhost:3000/guia-myst

O servidor suporta **hot-reload** - edições são refletidas automaticamente no navegador.

## 🐳 Build com Docker

Para quem prefere usar Docker (com Typst incluído):

```powershell
# Build da imagem
docker compose build

# Executar build do exemplo-springer.md com Typst
docker compose run --rm myst-build

# Output estará em books/guia-myst/exports/
```

**Alvo do build:** `books/guia-myst/exemplo-springer.md` → `exports/artigo-typst.pdf`

O container inclui:
- Python 3.12 + uv (gerenciador de pacotes)
- Node.js (runtime MyST)
- Typst (compilador de documentos)
- Todas as dependências Python do projeto

## 📚 Conteúdo Disponível

### 🏠 Landing Page
Página inicial moderna com cards, grids e navegação para os livros do projeto.

### 📘 Guia MyST Moderno

Um guia completo e prático sobre MyST Markdown:

1. **01-fundamentos.md** - Diretivas, matemática, código, admonições
2. **02-notebooks-intro.ipynb** - Introdução a notebooks executáveis
3. **03-notebooks-build.ipynb** - Notebooks com build-time execution
4. **03-notebooks-client.ipynb** - Notebooks com client-side execution (Thebe)
5. **04-visualizacao.md** - Matplotlib, Plotly, Altair, Mermaid
6. **05-componentes-ui.md** - Cards, grids, tabs, dropdowns
7. **06-cientifico.md** - Teoremas, provas, algoritmos
8. **07-referencias.md** - Bibliografia e citações (BibTeX)
9. **08-plugins.md** - JavaScript plugins, executable plugins

**Recursos incluídos:**
- Plugin JavaScript customizado (`qrcode.mjs`)
- Bibliografia gerenciada (`references.bib`)
- Exemplos de visualização com múltiplas bibliotecas
- Demonstrações de componentes UI modernos

## 🛠️ Tecnologias

| Ferramenta | Versão | Propósito |
|------------|--------|-----------|
| **MyST Markdown** | ≥1.6.6 | Sistema de autoria científica extensível |
| **Python** | ≥3.12 | Ambiente de execução |
| **uv** | Latest | Gerenciador de pacotes Python ultra-rápido |
| **Jupyter** | ≥1.0.0 | Notebooks interativos |
| **Ruff** | ≥0.14.6 | Linter e formatter Python |
| **Pyrefly** | ≥0.42.2 | Type checker Python |
| **Typer** | ≥0.20.0 | Framework para CLI |
| **Rich** | ≥14.2.0 | Output colorido no terminal |

### Bibliotecas de Visualização

- **Matplotlib** ≥3.8.0 - Gráficos científicos clássicos
- **Plotly** ≥5.18.0 - Gráficos interativos
- **Altair** ≥5.0.0 - Gramática de gráficos declarativa
- **NumPy** ≥1.26.0 - Computação numérica
- **Pandas** ≥2.2.0 - Análise de dados
- **SciPy** ≥1.12.0 - Computação científica

## 📖 Comandos Essenciais

### CLI Customizada (Recomendada)

```powershell
# Desenvolvimento
uv run python cli.py start           # Servidor com hot-reload
uv run python cli.py build           # Build padrão
uv run python cli.py build --html    # Build HTML estático
uv run python cli.py build --execute # Build com execução de notebooks
uv run python cli.py clean           # Limpar builds

# Qualidade de Código
uv run python cli.py check           # Verificar com Ruff + Pyrefly
uv run python cli.py check --fix     # Verificar e corrigir
uv run python cli.py format          # Formatar código
uv run python cli.py format --check  # Apenas verificar formatação

# Informações
uv run python cli.py info            # Versões do ambiente
uv run python cli.py --help          # Ajuda completa
```

### Comandos MyST Diretos

```powershell
cd books                             # Entrar no diretório MyST

# Desenvolvimento
uv run myst start                    # Servidor com hot-reload
uv run myst build --html             # Build HTML
uv run myst build --all              # Build todos exports
uv run myst clean                    # Limpar builds

# Validação
uv run myst build --check-links      # Verificar links quebrados
uv run myst build --strict           # Build com erro em warnings
```

### Gerenciamento de Dependências

```powershell
# Instalação
uv sync                              # Instalar todas dependências
uv sync --group dev                  # Instalar apenas dev
uv sync --no-dev                     # Instalar apenas produção

# Atualização
uv sync --upgrade                    # Atualizar todas
uv add mystmd --upgrade              # Atualizar MyST
uv add numpy --upgrade               # Atualizar pacote específico

# Adição de pacotes
uv add matplotlib                    # Adicionar produção
uv add --group dev pytest            # Adicionar dev
```

## 🎨 Personalização

### Adicionar Novo Livro

1. Criar estrutura do livro:
   ```powershell
   mkdir books/meu-livro
   cd books/meu-livro
   ```

2. Criar `index.md`:
   ```markdown
   ---
   title: Meu Livro
   ---
   
   # Conteúdo do Livro
   ```

3. Adicionar ao `books/myst.yml`:
   ```yaml
   project:
     toc:
       - file: index.md
       - file: meu-livro/index.md
         title: "Meu Livro"
         children:
           - file: meu-livro/capitulo1.md
   ```

### Configurar Exportações

No frontmatter de qualquer documento ou no `books/myst.yml`:

```yaml
project:
  exports:
    - format: html
      output: exports/documento.html
    - format: jats
      output: exports/documento.jats.xml
    - format: typst
      template: lapreprint-typst
      output: exports/documento.pdf
```

**Exemplo completo:** Veja `books/guia-myst/exemplo-springer.md` com 5 formatos de exportação configurados (PDF via Typst, LaTeX, Word, etc.)

### Personalizar Tema

No `books/myst.yml`:

```yaml
site:
  template: book-theme  # ou article-theme
  options:
    logo: ./logo.png
    logo_text: "Meu Projeto"
    hide_toc: false
    hide_outline: false
```

## 🐛 Solução de Problemas

### Servidor não inicia

```powershell
# Limpar builds e cache
uv run python cli.py clean

# Verificar se a porta 3000 está livre
# Se estiver em uso, o MyST usará outra porta automaticamente
```

### Links quebrados

- Use paths relativos: `./capitulo.md` 
- Ou use cross-references com labels: `[texto](#label)`
- Verifique com: `cd books; uv run myst build --check-links`

### Build lento

```powershell
# Limpar cache completo
cd books
uv run myst clean --all

# Build incremental sem execução
uv run python cli.py build --html
```

### Notebooks não executam

```powershell
# Verificar kernel instalado
uv run jupyter kernelspec list

# Instalar/reinstalar kernel
uv sync

# Executar notebooks explicitamente
uv run python cli.py build --execute
```

### Erros de importação Python

```powershell
# Verificar ambiente
uv run python cli.py info

# Reinstalar dependências
uv sync --reinstall
```

### Plugin JavaScript não carrega

- Verifique o path em `myst.yml`: `plugins: ["./plugin.mjs"]`
- Plugin deve exportar: `export const plugin = { name: "...", ... }`
- Console do navegador mostra erros de plugins

## 🏗️ Arquitetura do Projeto

### Fluxo de Trabalho

```
┌─────────────────┐
│  Markdown (.md) │
│  Notebooks (.ipynb) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   MyST Parser   │ ← books/myst.yml (config)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  AST + Plugins  │ ← qrcode.mjs (custom plugin)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Render Engine  │
└────────┬────────┘
         │
         ├─→ HTML (books/_build/html/)
         ├─→ JATS XML
         └─→ PDF (via LaTeX)
```

### Diretórios Importantes

- `books/` - **Raiz do projeto MyST** (executar comandos aqui)
- `books/_build/` - Output compilado (não versionar)
- `books/guia-myst/` - Conteúdo do guia
- `.github/instructions/` - Regras para AI agents
- `cli.py` - CLI customizada com Typer

### Configuração em Camadas

1. **Global**: `books/myst.yml` - Configuração do projeto inteiro
2. **Frontmatter**: Metadados por documento (YAML no topo do arquivo)
3. **CLI**: Flags de build e execução

## 🎓 Recursos de Aprendizado

### Documentação Oficial

- **MyST Guide**: https://mystmd.org/guide
- **MyST Sandbox**: https://mystmd.org/sandbox (teste online)
- **uv Docs**: https://docs.astral.sh/uv/
- **Jupyter Book**: https://jupyterbook.org/

### Exemplos e Templates

- **MyST Templates**: https://github.com/myst-templates
- **Made with MyST**: https://mystmd.org/made-with-myst
- **Executable Books Gallery**: https://executablebooks.org/en/latest/gallery/

### Comunidade

- **Discord MyST**: https://discord.mystmd.org
- **GitHub Discussions**: https://github.com/jupyter-book/mystmd/discussions

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch: `git checkout -b feature/nova-feature`
3. Commit suas mudanças: `git commit -am 'Adiciona nova feature'`
4. Push para a branch: `git push origin feature/nova-feature`
5. Abra um Pull Request

### Diretrizes

- Siga as instruções em `.github/instructions/`
- Use `uv run python cli.py check` antes de commitar
- Formate código com `uv run python cli.py format`
- Teste localmente com `uv run python cli.py start`

## 📄 Licença

- **Conteúdo**: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- **Código**: MIT

## 📚 Recursos

- **MyST Guide**: https://mystmd.org/guide
- **uv Docs**: https://docs.astral.sh/uv/
- **MyST Sandbox**: https://mystmd.org/sandbox
- **Thebe Docs**: https://thebe.readthedocs.io/

---

**Criado com ❤️ usando [MyST Markdown](https://mystmd.org)** | [Documentação](https://mystmd.org) | [GitHub](https://github.com/parahyba-com/caderno)
