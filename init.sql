-- Script de inicialização do banco de dados
-- Este arquivo será executado automaticamente quando o container PostgreSQL iniciar

-- Criar extensões úteis (se necessário)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Configurar encoding e locale
SET client_encoding = 'UTF8';

-- Configurações específicas do banco (opcional)
ALTER DATABASE series_db SET timezone TO 'America/Sao_Paulo';

-- Comentário para verificar se o script foi executado
COMMENT ON DATABASE series_db IS 'Banco de dados para aplicação de séries - Inicializado automaticamente';

-- Criar tabelas adicionais ou configurações específicas da aplicação
-- (O Django criará as tabelas automaticamente via migrations)
