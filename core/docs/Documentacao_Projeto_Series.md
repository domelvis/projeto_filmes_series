
# 📺 Sistema de Lista de Séries - Documentação do Projeto

## 📌 Visão Geral
Este projeto tem como objetivo criar uma aplicação **Full Stack** moderna para gerenciar listas de séries.  
O sistema permitirá cadastrar séries, organizá-las em categorias (Assistidas, Não Gostei, Não Recomendo), além de recursos para pesquisa, autenticação e visualização estatística.

O projeto será desenvolvido em **Python (Django + DRF)** no backend e **Next.js + React** no frontend, com **PostgreSQL** como banco de dados.

---

## 🎯 Objetivos do Projeto
- Criar uma API REST moderna e segura.  
- Interface web responsiva e fácil de usar.  
- Aplicar boas práticas de desenvolvimento e arquitetura.  
- Gerar um portfólio profissional para apresentação acadêmica.  

---

## 🏗️ Arquitetura Geral
**Frontend**: Next.js + React + TailwindCSS  
**Backend**: Django + Django Rest Framework  
**Banco de Dados**: PostgreSQL  
**Autenticação**: JWT  
**Deploy**: Vercel (frontend) + Render/Heroku/Docker (backend)  

---

## ⚙️ Funcionalidades Principais
- CRUD de séries (Adicionar, Editar, Excluir, Visualizar).  
- Filtros por categoria (Assistidas, Não Gostei, Não Recomendo).  
- Pesquisa por título ou gênero.  
- Login e registro de usuários.  
- Dashboard com estatísticas básicas.  
- Tema escuro/claro (Dark Mode).  

---

## 📂 Estrutura de Pastas (Proposta)
```
projeto-series/
  backend/
    core/            # Configurações do Django
    series/          # App para CRUD de séries
    users/           # App para autenticação e usuários
    api/             # Rotas e views do DRF
    tests/           # Testes automatizados
    requirements.txt # Dependências do backend

  frontend/
    pages/           # Páginas do Next.js
    components/      # Componentes React reutilizáveis
    services/        # Consumo da API
    styles/          # Estilização com TailwindCSS
    package.json     # Dependências do frontend

  docs/
    README.md        # Documentação principal
    API.md           # Documentação da API

  docker-compose.yml # Configuração para Docker
```

---

## 🛠️ Tecnologias Utilizadas
- **Frontend**: Next.js, React, TailwindCSS, Axios  
- **Backend**: Python, Django, Django Rest Framework, Simple JWT  
- **Banco de Dados**: PostgreSQL  
- **Ferramentas Extras**: Docker, Swagger, GitHub Actions (CI/CD)  

---

## 📋 Requisitos Funcionais

| ID   | Descrição                                        | Prioridade |
|------|--------------------------------------------------|------------|
| RF01 | Adicionar séries com título, gênero e status      | Alta       |
| RF02 | Editar informações das séries                    | Média      |
| RF03 | Excluir séries                                    | Alta       |
| RF04 | Filtrar por status e pesquisar por título/gênero  | Alta       |
| RF05 | Autenticação de usuários com JWT                  | Alta       |
| RF06 | Dashboard com estatísticas básicas               | Baixa      |

---

## 🚀 Requisitos Não Funcionais

| ID    | Descrição                                       | Prioridade |
|-------|-------------------------------------------------|------------|
| RNF01 | Interface responsiva e intuitiva                | Alta       |
| RNF02 | API REST seguindo padrões de mercado            | Alta       |
| RNF03 | Código limpo e bem estruturado                  | Alta       |
| RNF04 | Testes automatizados para funcionalidades-chave | Média      |
| RNF05 | Documentação clara e completa                   | Alta       |

---

## 🧩 Melhorias Futuras
- Integração com API externas (ex: IMDb).  
- Sistema de recomendações personalizadas.  
- Exportação da lista em CSV/PDF.  
- Suporte a múltiplos idiomas.  

---

## 🧪 Testes
- **Backend**: Testes unitários para APIs e autenticação.  
- **Frontend**: Testes de interface com Jest e React Testing Library.  

---

## 🏁 Deploy e Hospedagem
- **Frontend**: Deploy no Vercel.  
- **Backend**: Deploy no Render/Heroku com Docker.  
- **Banco de Dados**: PostgreSQL hospedado no Supabase ou Railway.  

---

## 📖 Documentação da API
Será criada utilizando **Swagger** ou **DRF Spectacular**.  
Endpoint: `/api/docs`  

---

## 👨‍💻 Equipe e Contribuição
- Projeto acadêmico para portfólio pessoal.  
- Aberto para contribuições futuras no GitHub.  

---
