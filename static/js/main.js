// Gerenciamento de notificações
const initNotifications = () => {
    const notifications = document.querySelectorAll('.alert');
    notifications.forEach(notification => {
        setTimeout(() => {
            notification.classList.add('opacity-0');
            setTimeout(() => notification.remove(), 500);
        }, 5000);
    });
};

// Gerenciamento de modais
const initModals = () => {
    const modals = document.querySelectorAll('[data-modal]');
    
    modals.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const modalId = trigger.dataset.modal;
            const modal = document.getElementById(modalId);
            
            if (modal) {
                modal.classList.remove('hidden');
                
                // Fechar modal
                const closeButtons = modal.querySelectorAll('[data-close-modal]');
                closeButtons.forEach(button => {
                    button.addEventListener('click', () => {
                        modal.classList.add('hidden');
                    });
                });
                
                // Fechar ao clicar fora
                modal.addEventListener('click', e => {
                    if (e.target === modal) {
                        modal.classList.add('hidden');
                    }
                });
            }
        });
    });
};

// Sistema de classificação por estrelas
const initRatingSystem = () => {
    const ratingContainers = document.querySelectorAll('.rating');
    
    ratingContainers.forEach(container => {
        const stars = container.querySelectorAll('.star');
        const input = container.querySelector('input[type="hidden"]');
        
        stars.forEach((star, index) => {
            star.addEventListener('click', () => {
                const rating = index + 1;
                input.value = rating;
                
                stars.forEach((s, i) => {
                    s.classList.toggle('active', i < rating);
                });
            });
            
            star.addEventListener('mouseover', () => {
                stars.forEach((s, i) => {
                    s.classList.toggle('hover', i <= index);
                });
            });
            
            star.addEventListener('mouseout', () => {
                stars.forEach(s => s.classList.remove('hover'));
            });
        });
    });
};

// Gerenciamento de favoritos
const initFavorites = () => {
    const favoriteButtons = document.querySelectorAll('[data-favorite]');
    
    favoriteButtons.forEach(button => {
        button.addEventListener('click', async () => {
            const seriesId = button.dataset.favorite;
            
            try {
                const response = await fetch(`/api/series/${seriesId}/favorite/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    }
                });
                
                if (response.ok) {
                    const data = await response.json();
                    const icon = button.querySelector('i');
                    
                    if (data.is_favorite) {
                        icon.classList.remove('far');
                        icon.classList.add('fas');
                        button.classList.add('text-red-500');
                    } else {
                        icon.classList.remove('fas');
                        icon.classList.add('far');
                        button.classList.remove('text-red-500');
                    }
                }
            } catch (error) {
                console.error('Erro ao atualizar favorito:', error);
            }
        });
    });
};

// Busca com debounce
const initSearch = () => {
    const searchInput = document.querySelector('#search-input');
    let debounceTimer;
    
    if (searchInput) {
        searchInput.addEventListener('input', e => {
            clearTimeout(debounceTimer);
            
            debounceTimer = setTimeout(async () => {
                const query = e.target.value;
                
                if (query.length >= 2) {
                    try {
                        const response = await fetch(`/api/series/search/?q=${encodeURIComponent(query)}`);
                        const data = await response.json();
                        
                        updateSearchResults(data.results);
                    } catch (error) {
                        console.error('Erro na busca:', error);
                    }
                }
            }, 300);
        });
    }
};

// Lazy loading de imagens
const initLazyLoading = () => {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
};

// Gerenciamento de formulários
const initForms = () => {
    const forms = document.querySelectorAll('form[data-ajax]');
    
    forms.forEach(form => {
        form.addEventListener('submit', async e => {
            e.preventDefault();
            
            const submitButton = form.querySelector('[type="submit"]');
            const originalText = submitButton.textContent;
            submitButton.disabled = true;
            submitButton.textContent = 'Enviando...';
            
            try {
                const formData = new FormData(form);
                const response = await fetch(form.action, {
                    method: form.method,
                    body: formData,
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken')
                    }
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    showNotification(data.message, 'success');
                    if (data.redirect) {
                        window.location.href = data.redirect;
                    }
                } else {
                    showNotification(data.message || 'Erro ao processar requisição', 'error');
                }
            } catch (error) {
                console.error('Erro no envio do formulário:', error);
                showNotification('Erro ao processar requisição', 'error');
            } finally {
                submitButton.disabled = false;
                submitButton.textContent = originalText;
            }
        });
    });
};

// Utilidades
const getCookie = name => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

const showNotification = (message, type = 'info') => {
    const container = document.createElement('div');
    container.className = `alert alert-${type} animate-fade-in fixed top-4 right-4 z-50`;
    container.textContent = message;
    
    document.body.appendChild(container);
    
    setTimeout(() => {
        container.classList.add('opacity-0');
        setTimeout(() => container.remove(), 500);
    }, 5000);
};

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    initNotifications();
    initModals();
    initRatingSystem();
    initFavorites();
    initSearch();
    initLazyLoading();
    initForms();
});