# Use Python 3.11 slim image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Set work directory
WORKDIR /app

# Instalação de dependências de sistema
# Inclui: build-essential (compilação), libpq-dev (PostgreSQL),
# libs para Pillow (libjpeg, zlib) e libs para Criptografia/SSL (libssl-dev, libffi-dev).
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        libpq-dev \
        gettext \
        curl \
        libjpeg-dev \
        zlib1g-dev \
        libfreetype6-dev \
        libssl-dev \
        libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalação das dependências Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o projeto
COPY . /app/

# Criação de diretórios para arquivos estáticos e de mídia
RUN mkdir -p /app/staticfiles /app/media /app/logs /app/logs

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput --clear

# Criar usuário não-root
RUN adduser --disabled-password --gecos '' appuser \
    && chown -R appuser:appuser /app
USER appuser

# Expor porta
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health/ || exit 1

# Rodar a aplicação (Gunicorn)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120", "core.wsgi:application"]


