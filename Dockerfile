FROM python:3.13-slim

# Injeta temporariamente o binário oficial do UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Garante que os pacotes sejam copiados de forma independente e define o PATH
ENV UV_LINK_MODE=copy
ENV UV_COMPILE_BYTECODE=1
ENV PATH="/app/.venv/bin:$PATH"

# Copia apenas os arquivos de manifesto para aproveitar o cache de camadas
COPY pyproject.toml uv.lock ./

# Instala as dependências de produção e destrói o cache de downloads na mesma camada
RUN uv sync --frozen --no-dev --no-install-project \
    && rm -rf /root/.cache/uv

# Copia o código-fonte da aplicação
COPY . .

# Sincroniza o pacote final e remove os binários do instalador para enxugar a imagem
RUN uv sync --frozen --no-dev \
    && rm -f /bin/uv /bin/uvx

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]