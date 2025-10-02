# Imagem base com dependências comuns
FROM python:3.11-slim as base

# Configurações de ambiente comuns
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=off

WORKDIR /app

# Instalar dependências do sistema base
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    libssl-dev \
    libffi-dev \
    curl \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Criar diretórios necessários
RUN mkdir -p /app/staticfiles /app/media /app/tests /app/logs

# Criar usuário não-root
RUN adduser --disabled-password --gecos '' appuser \
    && chown -R appuser:appuser /app

# Stage de desenvolvimento
FROM base as development

# Copiar apenas o requirements.txt primeiro
COPY --chown=appuser:appuser requirements.txt .

# Instalar dependências de desenvolvimento
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install pytest pytest-django pytest-cov factory-boy

USER appuser

# Copiar o código do projeto
COPY --chown=appuser:appuser . .

# Stage de produção
FROM base as production

# Copiar apenas o requirements.txt primeiro
COPY --chown=appuser:appuser requirements.txt .

# Instalar apenas dependências de produção
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

USER appuser

# Copiar o código do projeto
COPY --chown=appuser:appuser . .

# Configurar variáveis de ambiente específicas para produção
ENV DJANGO_ENV=production \
    DEBUG=False

# Comando de produção usando gunicorn
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "120"]

# Stage de testes
FROM development as testing

# Configurar variáveis de ambiente específicas para testes
ENV DJANGO_ENV=testing \
    DEBUG=True \
    PYTHONPATH=/app

# Comando para executar os testes
CMD ["pytest", "--cov=.", "--cov-report=term-missing"]
