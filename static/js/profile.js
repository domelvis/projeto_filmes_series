// Configuração do perfil
const initializeProfilePage = () => {
    // Atualizar contadores em tempo real
    updateLiveCounters();
    
    // Configurar tooltips
    setupProfileTooltips();
    
    // Configurar eventos de interação
    setupProfileEvents();
};

const setupProfileInteractions = () => {
    // Toggle da biografia (edição rápida)
    const bioSection = document.querySelector('.profile-bio');
    if (bioSection) {
        bioSection.addEventListener('dblclick', () => {
            window.location.href = bioSection.dataset.editUrl;
        });
    }
    
    // Hover effects nas séries
    const seriesCards = document.querySelectorAll('.series-card--profile');
    seriesCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.transition = 'transform 0.3s ease';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
};

const toggleBio = (editUrl) => {
    window.location.href = editUrl;
};

const updateLiveCounters = () => {
    // Atualizar contadores periodicamente (se necessário)
    setInterval(() => {
        // Buscar dados atualizados via API
        updateProfileStats();
    }, 30000);
};

const setupProfileTooltips = () => {
    // Verificar se Bootstrap está disponível
    if (typeof bootstrap !== 'undefined') {
        const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
        tooltipTriggerList.forEach(el => new bootstrap.Tooltip(el));
    } else {
        console.warn('Bootstrap não encontrado. Tooltips não serão inicializados.');
    }
};

const setupProfileEvents = () => {
    // Evento para acompanhar interações do usuário
    document.querySelectorAll('.series-card--profile .card-link').forEach(link => {
        link.addEventListener('click', function() {
            // Tracking de analytics
            if (typeof gtag !== 'undefined') {
                gtag('event', 'profile_series_click', {
                    'event_category': 'Profile',
                    'event_label': this.textContent
                });
            }
        });
    });
};

// Função para atualizar estatísticas via API
const updateProfileStats = async () => {
    try {
        const response = await fetch(`/api/v1/users/stats/${window.PROFILE_CONFIG.userId}/`);
        if (response.ok) {
            const newStats = await response.json();
            if (window.PROFILE_CONFIG) {
                window.PROFILE_CONFIG.stats = { ...window.PROFILE_CONFIG.stats, ...newStats };
                updateStatDisplay(newStats);
            }
        }
    } catch (error) {
        console.error('Erro ao atualizar estatísticas:', error);
    }
};

// Atualizar os elementos na tela com as novas estatísticas
const updateStatDisplay = (stats) => {
    if (!stats) return;

    const statElements = {
        'seriesCreated': document.querySelector('.stat-number[data-stat="series"]'),
        'favoritesCount': document.querySelector('.stat-number[data-stat="favorites"]'),
        'commentsCount': document.querySelector('.stat-number[data-stat="comments"]'),
        'membershipDays': document.querySelector('.stat-number[data-stat="membership"]')
    };

    Object.entries(stats).forEach(([key, value]) => {
        const element = statElements[key];
        if (element) {
            element.textContent = value;
        }
    });
};

// Função para verificar se o usuário está online
const checkUserStatus = () => navigator.onLine ? 'online' : 'offline';

// Cleanup quando a página for fechada
window.addEventListener('beforeunload', () => {
    // Limpar event listeners específicos se necessário
    const seriesCards = document.querySelectorAll('.series-card--profile');
    seriesCards.forEach(card => {
        card.removeEventListener('mouseenter', null);
        card.removeEventListener('mouseleave', null);
    });
});

// Error handling global para esta página
window.addEventListener('error', (e) => {
    console.error('Erro na página de perfil:', e.error);
});

// Inicialização quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', () => {
    initializeProfilePage();
    setupProfileInteractions();
});