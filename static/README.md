# Sistema de CSS - Séries TV

Este diretório contém todos os arquivos de estilo CSS para o projeto Séries TV, criados com um design moderno e profissional.

## Estrutura de Arquivos

```
static/
├── css/
│   ├── base.css          # Estilos base e variáveis CSS
│   ├── series.css        # Estilos específicos para páginas de séries
│   └── users.css         # Estilos específicos para páginas de usuários
├── js/
│   └── main.js           # JavaScript principal com funcionalidades interativas
└── images/               # Diretório para imagens estáticas
```

## Características do Design

### 🎨 Paleta de Cores Moderna
- **Primária**: #6366f1 (Indigo)
- **Secundária**: #64748b (Slate)
- **Accent**: #f59e0b (Amber)
- **Sucesso**: #10b981 (Emerald)
- **Aviso**: #f59e0b (Amber)
- **Perigo**: #ef4444 (Red)
- **Info**: #3b82f6 (Blue)

### 🎯 Recursos Implementados

#### CSS Base (`base.css`)
- ✅ Variáveis CSS para consistência
- ✅ Reset e estilos globais
- ✅ Navegação moderna com gradientes
- ✅ Sistema de cards com sombras e animações
- ✅ Botões com efeitos hover e transições
- ✅ Formulários estilizados
- ✅ Sistema de badges e alertas
- ✅ Breadcrumbs e paginação
- ✅ Footer responsivo
- ✅ Scrollbar customizada
- ✅ Estados de loading
- ✅ Preparação para dark mode

#### CSS para Séries (`series.css`)
- ✅ Header com gradiente e padrão de fundo
- ✅ Cards de séries com hover effects
- ✅ Placeholder para imagens sem foto
- ✅ Badges de gênero com cores específicas
- ✅ Página de detalhes com layout moderno
- ✅ Séries relacionadas
- ✅ Formulários de criação/edição
- ✅ Preview de imagens
- ✅ Confirmação de exclusão
- ✅ Filtros e busca
- ✅ Estado vazio
- ✅ Animações específicas
- ✅ Loading skeleton

#### CSS para Usuários (`users.css`)
- ✅ Páginas de autenticação com design moderno
- ✅ Cards de login/registro com animações
- ✅ Formulários com validação visual
- ✅ Toggle de senha
- ✅ Página de perfil com header gradiente
- ✅ Estatísticas do perfil
- ✅ Seções organizadas
- ✅ Grid de séries do usuário
- ✅ Formulário de edição de perfil
- ✅ Preview de avatar
- ✅ Informações da conta
- ✅ Animações específicas
- ✅ Estados de loading

#### JavaScript (`main.js`)
- ✅ Inicialização automática
- ✅ Tooltips do Bootstrap
- ✅ Animações de entrada
- ✅ Validação de formulários em tempo real
- ✅ Preview de imagens
- ✅ Toggle de senha
- ✅ Scroll suave
- ✅ Estados de loading
- ✅ Toggle de tema (preparado)
- ✅ Notificações
- ✅ Confirmação de ações
- ✅ Copiar para clipboard
- ✅ Funções específicas para séries
- ✅ Funções específicas para usuários
- ✅ Lazy loading
- ✅ Performance otimizada

### 📱 Design Responsivo

O sistema é totalmente responsivo com breakpoints para:
- **Desktop**: > 768px
- **Tablet**: 576px - 768px
- **Mobile**: < 576px

### 🎭 Animações e Transições

- Transições suaves em todos os elementos interativos
- Animações de entrada para cards e seções
- Efeitos hover com transformações
- Loading states com animações
- Gradientes animados nos headers

### 🎨 Componentes Personalizados

#### Cards
- Sombras dinâmicas
- Hover effects com elevação
- Bordas arredondadas
- Gradientes nos headers

#### Botões
- Efeitos de brilho no hover
- Gradientes de fundo
- Estados de loading
- Ícones integrados

#### Formulários
- Validação visual em tempo real
- Campos com foco destacado
- Mensagens de erro estilizadas
- Preview de imagens

#### Badges
- Cores específicas por gênero
- Efeitos de pulso no hover
- Tipografia em maiúsculas

### 🚀 Performance

- CSS otimizado com variáveis
- JavaScript modular
- Lazy loading para imagens
- Animações com `transform` e `opacity`
- Debounce e throttle para eventos

### 🎯 Acessibilidade

- Contraste adequado nas cores
- Foco visível nos elementos interativos
- Textos alternativos para ícones
- Navegação por teclado
- Screen reader friendly

## Como Usar

### 1. Incluir no Template Base
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/base.css' %}">
<link rel="stylesheet" href="{% static 'css/series.css' %}">
<link rel="stylesheet" href="{% static 'css/users.css' %}">
<script src="{% static 'js/main.js' %}"></script>
```

### 2. Classes CSS Disponíveis

#### Utilitárias
- `.text-gradient` - Texto com gradiente
- `.shadow-custom` - Sombra personalizada
- `.rounded-custom` - Bordas arredondadas
- `.transition-custom` - Transição personalizada

#### Animações
- `.animate-fade-in-up` - Animação de entrada
- `.animate-fade-in` - Fade in simples
- `.animate-slide-in-right` - Slide da direita

#### Componentes
- `.series-card` - Card de série
- `.auth-card` - Card de autenticação
- `.profile-section` - Seção de perfil
- `.genre-badge` - Badge de gênero

### 3. JavaScript Global

O objeto `SeriesTV` está disponível globalmente com funções:
- `SeriesTV.showNotification(message, type, duration)`
- `SeriesTV.confirmAction(message, callback)`
- `SeriesTV.copyToClipboard(text)`
- `SeriesTV.shareSerie(title, url)`
- `SeriesTV.toggleTheme()`

## Personalização

### Cores
Modifique as variáveis CSS em `base.css`:
```css
:root {
    --primary-color: #6366f1;
    --secondary-color: #64748b;
    --accent-color: #f59e0b;
    /* ... outras variáveis */
}
```

### Animações
Ajuste as durações e efeitos:
```css
:root {
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    --transition-fast: all 0.15s ease-in-out;
}
```

## Compatibilidade

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Mobile browsers

## Próximos Passos

- [ ] Implementar dark mode completo
- [ ] Adicionar mais animações
- [ ] Criar tema personalizável
- [ ] Otimizar para PWA
- [ ] Adicionar mais componentes

---

**Desenvolvido com ❤️ para o projeto Séries TV**

