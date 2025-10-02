🎬 Gerenciador de Séries de TV - Documentação Completa do Projeto
📋 Índice
Visão Geral do Projeto

Arquitetura

Stack Tecnológica

Documentação da API

Guia de Desenvolvimento

Deploy

Testes

Contribuição

🎯 Visão Geral do Projeto
Gerenciador de Séries de TV é uma aplicação web full-stack para gerenciar e descobrir séries de TV. Desenvolvida com tecnologias modernas e seguindo melhores práticas, oferece uma solução completa para entusiastas de séries.

🌟 Funcionalidades Principais
Gerenciamento de Séries: Operações completas de CRUD para séries de TV

Sistema de Avaliações: Classificações e reviews com suporte a markdown

Perfis de Usuário: Listas personalizadas e acompanhamento de progresso

Busca Avançada: Filtros por gênero, status e avaliações

Design Responsivo: Abordagem mobile-first com temas claro/escuro

Analytics em Tempo Real: Dashboard com estatísticas de visualização

🎯 Público-Alvo
Entusiastas de séries e maratonistas

Críticos e revisores de conteúdo

Desenvolvedores interessados em aplicações Django/Next.js full-stack

🏗 Arquitetura
Diagrama de Arquitetura do Sistema
text
Camada do Cliente (Frontend) → Gateway API (Nginx) → Camada de Aplicação (Django) → Camada de Dados (PostgreSQL/Redis)
🔧 Componentes da Arquitetura
Frontend Layer
Next.js 14+: Framework React com SSR e SSG

Tailwind CSS: Sistema de design utilitário

Axios: Cliente HTTP para consumo de API

Context API: Gerenciamento de estado global

Backend Layer
Django 4.2+: Framework web Python

Django REST Framework: API RESTful

Simple JWT: Autenticação por tokens

Django CORS: Controle de origem cruzada

Data Layer
PostgreSQL 15+: Banco de dados relacional principal

Redis 7+: Cache e message broker

Celery: Tarefas assíncronas

Flower: Monitoramento do Celery

Infrastructure Layer
Docker: Containerização

Docker Compose: Orquestração

Nginx: Proxy reverso e servidor web

Gunicorn: Servidor WSGI Python

🛠 Stack Tecnológica
Backend & API
https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
https://img.shields.io/badge/Django_REST-ff1709?style=for-the-badge&logo=django&logoColor=white

Banco de Dados & Cache
https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white
https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white

Frontend
https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white
https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black
https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white

Infraestrutura
https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white

📚 Documentação da API
Endpoints Principais
Autenticação
http
POST /api/auth/login/
POST /api/auth/register/
POST /api/auth/refresh/
POST /api/auth/logout/
Séries
http
GET    /api/series/           # Listar séries
POST   /api/series/           # Criar série
GET    /api/series/{id}/      # Detalhes da série
PUT    /api/series/{id}/      # Atualizar série
DELETE /api/series/{id}/      # Excluir série
Avaliações
http
GET    /api/reviews/          # Listar avaliações
POST   /api/reviews/          # Criar avaliação
GET    /api/reviews/{id}/     # Detalhes da avaliação
PUT    /api/reviews/{id}/     # Atualizar avaliação
DELETE /api/reviews/{id}/     # Excluir avaliação
Usuários
http
GET    /api/users/profile/    # Perfil do usuário
PUT    /api/users/profile/    # Atualizar perfil
GET    /api/users/watchlist/  # Lista de observação
Exemplos de Requisições
Criar Série
bash
curl -X POST http://localhost:8000/api/series/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {token}" \
  -d '{
    "title": "Breaking Bad",
    "genre": "Drama",
    "status": "assistida",
    "rating": 5,
    "description": "Um professor de química se transforma em produtor de metanfetamina."
  }'
Filtrar Séries
bash
curl -X GET "http://localhost:8000/api/series/?genre=Drama&status=assistida&search=breaking"
💻 Guia de Desenvolvimento
Pré-requisitos
Docker 20.10+

Docker Compose 2.0+

Git

Python 3.11+ (para desenvolvimento local)

Configuração do Ambiente
1. Clone o Repositório
bash
git clone https://github.com/domelvis/projeto-series.git
cd projeto-series
2. Configure Variáveis de Ambiente
bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
3. Execute a Aplicação
bash
# Desenvolvimento
docker-compose -f docker-compose.dev.yml up --build

# Produção
docker-compose -f docker-compose.prod.yml up --build -d
Estrutura do Projeto
text
projeto-series/
├── backend/                 # Aplicação Django
│   ├── api/                # API REST
│   ├── series/             # App de séries
│   ├── reviews/            # Sistema de avaliações
│   ├── users/              # Autenticação e usuários
│   └── core/               # Configurações principais
├── frontend/               # Aplicação Next.js
│   ├── pages/              # Rotas e páginas
│   ├── components/         # Componentes React
│   ├── services/           # Clientes API
│   └── styles/             # Estilos Tailwind
├── nginx/                  # Configuração do Nginx
├── docker/                 # Configurações Docker
└── docs/                   # Documentação
Comandos de Desenvolvimento
Backend (Django)
bash
# Acessar container
docker-compose exec backend bash

# Migrações
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate

# Superusuário
docker-compose exec backend python manage.py createsuperuser

# Testes
docker-compose exec backend python manage.py test

# Shell interativo
docker-compose exec backend python manage.py shell
Frontend (Next.js)
bash
# Acessar container
docker-compose exec frontend bash

# Desenvolvimento
npm run dev

# Build
npm run build

# Testes
npm run test
🚀 Deploy
Configuração de Produção
Variáveis de Ambiente (.env)
env
DEBUG=False
SECRET_KEY=sua-chave-super-secreta-aqui
ALLOWED_HOSTS=seudominio.com,www.seudominio.com
DATABASE_URL=postgresql://user:pass@db:5432/projeto_series
REDIS_URL=redis://redis:6379/0
Deploy com Docker
bash
# Build e deploy
docker-compose -f docker-compose.prod.yml up --build -d

# Verificar logs
docker-compose -f docker-compose.prod.yml logs -f

# Scale services
docker-compose -f docker-compose.prod.yml up -d --scale backend=3
Plataformas de Hospedagem Recomendadas
Frontend
Vercel: Deploy automático do Next.js

Netlify: Alternativa excelente

Backend
Railway: Simples e eficiente

Render: Boa opção gratuita

Heroku: Tradicional (com Docker)

Banco de Dados
Supabase: PostgreSQL gratuito

Railway: PostgreSQL com bom free tier

ElephantSQL: Alternativa sólida

🧪 Testes
Estratégia de Testes
Testes de Backend (Django)
python
# tests/test_series.py
class SeriesTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', 'test@email.com', 'password')
        self.series_data = {
            'title': 'Test Series',
            'genre': 'Drama',
            'status': 'assistida'
        }
    
    def test_series_creation(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/series/', self.series_data)
        self.assertEqual(response.status_code, 201)
Testes de Frontend (Jest/Testing Library)
javascript
// tests/SeriesList.test.js
import { render, screen } from '@testing-library/react'
import SeriesList from '../components/SeriesList'

test('renders series list', () => {
  render(<SeriesList />)
  const titleElement = screen.getByText(/Séries/i)
  expect(titleElement).toBeInTheDocument()
})
Testes de API (Postman)
bash
# Collection do Postman incluída em docs/postman/
npm run test:api
Cobertura de Testes
bash
# Backend
docker-compose exec backend python -m pytest --cov=.

# Frontend
docker-compose exec frontend npm test -- --coverage
🤝 Contribuição
Fluxo de Contribuição
Fork do Projeto

bash
git fork https://github.com/domelvis/projeto-series.git
Branch de Feature

bash
git checkout -b feature/nova-funcionalidade
Commit Semântico

bash
git commit -m "feat: adiciona sistema de recomendações"
Push e Pull Request

bash
git push origin feature/nova-funcionalidade
Padrões de Código
Backend (Python/Django)
python
# Boas práticas
class SeriesViewSet(viewsets.ModelViewSet):
    """ViewSet para gerenciamento de séries."""
    
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        """Retorna avaliações de uma série."""
        series = self.get_object()
        reviews = series.reviews.all()
        # ...
Frontend (React/Next.js)
javascript
// Componentes funcionais com hooks
const SeriesList = ({ series, onSelect }) => {
  const [filter, setFilter] = useState('')
  
  const filteredSeries = useMemo(() => {
    return series.filter(s => s.title.includes(filter))
  }, [series, filter])
  
  return (
    <div className="series-grid">
      {filteredSeries.map(series => (
        <SeriesCard key={series.id} series={series} onClick={onSelect} />
      ))}
    </div>
  )
}
Code Review Checklist
Código segue os padrões estabelecidos

Testes passam e cobrem a funcionalidade

Documentação atualizada

Migrações de banco (se necessário)

Variáveis de ambiente configuradas

📞 Suporte e Contato
Canais de Comunicação
Issues: GitHub Issues

Email: elvishootsrockreggae@hotmail.com

LinkedIn: Elvis Marcelo

Recursos Adicionais
Documentação Online: GitHub Wiki

Board do Projeto: GitHub Projects

Releases: GitHub Releases

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

Desenvolvido com ❤️ por Elvis Marcelo Pereira de Souza

https://img.shields.io/badge/GitHub-domelvis-181717?style=for-the-badge&logo=github
https://img.shields.io/badge/LinkedIn-Elvis%2520Marcelo-0A66C2?style=for-the-badge&logo=linkedin



