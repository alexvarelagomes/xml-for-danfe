# --- Estágio de Build: Instala as dependências ---
FROM python:3.12-slim AS builder

WORKDIR /app

# Copia o arquivo requirements.txt primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instala as dependências do requirements.txt
# Garante que o pip esteja atualizado e instala todas as libs
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# --- Estágio Final: Imagem de Produção Otimizada ---
FROM python:3.12-slim

WORKDIR /app

# Copia o ambiente virtual inteiro (ou site-packages e binários) do estágio de build
# Esta é a parte crucial para garantir que Streamlit e outros executáveis estejam no PATH
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Se você tem arquivos de cache ou outras coisas do pip que podem não estar
# no /usr/local/bin ou /usr/local/lib/pythonX.Y/site-packages,
# mas são necessárias para a execução, você pode tentar copiar o venv inteiro:
# COPY --from=builder /usr/local /usr/local

# Copia sua aplicação Streamlit para o container
# Certifique-se de que sua aplicação está no mesmo diretório do Dockerfile
COPY . .

# Expõe a porta padrão do Streamlit
EXPOSE 8501

# Comando para rodar a aplicação Streamlit
# Ajuste 'your_app.py' para o nome do seu arquivo principal do Streamlit
# O --server.enableCORS=false e --server.enableXsrfProtection=false são úteis para dev
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
