# 🐳 Séries TV - Docker Setup

Este documento explica como executar o projeto Séries TV usando Docker e Docker Compose.

## 📋 Pré-requisitos

- Docker (versão 20.10+)
- Docker Compose (versão 2.0+)
- Git

## 🚀 Início Rápido

### 1. Clone o repositório
```bash
git clone <seu-repositorio>
cd projeto-series
```

### 2. Configure as variáveis de ambiente
```bash
cp env.example .env
```

Edite o arquivo `.env` com suas configurações:
```env
# Django Settings
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# Database Settings
POSTGRES_DB=series_db
POSTGRES_USER=series_user
POSTGRES_PASSWORD=series_password

# Redis Settings
REDIS_URL=redis://redis:6379/0
```

### 3. Execute o projeto
```bash
# Construir e iniciar todos os serviços
docker-compose up --build

# Ou em background
docker-compose up -d --build
```

### 4. Acesse a aplicação
- **Aplicação Web**: http://localhost:8000
- **API Documentation**: http://localhost:8000/api/docs/
- **Admin Django**: http://localhost:8000/admin/
- **Flower (Celery)**: http://localhost:5555

## 🏗️ Arquitetura dos Serviços

### Serviços Incluídos

| Serviço | Porta | Descrição |
|---------|-------|-----------|
| **web** | 8000 | Aplicação Django |
| **db** | 5432 | PostgreSQL Database |
| **redis** | 6379 | Redis Cache |
| **nginx** | 80 | Reverse Proxy |
| **celery** | - | Worker de tarefas |
| **celery-beat** | - | Agendador de tarefas |
| **flower** | 5555 | Monitor do Celery |

### Volumes Persistentes

- `postgres_data`: Dados do PostgreSQL
- `redis_data`: Dados do Redis
- `static_volume`: Arquivos estáticos
- `media_volume`: Arquivos de mídia

## 🔧 Comandos Úteis

### Gerenciamento de Containers

```bash
# Parar todos os serviços
docker-compose down

# Parar e remover volumes
docker-compose down -v

# Ver logs
docker-compose logs -f

# Ver logs de um serviço específico
docker-compose logs -f web

# Executar comandos no container
docker-compose exec web python manage.py shell
docker-compose exec web python manage.py createsuperuser
```

### Desenvolvimento

```bash
# Instalar dependências
docker-compose exec web pip install -r requirements.txt

# Executar migrações
docker-compose exec web python manage.py migrate

# Coletar arquivos estáticos
docker-compose exec web python manage.py collectstatic

# Executar testes
docker-compose exec web python manage.py test

# Acessar shell do Django
docker-compose exec web python manage.py shell
```

### Banco de Dados

```bash
# Acessar PostgreSQL
docker-compose exec db psql -U series_user -d series_db

# Backup do banco
docker-compose exec db pg_dump -U series_user series_db > backup.sql

# Restaurar backup
docker-compose exec -T db psql -U series_user -d series_db < backup.sql
```

## 🔐 Configurações de Segurança

### Produção

Para produção, atualize o arquivo `.env`:

```env
DEBUG=False
SECRET_KEY=sua-chave-secreta-muito-forte
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000
```

### SSL/HTTPS

Para habilitar HTTPS, adicione certificados SSL em `nginx/ssl/` e atualize `nginx/conf.d/default.conf`.

## 📊 Monitoramento

### Health Checks

Todos os serviços incluem health checks:

```bash
# Verificar status dos serviços
docker-compose ps

# Health check manual
curl http://localhost:8000/health/
```

### Logs

```bash
# Logs em tempo real
docker-compose logs -f

# Logs específicos
docker-compose logs -f web
docker-compose logs -f db
docker-compose logs -f redis
```

## 🐛 Troubleshooting

### Problemas Comuns

1. **Porta já em uso**
   ```bash
   # Verificar portas em uso
   netstat -tulpn | grep :8000
   
   # Parar serviços conflitantes
   sudo systemctl stop apache2  # ou nginx
   ```

2. **Permissões de arquivo**
   ```bash
   # Corrigir permissões
   sudo chown -R $USER:$USER .
   chmod +x backend/entrypoint.sh
   ```

3. **Banco de dados não conecta**
   ```bash
   # Verificar logs do banco
   docker-compose logs db
   
   # Reiniciar apenas o banco
   docker-compose restart db
   ```

4. **Cache Redis**
   ```bash
   # Limpar cache Redis
   docker-compose exec redis redis-cli FLUSHALL
   ```

### Limpeza Completa

```bash
# Parar e remover tudo
docker-compose down -v --remove-orphans

# Remover imagens
docker-compose down --rmi all

# Limpeza completa do Docker
docker system prune -a
```

## 🔄 Atualizações

### Atualizar o Projeto

```bash
# Parar serviços
docker-compose down

# Atualizar código
git pull

# Reconstruir e iniciar
docker-compose up --build -d
```

### Atualizar Dependências

```bash
# Atualizar requirements.txt
docker-compose exec web pip freeze > requirements.txt

# Reconstruir imagem
docker-compose build web
```

## 📈 Performance

### Otimizações

1. **Nginx**: Configurado com gzip, cache e rate limiting
2. **PostgreSQL**: Configurações otimizadas para produção
3. **Redis**: Cache de sessões e dados frequentes
4. **Celery**: Processamento assíncrono de tarefas

### Escalabilidade

Para escalar horizontalmente:

```bash
# Escalar workers do Celery
docker-compose up -d --scale celery=3

# Escalar aplicação Django
docker-compose up -d --scale web=2
```

## 📚 Documentação da API

Acesse a documentação interativa da API:

- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/
- **Schema JSON**: http://localhost:8000/api/schema/

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

**Desenvolvido com ❤️ para o projeto Séries TV**

🌲 Estrutura de Arquivos do PROJETO-SERIES (Atualizada)
PROJETO-SERIES/
├── backend/
│   ├── .venv/                         # Ambiente Virtual Python (venv)
│   │   ├── Include/
│   │   ├── Lib/
│   │   └── Scripts/
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── urls.py
│   ├── core/                          # Configurações Principais
│   │   ├── ... (arquivos de configuração)
│   ├── media/                         # Arquivos de Mídia
│   │   └── series/
│   ├── reviews/                       # 🌟 NOVO APP: Lógica de Comentários e Avaliações
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── services/                      # Lógica de Negócio Modular
│   │   ├── external/
│   │   └── internal/
│   ├── static/                        # Arquivos Estáticos Globais
│   │   ├── css/
│   │   │   ├── base.css
│   │   │   ├── ... (layout.css, users.css, series.css)
│   │   │   └── components/            # 🌟 NOVA PASTA: CSS Modular
│   │   │       ├── _buttons.css
│   │   │       └── _cards.css
│   │   ├── images/
│   │   └── js/
│   │       ├── main.js
│   │       ├── series.js
│   │       └── users.js
│   ├── templates/                     # Templates do Projeto
│   │   ├── base.html
│   │   ├── 404.html                   # 🌟 NOVO ARQUIVO: Página de Erro 404 Customizada
│   │   ├── partials/                  # 🌟 NOVA PASTA: Componentes Reutilizáveis
│   │   │   ├── _footer.html
│   │   │   ├── _header.html
│   │   │   ├── _messages.html
│   │   │   └── _pagination.html
│   │   ├── series/
│   │   │   ├── confirm_delete.html
│   │   │   ├── detail.html
│   │   │   ├── form.html
│   │   │   ├── list.html
│   │   │   └── search_results.html    # 🌟 NOVO ARQUIVO: Para Busca Avançada
│   │   └── users/
│   │       ├── login.html
│   │       ├── profile_edit.html
│   │       ├── profile.html
│   │       └── register.html
│   ├── series/                        # App 'series'
│   │   └── ... (arquivos do app)
│   ├── users/                         # App 'users'
│   │   └── ... (arquivos do app)
│   ├── tests/
│   └── ... (Arquivos de Root)

📊 O que foi criado:
✅ 10 tabelas principais do sistema

✅ Todas as constraints e chaves estrangeiras

✅ Índices de performance otimizados

✅ Estrutura relacional completa

🗂️ Tabelas criadas:
content - Conteúdo principal (filmes/séries)

genres - Gêneros/categorias

content_genres - Relação conteúdo-gêneros

seasons - Temporadas (para séries)

episodes - Episódios

ratings - Sistema de avaliações

user_watchlist - Listas de usuários

watch_progress - Progresso de visualização

recommendations - Sistema de recomendações

content_analytics - Estatísticas e analytics
