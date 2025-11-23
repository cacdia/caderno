---
title: Plugins e Extensões
description: Como criar e usar plugins MyST para estender funcionalidades
keywords: [plugins, javascript, executable, myst-ext, extensões]
---

# Plugins e Extensões

O MyST possui um sistema de plugins poderoso que permite estender suas funcionalidades com diretivas, roles e transformações personalizadas.

## Tipos de Plugins

### JavaScript Plugins

Plugins JavaScript (`.mjs`) são a forma mais comum de estender o MyST. Eles podem adicionar:

- **Diretivas**: Novos blocos de conteúdo estruturado
- **Roles**: Marcação inline customizada
- **Transforms**: Modificações na árvore AST (Abstract Syntax Tree)

#### Exemplo de Plugin JavaScript

Crie um arquivo `meu-plugin.mjs`:

```javascript
export const directives = [
  {
    name: 'minha-diretiva',
    arg: { type: String, required: false },
    options: {
      classe: { type: String }
    },
    run(data, vfile) {
      return [
        {
          type: 'container',
          class: data.options.classe || 'default',
          children: data.body
        }
      ];
    }
  }
];

export const roles = [
  {
    name: 'destaque',
    body: { type: String, required: true },
    run(data) {
      return [
        {
          type: 'emphasis',
          children: [{ type: 'text', value: data.body }]
        }
      ];
    }
  }
];
```

#### Configurar Plugin no `myst.yml`

```yaml
project:
  plugins:
    - ./meu-plugin.mjs
```

### Executable Plugins

Plugins executáveis podem ser escritos em qualquer linguagem (Python, Rust, Go, etc.) e se comunicam via stdin/stdout.

#### Exemplo de Plugin Python

Crie `meu_plugin.py`:

```python
#!/usr/bin/env python3
import sys
import json

def process_directive(data):
    """Processa uma diretiva customizada"""
    return {
        "type": "container",
        "class": "python-generated",
        "children": data.get("body", [])
    }

if __name__ == "__main__":
    for line in sys.stdin:
        request = json.loads(line)
        response = process_directive(request)
        print(json.dumps(response))
        sys.stdout.flush()
```

#### Configurar Plugin Executável

```yaml
project:
  plugins:
    - directives:
        - name: python-directive
          executable: python
          args: [./meu_plugin.py]
```

## Plugins Oficiais

O MyST vem com extensões oficiais que podem ser habilitadas:

### myst-ext-card

Cards visuais para organizar conteúdo:

:::{card} Título do Card
:link: https://mystmd.org
:footer: Rodapé opcional

Conteúdo do card com **markdown**.
:::

### myst-ext-grid

Layouts em grid responsivos:

::::{grid} 2

:::{card} Card 1
Conteúdo do primeiro card
:::

:::{card} Card 2
Conteúdo do segundo card
:::
::::

### myst-ext-tabs

Conteúdo em abas:

::::{tab-set}

:::{tab-item} Python
```python
print("Hello, World!")
```
:::

:::{tab-item} JavaScript
```javascript
console.log("Hello, World!");
```
:::

::::

## Distribuindo Plugins

### Via npm Package

Para distribuir plugins JavaScript:

1. Crie `package.json`:

```json
{
  "name": "myst-plugin-exemplo",
  "version": "1.0.0",
  "type": "module",
  "main": "index.mjs",
  "exports": {
    ".": "./index.mjs"
  }
}
```

2. Publique no npm:

```bash
npm publish
```

3. Use no projeto:

```yaml
project:
  plugins:
    - myst-plugin-exemplo
```

### Via URL

Plugins podem ser carregados diretamente de URLs:

```yaml
project:
  plugins:
    - https://example.com/meu-plugin.mjs
```

## Exemplos Práticos

### Plugin de Alerta Customizado

```javascript
// alert-plugin.mjs
export const directives = [
  {
    name: 'alert',
    arg: { type: String, required: true }, // tipo: success, info, warning, danger
    run(data) {
      const type = data.arg;
      const emoji = {
        success: '✅',
        info: 'ℹ️',
        warning: '⚠️',
        danger: '🚨'
      }[type] || '📢';
      
      return [
        {
          type: 'admonition',
          kind: type,
          children: [
            { type: 'admonitionTitle', children: [{ type: 'text', value: emoji }] },
            ...data.body
          ]
        }
      ];
    }
  }
];
```

Uso no markdown:

```markdown
:::{alert} success
Operação concluída com sucesso!
:::

:::{alert} danger
Erro crítico detectado!
:::

### Exemplo: Plugin QR Code

Este exemplo demonstra como usar o plugin `qrcode.mjs` para gerar QR Codes dinamicamente.

```markdown
:::{qr} https://mystmd.org
:size: 200
:color: 2563eb
:::
```

Resultado:

:::{qr} https://mystmd.org
:size: 200
:color: 2563eb
:::

### Plugin de Citação Bibliográfica

```javascript
// cite-plugin.mjs
export const roles = [
  {
    name: 'cite',
    body: { type: String, required: true },
    run(data) {
      const [author, year] = data.body.split(',').map(s => s.trim());
      return [
        {
          type: 'link',
          url: `#ref-${author.toLowerCase()}${year}`,
          children: [
            { type: 'text', value: `${author} (${year})` }
          ]
        }
      ];
    }
  }
];
```

Uso: `Segundo {cite}`Smith, 2023`, a metodologia...`

## Debugging de Plugins

### Logs e Mensagens

Use o objeto `vfile` para emitir mensagens:

```javascript
run(data, vfile) {
  vfile.message('Processando diretiva customizada');
  vfile.info('Info adicional');
  vfile.warn('Aviso de deprecation');
  
  if (problemaCritico) {
    vfile.fail('Erro crítico encontrado');
  }
  
  return [...];
}
```

### Testar Localmente

Execute o MyST em modo verbose:

```bash
uv run myst build --verbose
```

## Recursos Avançados

### Transforms AST

Modifique a árvore de nós após parsing:

```javascript
export const transforms = [
  {
    name: 'meu-transform',
    stage: 'document', // ou 'project'
    plugin: (tree, vfile) => {
      visit(tree, 'paragraph', (node) => {
        // Modificar nós de parágrafo
        node.class = 'modified-paragraph';
      });
    }
  }
];
```

### Plugins com Dependências

Use imports ES6 normalmente:

```javascript
import { visit } from 'unist-util-visit';
import { h } from 'hastscript';

export const directives = [
  {
    name: 'custom',
    run(data, vfile) {
      const ast = processWithDependencies(data.body);
      return ast;
    }
  }
];
```

## Próximos Passos

- Explore [plugins oficiais](https://github.com/executablebooks/myst-theme)
- Aprenda sobre [AST nodes](https://mystmd.org/guide/directives)
- Veja exemplos em [myst-templates](https://github.com/myst-templates)

:::{seealso}
Consulte a [documentação oficial de plugins](https://mystmd.org/guide/plugins) para referência completa.
:::
