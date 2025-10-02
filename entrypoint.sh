#!/bin/bash

# Exit on any error
set -e

# Função para esperar serviços
wait_for_service() {
    local host=$1
    local port=$2
    local service=$3
    
    echo "Waiting for $service..."
    while ! nc -z $host $port; do
        echo ".$service is unavailable - sleeping"
        sleep 1
    done
    echo "$service is ready!"
}

# Verificar ambiente
echo "Current environment: $DJANGO_ENV"
if [ "$DJANGO_ENV" = "testing" ]; then
    echo "Setting up test environment..."
    wait_for_service db 5432 "database"
    python manage.py migrate
    exec "$@"
    exit 0
fi

# Esperar dependências
wait_for_service db 5432 "database"
wait_for_service redis 6379 "redis"

# Criar diretórios necessários
mkdir -p /app/logs /app/staticfiles /app/media

# Executar migrações
echo "Running migrations..."
python manage.py migrate

# Configurações específicas por ambiente
if [ "$DJANGO_ENV" = "development" ]; then
    echo "Setting up development environment..."
    
    # Coletar arquivos estáticos para desenvolvimento
    python manage.py collectstatic --noinput --clear
    
    # Criar superuser de desenvolvimento
    python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='dev_admin').exists():
    User.objects.create_superuser('dev_admin', 'dev_admin@example.com', 'dev123')
    print('Development superuser created: dev_admin/dev123')
else:
    print('Development superuser already exists')
EOF

elif [ "$DJANGO_ENV" = "production" ]; then
    echo "Setting up production environment..."
    
    # Coletar arquivos estáticos em produção
    python manage.py collectstatic --noinput --clear
    
    # Criar superuser de produção se não existir
    python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Production superuser created: admin/admin123')
else:
    print('Production superuser already exists')
EOF
fi

# Iniciar aplicação
echo "Starting application in $DJANGO_ENV mode..."
exec "$@"
