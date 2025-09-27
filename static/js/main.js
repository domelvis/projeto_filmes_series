/* ========================================
   SÉRIES TV - JAVASCRIPT PRINCIPAL
   Funcionalidades interativas e UX
   ======================================== */

// ===== INICIALIZAÇÃO =====
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    // Inicializar componentes
    initTooltips();
    initAnimations();
    initFormValidation();
    initImagePreview();
    initPasswordToggle();
    initSmoothScrolling();
    initLoadingStates();
    initThemeToggle();
    
    // Adicionar classes de animação
    addAnimationClasses();
    
    console.log('Séries TV - Aplicação inicializada com sucesso!');
}

// ===== TOOLTIPS =====
function initTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// ===== ANIMAÇÕES =====
function initAnimations() {
    // Intersection Observer para animações de entrada
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observar elementos para animação
    const animateElements = document.querySelectorAll('.card, .series-card, .profile-section');
    animateElements.forEach(el => {
        observer.observe(el);
    });
}

function addAnimationClasses() {
    // Adicionar classes de animação com delay
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });
}

// ===== VALIDAÇÃO DE FORMULÁRIOS =====
function initFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
                e.stopPropagation();
            }
            
            this.classList.add('was-validated');
        });
        
        // Validação em tempo real
        const inputs = form.querySelectorAll('input, textarea, select');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                validateField(this);
            });
            
            input.addEventListener('input', function() {
                if (this.classList.contains('is-invalid')) {
                    validateField(this);
                }
            });
        });
    });
}

function validateForm(form) {
    let isValid = true;
    const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
    
    inputs.forEach(input => {
        if (!validateField(input)) {
            isValid = false;
        }
    });
    
    return isValid;
}

function validateField(field) {
    const value = field.value.trim();
    const type = field.type;
    const required = field.hasAttribute('required');
    let isValid = true;
    let message = '';
    
    // Validação de campo obrigatório
    if (required && !value) {
        isValid = false;
        message = 'Este campo é obrigatório.';
    }
    
    // Validações específicas por tipo
    if (value && type === 'email') {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            message = 'Por favor, insira um email válido.';
        }
    }
    
    if (value && type === 'password') {
        if (value.length < 8) {
            isValid = false;
            message = 'A senha deve ter pelo menos 8 caracteres.';
        }
    }
    
    if (value && field.name === 'password2') {
        const password1 = document.querySelector('input[name="password1"]');
        if (password1 && value !== password1.value) {
            isValid = false;
            message = 'As senhas não coincidem.';
        }
    }
    
    if (value && field.name === 'username') {
        if (value.length < 3) {
            isValid = false;
            message = 'O nome de usuário deve ter pelo menos 3 caracteres.';
        }
    }
    
    // Aplicar validação visual
    if (isValid) {
        field.classList.remove('is-invalid');
        field.classList.add('is-valid');
        removeFieldError(field);
    } else {
        field.classList.remove('is-valid');
        field.classList.add('is-invalid');
        showFieldError(field, message);
    }
    
    return isValid;
}

function showFieldError(field, message) {
    removeFieldError(field);
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    
    field.parentNode.appendChild(errorDiv);
}

function removeFieldError(field) {
    const existingError = field.parentNode.querySelector('.invalid-feedback');
    if (existingError) {
        existingError.remove();
    }
}

// ===== PREVIEW DE IMAGENS =====
function initImagePreview() {
    const imageInputs = document.querySelectorAll('input[type="file"][accept*="image"]');
    
    imageInputs.forEach(input => {
        input.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    showImagePreview(input, e.target.result);
                };
                reader.readAsDataURL(file);
            }
        });
    });
}

function showImagePreview(input, imageSrc) {
    const previewId = input.id + 'Preview';
    let preview = document.getElementById(previewId);
    
    if (!preview) {
        preview = document.createElement('div');
        preview.id = previewId;
        preview.className = 'image-preview mt-3';
        preview.innerHTML = `
            <label class="form-label">Pré-visualização:</label>
            <div class="text-center">
                <img src="${imageSrc}" class="img-thumbnail" style="max-width: 200px; max-height: 200px;" alt="Pré-visualização">
            </div>
        `;
        input.parentNode.appendChild(preview);
    } else {
        const img = preview.querySelector('img');
        if (img) {
            img.src = imageSrc;
        }
    }
    
    preview.style.display = 'block';
}

// ===== TOGGLE DE SENHA =====
function initPasswordToggle() {
    const toggleButtons = document.querySelectorAll('.password-toggle-btn, [id^="togglePassword"]');
    
    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target') || 
                           this.id.replace('toggle', '').replace('Password', '');
            const passwordField = document.getElementById(targetId);
            const icon = this.querySelector('i');
            
            if (passwordField && icon) {
                if (passwordField.type === 'password') {
                    passwordField.type = 'text';
                    icon.className = 'bi bi-eye-slash';
                } else {
                    passwordField.type = 'password';
                    icon.className = 'bi bi-eye';
                }
            }
        });
    });
}

// ===== SCROLL SUAVE =====
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// ===== ESTADOS DE LOADING =====
function initLoadingStates() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                showLoadingState(submitBtn);
            }
        });
    });
}

function showLoadingState(button) {
    const originalText = button.innerHTML;
    button.innerHTML = '<i class="bi bi-hourglass-split me-2"></i>Carregando...';
    button.disabled = true;
    button.classList.add('loading');
    
    // Restaurar após 3 segundos (fallback)
    setTimeout(() => {
        button.innerHTML = originalText;
        button.disabled = false;
        button.classList.remove('loading');
    }, 3000);
}

function hideLoadingState(button, originalText) {
    button.innerHTML = originalText;
    button.disabled = false;
    button.classList.remove('loading');
}

// ===== TOGGLE DE TEMA =====
function initThemeToggle() {
    // Verificar preferência salva
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.documentElement.setAttribute('data-theme', savedTheme);
    }
    
    // Criar botão de toggle se não existir
    if (!document.querySelector('.theme-toggle')) {
        createThemeToggle();
    }
}

function createThemeToggle() {
    const navbar = document.querySelector('.navbar .navbar-nav');
    if (navbar) {
        const themeToggle = document.createElement('li');
        themeToggle.className = 'nav-item theme-toggle';
        themeToggle.innerHTML = `
            <button class="btn btn-link nav-link" onclick="toggleTheme()" title="Alternar tema">
                <i class="bi bi-sun" id="theme-icon"></i>
            </button>
        `;
        navbar.appendChild(themeToggle);
    }
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    const icon = document.getElementById('theme-icon');
    if (icon) {
        icon.className = newTheme === 'dark' ? 'bi bi-moon' : 'bi bi-sun';
    }
}

// ===== FUNÇÕES UTILITÁRIAS =====
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// ===== NOTIFICAÇÕES =====
function showNotification(message, type = 'info', duration = 3000) {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = `
        top: 100px;
        right: 20px;
        z-index: 9999;
        min-width: 300px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    `;
    
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto-remover após duração especificada
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, duration);
}

// ===== CONFIRMAÇÃO DE AÇÕES =====
function confirmAction(message, callback) {
    if (confirm(message)) {
        callback();
    }
}

// ===== COPIAR PARA CLIPBOARD =====
function copyToClipboard(text) {
    if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(() => {
            showNotification('Copiado para a área de transferência!', 'success');
        }).catch(() => {
            fallbackCopyToClipboard(text);
        });
    } else {
        fallbackCopyToClipboard(text);
    }
}

function fallbackCopyToClipboard(text) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    textArea.style.top = '-999999px';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    
    try {
        document.execCommand('copy');
        showNotification('Copiado para a área de transferência!', 'success');
    } catch (err) {
        showNotification('Erro ao copiar texto', 'danger');
    }
    
    document.body.removeChild(textArea);
}

// ===== FUNÇÕES ESPECÍFICAS PARA SÉRIES =====
function shareSerie(title, url) {
    if (navigator.share) {
        navigator.share({
            title: title,
            text: `Confira esta série: ${title}`,
            url: url
        }).catch(err => {
            console.log('Erro ao compartilhar:', err);
            copyToClipboard(url);
        });
    } else {
        copyToClipboard(url);
    }
}

function toggleFavorite(serieId) {
    // Implementar funcionalidade de favoritos
    console.log('Toggle favorite:', serieId);
}

// ===== FUNÇÕES ESPECÍFICAS PARA USUÁRIOS =====
function updateProfileStats() {
    // Atualizar estatísticas do perfil
    const stats = document.querySelectorAll('.profile-stat-value');
    stats.forEach(stat => {
        const finalValue = parseInt(stat.textContent);
        animateCounter(stat, 0, finalValue, 1000);
    });
}

function animateCounter(element, start, end, duration) {
    const startTime = performance.now();
    
    function updateCounter(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const current = Math.floor(start + (end - start) * progress);
        
        element.textContent = current;
        
        if (progress < 1) {
            requestAnimationFrame(updateCounter);
        }
    }
    
    requestAnimationFrame(updateCounter);
}

// ===== EVENT LISTENERS GLOBAIS =====
document.addEventListener('click', function(e) {
    // Fechar dropdowns ao clicar fora
    if (!e.target.closest('.dropdown')) {
        const openDropdowns = document.querySelectorAll('.dropdown-menu.show');
        openDropdowns.forEach(dropdown => {
            dropdown.classList.remove('show');
        });
    }
});

// ===== PERFORMANCE =====
// Lazy loading para imagens
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// ===== EXPORTAR FUNÇÕES GLOBAIS =====
window.SeriesTV = {
    showNotification,
    confirmAction,
    copyToClipboard,
    shareSerie,
    toggleFavorite,
    updateProfileStats,
    toggleTheme
};

