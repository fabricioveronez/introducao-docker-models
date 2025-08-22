FROM python:3.11-slim

# Define variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV APP_HOME=/app

# Cria diretório de trabalho
WORKDIR $APP_HOME

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copia arquivo de requirements
COPY src/requirements.txt .

# Instala dependências Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia código da aplicação
COPY src/ ./src/

# Cria usuário não-root para segurança
RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app $APP_HOME
USER app

# Expõe porta do Streamlit
EXPOSE 8501

# Define diretório de trabalho para execução
WORKDIR $APP_HOME

# Comando padrão para executar Streamlit
CMD ["streamlit", "run", "src/app.py", "--server.address", "0.0.0.0", "--server.port", "8501", "--server.headless", "true"]