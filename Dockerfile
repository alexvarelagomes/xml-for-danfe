# Dockerfile
FROM python:3.13-slim AS builder

# Copia o binário oficial do uv diretamente da imagem da Astral
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Otimizações de performance para o uv dentro de contêineres
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Copia apenas os arquivos de controle de dependências para aproveitar o cache do Docker
COPY pyproject.toml uv.lock ./

# Instala as dependências no ambiente virtual (.venv)
# --frozen: Garante builds determinísticos falhando se o uv.lock estiver desatualizado
# --no-dev: Não instala pacotes de desenvolvimento no ambiente de produção
# --no-install-project: Instala apenas as bibliotecas listadas.
RUN uv sync --frozen --no-dev --no-install-project

# Copia o restante do código da aplicação
COPY . .

# Sincroniza novamente para registrar o projeto principal no .venv
RUN uv sync --frozen --no-dev

# Imagem para rodar a aplicação.
FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv

# Isso dispensa ativação manual; qualquer chamada a "python" ou "streamlit" usará o .venv
ENV PATH="/app/.venv/bin:$PATH"

# Copia o código-fonte da aplicação
COPY . .

# Expõe a porta padrão utilizada pelo Streamlit
EXPOSE 8501

# Comando de execução do contêiner mantendo as flags úteis
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]