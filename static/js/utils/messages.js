/**
 * MessageManager - Sistema de mensagens profissional para feedback do usuário
 * 
 * Recursos:
 * - Exibição elegante de mensagens com animações
 * - Diferentes tipos: sucesso, erro, alerta, informação
 * - Auto-remoção com duração configurável
 * - Limite de mensagens simultâneas
 * - Design responsivo e acessível
 */
class MessageManager {
    constructor() {
        // Configurações do sistema
        this.config = {
            duration: 5000,        // Duração padrão de exibição
            maxMessages: 3,        // Máximo de mensagens simultâneas
            position: 'top-right', // Posição na tela
            animations: {
                enter: 300,        // Duração da animação de entrada
                exit: 200         // Duração da animação de saída
            }
        };

        this.setupEventListeners();
        this.setupContainer();
    }

    /**
     * Configura os event listeners globais
     */
    setupEventListeners() {
        document.addEventListener('show-message', (event) => {
            const { type, message, duration } = event.detail;
            this.showMessage(type, message, duration);
        });
    }

    /**
     * Configura o container de mensagens
     */
    setupContainer() {
        this.container = document.querySelector('.messages-container');
        if (!this.container) {
            this.container = document.createElement('div');
            this.container.className = `messages-container messages-${this.config.position}`;
            document.body.appendChild(this.container);
        }
    }

    /**
     * Exibe uma nova mensagem
     * @param {string} type - Tipo da mensagem (success, error, warning, info)
     * @param {string} message - Texto da mensagem
     * @param {number} [duration] - Duração personalizada em ms
     */
    showMessage(type, message, duration = this.config.duration) {
        // Limita o número de mensagens
        while (this.container.children.length >= this.config.maxMessages) {
            this.removeMessage(this.container.firstChild);
        }

        // Cria e adiciona a mensagem
        const messageElement = this.createMessageElement(type, message);
        this.container.appendChild(messageElement);

        // Força reflow para animação
        messageElement.offsetHeight;
        messageElement.classList.add('show');

        // Configura remoção automática
        if (duration > 0) {
            setTimeout(() => this.removeMessage(messageElement), duration);
        }
    }

    /**
     * Cria o elemento HTML da mensagem
     * @param {string} type - Tipo da mensagem
     * @param {string} message - Texto da mensagem
     * @returns {HTMLElement} Elemento da mensagem
     */
    createMessageElement(type, message) {
        const element = document.createElement('div');
        element.className = `message message-${type}`;
        element.setAttribute('role', 'alert');
        
        element.innerHTML = `
            <span class="message-icon" aria-hidden="true">${this.getIcon(type)}</span>
            <div class="message-content">
                <div class="message-title">${this.getTitle(type)}</div>
                <p>${message}</p>
            </div>
            <button type="button" class="message-close" aria-label="Fechar">
                <i class="bi bi-x"></i>
            </button>
        `;

        // Adiciona listeners
        this.setupMessageListeners(element);

        return element;
    }

    /**
     * Configura os listeners da mensagem
     * @param {HTMLElement} element - Elemento da mensagem
     */
    setupMessageListeners(element) {
        // Botão de fechar
        const closeButton = element.querySelector('.message-close');
        closeButton.addEventListener('click', () => this.removeMessage(element));

        // Swipe em dispositivos móveis
        let touchStartX = 0;
        let touchEnd = 0;

        element.addEventListener('touchstart', (e) => {
            touchStartX = e.changedTouches[0].screenX;
        });

        element.addEventListener('touchend', (e) => {
            touchEnd = e.changedTouches[0].screenX;
            if (touchStartX - touchEnd > 50) {
                this.removeMessage(element);
            }
        });
    }

    /**
     * Remove uma mensagem com animação
     * @param {HTMLElement} element - Elemento a ser removido
     */
    removeMessage(element) {
        if (!element || !element.parentNode) return;

        element.classList.remove('show');
        element.classList.add('removing');

        setTimeout(() => {
            if (element.parentNode === this.container) {
                this.container.removeChild(element);
            }
        }, this.config.animations.exit);
    }

    /**
     * Retorna o ícone adequado para o tipo de mensagem
     * @param {string} type - Tipo da mensagem
     * @returns {string} - HTML do ícone
     */
    getIcon(type) {
        const icons = {
            success: '<i class="bi bi-check-circle-fill"></i>',
            error: '<i class="bi bi-x-circle-fill"></i>',
            warning: '<i class="bi bi-exclamation-triangle-fill"></i>',
            info: '<i class="bi bi-info-circle-fill"></i>'
        };
        return icons[type] || icons.info;
    }

    /**
     * Retorna o título adequado para o tipo de mensagem
     * @param {string} type - Tipo da mensagem
     * @returns {string} - Título da mensagem
     */
    getTitle(type) {
        const titles = {
            success: 'Sucesso!',
            error: 'Erro!',
            warning: 'Atenção!',
            info: 'Informação'
        };
        return titles[type] || titles.info;
    }

    /**
     * Métodos de conveniência para diferentes tipos de mensagens
     */
    success(message, duration) {
        this.showMessage('success', message, duration);
    }

    error(message, duration) {
        this.showMessage('error', message, duration);
    }

    warning(message, duration) {
        this.showMessage('warning', message, duration);
    }

    info(message, duration) {
        this.showMessage('info', message, duration);
    }
}

// Inicializa o gerenciador de mensagens globalmente
document.addEventListener('DOMContentLoaded', () => {
    window.messageManager = new MessageManager();
});