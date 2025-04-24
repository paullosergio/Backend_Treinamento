# Use uma imagem Python oficial como base
FROM python:3.12-slim

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && \
    rm -rf /var/lib/apt/lists/*

# Copiar requirements.txt
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install uvicorn
RUN pip install pydantic

# Copiar o projeto
COPY . .

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expor a porta 8000
EXPOSE 8000