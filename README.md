🎬 Séries de TV - Plataforma de Gerenciamento # 🐳 Séries TV - Docker Setup
https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white
https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white
https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white

Uma plataforma completa para gerenciamento e descoberta de séries de TV, desenvolvida com Django e containerizada com Docker.

📋 Índice
Visão Geral

Funcionalidades

Tecnologias

Arquitetura

Quick Start

Estrutura do Projeto

Desenvolvimento

Produção

API Documentation

Roadmap

🎯 Visão Geral
O Séries de TV é uma aplicação web moderna que permite aos usuários explorar, gerenciar e acompanhar suas séries favoritas. Com um sistema completo de avaliações, listas personalizadas e recomendações inteligentes.

https://via.placeholder.com/800x400/2D3748/FFFFFF?text=Series+TV+Dashboard

✨ Funcionalidades
🎭 Gerenciamento de Conteúdo
Catálogo completo de séries e filmes

Sistema de temporadas e episódios

Busca avançada e filtros

Upload e gestão de mídias

⭐ Sistema de Avaliações
Avaliações e comentários

Sistema de rating (1-5 estrelas)

Reviews detalhadas com markdown

Moderação de conteúdo

📊 Personalização
Listas de watchlist personalizadas

Acompanhamento de progresso

Recomendações baseadas no perfil

Perfis de usuário customizáveis

🔧 Ferramentas Avançadas
Processamento assíncrono com Celery

Cache Redis para performance

API REST completa

Monitoramento em tempo real

🛠 Tecnologias
Backend
https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
https://img.shields.io/badge/Django_REST-ff1709?style=for-the-badge&logo=django&logoColor=white

Banco de Dados & Cache
https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white
https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white

Frontend
https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black

Infraestrutura
https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white
https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white

🏗 Arquitetura









Serviços Containerizados
Serviço	Porta	Descrição
web	8000	Aplicação Django principal
db	5432	Banco de dados PostgreSQL
redis	6379	Cache e message broker
nginx	80	Proxy reverso e servidor web
celery	-	Processamento assíncrono
celery-beat	-	Agendador de tarefas
flower	5555	Monitoramento do Celery
🚀 Quick Start
Pré-requisitos
Docker 20.10+

Docker Compose 2.0+

Git

Instalação em 3 Passos
bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/projeto-series.git
cd projeto-series

# 2. Configure as variáveis de ambiente
cp env.example .env
# Edite o .env com suas configurações

# 3. Execute a aplicação
docker-compose up --build -d
Acesso Inicial
🌐 Aplicação: http://localhost:8000

📚 API Docs: http://localhost:8000/api/docs/

⚙️ Admin: http://localhost:8000/admin/

📊 Monitor: http://localhost:5555

Credenciais padrão do admin:

Usuário: admin

Senha: admin123

📁 Estrutura do Projeto
text
PROJETO-SERIES/
├── 📁 backend/                 # Aplicação Django
│   ├── 📁 api/                # API REST
│   │   └── 📁 v1/             # Versão 1 da API
│   ├── 📁 core/               # Configurações principais
│   ├── 📁 media/              # Arquivos de mídia
│   │   └── 📁 series/         # Imagens das séries
│   ├── 📁 reviews/            # 🌟 NOVO: Sistema de avaliações
│   │   ├── models.py          # Modelos de reviews
│   │   ├── views.py           # Views das avaliações
│   │   └── urls.py            # URLs do app reviews
│   ├── 📁 services/           # Lógica de negócio
│   │   ├── 📁 external/       # Integrações externas
│   │   └── 📁 internal/       # Serviços internos
│   ├── 📁 static/             # Arquivos estáticos
│   │   ├── 📁 css/            # Estilos CSS
│   │   │   ├── base.css       # Estilos base
│   │   │   ├── series.css     # Estilos específicos
│   │   │   └── 📁 components/ # 🌟 NOVO: CSS modular
│   │   │       ├── _buttons.css
│   │   │       └── _cards.css
│   │   └── 📁 js/             # JavaScript
│   │       ├── main.js        # JS principal
│   │       ├── series.js      # JS das séries
│   │       └── users.js       # JS de usuários
│   ├── 📁 templates/          # Templates HTML
│   │   ├── base.html          # Template base
│   │   ├── 404.html           # 🌟 NOVO: Página 404
│   │   ├── 📁 partials/       # 🌟 NOVO: Componentes
│   │   │   ├── _header.html
│   │   │   ├── _footer.html
│   │   │   └── _pagination.html
│   │   ├── 📁 series/         # Templates de séries
│   │   │   ├── list.html
│   │   │   ├── detail.html
│   │   │   └── search_results.html # 🌟 NOVO: Busca
│   │   └── 📁 users/          # Templates de usuários
│   ├── 📁 series/             # App principal de séries
│   ├── 📁 users/              # App de usuários
│   └── 📁 tests/              # Testes automatizados
├── 📁 nginx/                  # Configuração do Nginx
├── 📁 docker/                 # Configurações Docker
├── docker-compose.yml         # Orquestração
└── README.md                  # Este arquivo
🗃️ Modelo de Dados
sql
-- Principais tabelas do sistema
content           -- Conteúdo principal (filmes/séries)
genres            -- Gêneros/categorias
content_genres    -- Relação conteúdo-gêneros
seasons           -- Temporadas (para séries)
episodes          -- Episódios
reviews           -- Sistema de avaliações
user_watchlist    -- Listas de usuários
watch_progress    -- Progresso de visualização
recommendations   -- Sistema de recomendações
content_analytics -- Estatísticas e análises
💻 Desenvolvimento
Comandos Úteis
bash
# Acessar o container
docker-compose exec web bash

# Executar migrações
docker-compose exec web python manage.py migrate

# Criar superusuário
docker-compose exec web python manage.py createsuperuser

# Coletar arquivos estáticos
docker-compose exec web python manage.py collectstatic

# Executar testes
docker-compose exec web python manage.py test

# Shell do Django
docker-compose exec web python manage.py shell
Logs e Monitoramento
bash
# Ver todos os logs
docker-compose logs -f

# Logs específicos
docker-compose logs -f web
docker-compose logs -f db

# Status dos serviços
docker-compose ps

# Health check
curl http://localhost:8000/health/
🚀 Produção
Configurações de Segurança
bash
# .env para produção
DEBUG=False
SECRET_KEY=suachavemuitoforteaqui
ALLOWED_HOSTS=seudominio.com,www.seudominio.com
SECURE_SSL_REDIRECT=True
Otimizações
Nginx: Gzip, cache e rate limiting

PostgreSQL: Configurações otimizadas

Redis: Cache de sessões e queries

Celery: Processamento assíncrono

Escalabilidade
bash
# Escalar horizontalmente
docker-compose up -d --scale web=3 --scale celery=4
📚 API Documentation
Endpoints Principais
Método	Endpoint	Descrição
GET	/api/series/	Listar séries
POST	/api/series/	Criar série
GET	/api/series/{id}/	Detalhes da série
GET	/api/reviews/	Listar avaliações
POST	/api/reviews/	Criar avaliação
Documentação Interativa
Swagger UI: /api/docs/

ReDoc: /api/redoc/

Schema: /api/schema/

🛣️ Roadmap
🎯 Melhorias Imediatas (v1.1)
Sistema de notificações

Importação de dados via API externa

Modo offline básico

Exportação de dados

🚀 Versão 2.0
Aplicativo mobile (React Native)

Sistema de recomendações com ML

Player de vídeo integrado

Social features (seguir usuários)

🔮 Futuro
Suporte a múltiplos idiomas

API GraphQL

Microserviços architecture

Kubernetes deployment

🤝 Contribuição
Fork o projeto

Crie uma branch: git checkout -b feature/nova-feature

Commit suas mudanças: git commit -m 'Add nova feature'

Push para a branch: git push origin feature/nova-feature

Abra um Pull Request

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

🆘 Suporte
Solução de Problemas Comuns
bash
# Portas em uso
sudo lsof -i :8000

# Permissões de arquivo
sudo chown -R $USER:$USER .
chmod +x backend/entrypoint.sh

# Limpar cache
docker-compose exec redis redis-cli FLUSHALL

# Reiniciar serviços
docker-compose restart web db redis
Limpeza Completa
bash
# Parar e remover tudo
docker-compose down -v --remove-orphans

# Limpar Docker
docker system prune -a -f
Atualização
bash
# Atualizar projeto
git pull
docker-compose down
docker-compose up --build -d
Desenvolvido com ❤️ pela Equipe Séries de TV

📧 Contato: equipe@projetoseries.com
🐛 Issues: GitHub Issues
📖 Documentação: Wiki

<div align="center">
⭐️ Gostou do projeto? Deixe uma estrela no GitHub!
https://api.star-history.com/svg?repos=seu-usuario/projeto-series&type=Date

</div>
