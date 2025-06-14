# Use uma imagem Python oficial como base
FROM python:3.12-slim

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copiar requirements.txt
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o projeto
COPY . .

# Criar diretórios para arquivos estáticos e mídia (se não existirem)
RUN mkdir -p /app/staticfiles
RUN mkdir -p /app/media

# Definir permissões corretas para os diretórios
RUN chmod -R 755 /app/staticfiles
RUN chmod -R 755 /app/media

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expor a porta 8000
EXPOSE 8000