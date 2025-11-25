# Multi-stage build otimizado com Debian
FROM python:3.12-slim-bookworm AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar apenas dependências necessárias
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    mv /root/.local/bin/uv /usr/local/bin/uv && \
    mv /root/.local/bin/uvx /usr/local/bin/uvx

# Copiar arquivos de dependências
COPY pyproject.toml uv.lock* ./

# Instalar dependências sem o projeto
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project --no-dev

# Copiar código fonte
COPY . .

# Instalar projeto
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-editable --no-dev

# Imagem final com Typst + Node.js + Python
FROM python:3.12-slim-bookworm

# Instalar Node.js (via NodeSource ou nvm para melhor compatibilidade)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    xz-utils \
    && curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

# Instalar Typst
RUN curl -fsSL https://github.com/typst/typst/releases/latest/download/typst-x86_64-unknown-linux-musl.tar.xz \
    | tar -xJ -C /usr/local/bin --strip-components=1

# Copiar ambiente virtual do Python
COPY --from=builder /app/.venv /app/.venv

ENV PATH="/app/.venv/bin:${PATH}" \
    PYTHONUNBUFFERED=1

# Configurar Jupyter para permitir execução como root
RUN jupyter server --generate-config && \
    echo "c.ServerApp.allow_root = True" >> /root/.jupyter/jupyter_server_config.py

WORKDIR /workspace

CMD ["myst", "build", "--execute", "--html", "--typst"]