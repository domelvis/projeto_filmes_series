/**
 * ProfileManager - Classe responsável pela gestão do perfil do usuário
 * 
 * Esta classe gerencia todas as interações relacionadas ao perfil do usuário:
 * - Carregamento inicial dos dados
 * - Upload de avatar
 * - Atualização de informações
 * - Gestão de estado da UI
 */
class ProfileManager {
    constructor() {
        // Dados do perfil carregados do servidor
        this.profileData = {};
        
        // Estado da UI
        this.uiState = {
            isLoading: false,
            hasError: false,
            errorMessage: '',
            isDirty: false
        };

        // Inicializa o gerenciador
        this.init();
    }

    /**
     * Inicializa o gerenciador de perfil
     * - Carrega dados iniciais
     * - Configura event listeners
     */
    async init() {
        try {
            this.setupEventListeners();
            await this.loadProfileData();
        } catch (error) {
            console.error('Erro na inicialização:', error);
            this.handleError('Não foi possível inicializar o perfil');
        }
    }

    /**
     * Configura todos os event listeners necessários
     */
    setupEventListeners() {
        // Upload de avatar
        const avatarInput = document.getElementById('avatar-upload');
        if (avatarInput) {
            avatarInput.addEventListener('change', this.handleAvatarUpload.bind(this));
        }

        // Formulário de edição
        const editForm = document.getElementById('edit-profile-form');
        if (editForm) {
            editForm.addEventListener('submit', this.handleProfileUpdate.bind(this));
        }

        // Monitor de mudanças para campos editáveis
        document.querySelectorAll('.profile-editable').forEach(field => {
            field.addEventListener('change', () => this.uiState.isDirty = true);
        });
    }

    /**
     * Carrega os dados do perfil do servidor
     */
    async loadProfileData() {
        this.setLoading(true);
        try {
            const response = await this.fetchWithAuth('/api/v1/users/profile/');
            
            if (!response.ok) {
                throw new Error('Falha ao carregar dados do perfil');
            }

            this.profileData = await response.json();
            this.updateUI();
            
        } catch (error) {
            this.handleError('Erro ao carregar dados do perfil');
            throw error;
        } finally {
            this.setLoading(false);
        }
    }

    /**
     * Atualiza toda a interface com os dados do perfil
     */
    updateUI() {
        if (!this.profileData) return;

        // Avatar
        this.updateAvatar();
        
        // Informações básicas
        this.updateBasicInfo();
        
        // Estatísticas
        this.updateStats();
        
        // Status de loading/erro
        this.updateLoadingState();
    }

    /**
     * Atualiza o avatar na interface
     */
    updateAvatar() {
        const avatarContainer = document.querySelector('.profile-avatar');
        const avatarPlaceholder = document.querySelector('.avatar-placeholder');
        
        if (this.profileData.avatar_url) {
            if (avatarContainer) {
                const img = avatarContainer.querySelector('img');
                if (img) {
                    img.src = this.profileData.avatar_url;
                }
            }
            if (avatarPlaceholder) {
                avatarPlaceholder.style.display = 'none';
            }
        } else {
            if (avatarContainer) {
                avatarContainer.style.display = 'none';
            }
            if (avatarPlaceholder) {
                avatarPlaceholder.style.display = 'flex';
            }
        }
    }

    /**
     * Atualiza informações básicas do perfil
     */
    updateBasicInfo() {
        const selectors = {
            username: '.profile-username',
            fullName: '.profile-fullname',
            bio: '.profile-bio',
            email: '.profile-email'
        };

        for (const [key, selector] of Object.entries(selectors)) {
            const element = document.querySelector(selector);
            if (element && this.profileData[key]) {
                element.textContent = this.profileData[key];
            }
        }
    }

    /**
     * Atualiza as estatísticas do perfil
     */
    updateStats() {
        const stats = {
            series_watched: document.getElementById('series-watched'),
            reviews_count: document.getElementById('reviews-count'),
            favorite_genres: document.getElementById('favorite-genres')
        };

        for (const [key, element] of Object.entries(stats)) {
            if (element && this.profileData[key] !== undefined) {
                element.textContent = this.profileData[key];
            }
        }
    }

    /**
     * Atualiza o estado de loading na interface
     */
    updateLoadingState() {
        const loadingIndicator = document.querySelector('.profile-loading');
        const errorMessage = document.querySelector('.profile-error');
        
        if (loadingIndicator) {
            loadingIndicator.style.display = this.uiState.isLoading ? 'block' : 'none';
        }
        
        if (errorMessage) {
            errorMessage.style.display = this.uiState.hasError ? 'block' : 'none';
            if (this.uiState.hasError) {
                errorMessage.textContent = this.uiState.errorMessage;
            }
        }
    }

    /**
     * Manipula o upload de avatar
     * @param {Event} event - Evento do input file
     */
    async handleAvatarUpload(event) {
        const file = event.target.files[0];
        if (!file) return;

        // Valida o arquivo
        if (!this.validateAvatarFile(file)) {
            return;
        }

        this.setLoading(true);
        const formData = new FormData();
        formData.append('avatar', file);

        try {
            const response = await this.fetchWithAuth('/api/v1/users/profile/avatar/', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error('Falha ao atualizar avatar');
            }

            const data = await response.json();
            this.profileData.avatar_url = data.avatar_url;
            this.updateAvatar();
            this.showSuccess('Avatar atualizado com sucesso');
            
        } catch (error) {
            this.handleError('Erro ao atualizar avatar');
        } finally {
            this.setLoading(false);
        }
    }

    /**
     * Valida o arquivo de avatar
     * @param {File} file - Arquivo a ser validado
     * @returns {boolean} - Indica se o arquivo é válido
     */
    validateAvatarFile(file) {
        // Tamanho máximo: 5MB
        const maxSize = 5 * 1024 * 1024;
        if (file.size > maxSize) {
            this.showError('O arquivo deve ter no máximo 5MB');
            return false;
        }

        // Tipos permitidos
        const allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
        if (!allowedTypes.includes(file.type)) {
            this.showError('Formato de arquivo não suportado. Use JPG, PNG ou GIF');
            return false;
        }

        return true;
    }

    /**
     * Manipula a atualização do perfil
     * @param {Event} event - Evento do formulário
     */
    async handleProfileUpdate(event) {
        event.preventDefault();
        
        if (!this.uiState.isDirty) {
            return;
        }

        this.setLoading(true);
        const form = event.target;
        const formData = new FormData(form);

        try {
            const response = await this.fetchWithAuth('/api/v1/users/profile/', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error('Falha ao atualizar perfil');
            }

            this.profileData = await response.json();
            this.updateUI();
            this.uiState.isDirty = false;
            this.showSuccess('Perfil atualizado com sucesso');
            
        } catch (error) {
            this.handleError('Erro ao atualizar perfil');
        } finally {
            this.setLoading(false);
        }
    }

    /**
     * Realiza uma requisição autenticada
     * @param {string} url - URL da requisição
     * @param {object} options - Opções da requisição
     * @returns {Promise<Response>} - Response da requisição
     */
    async fetchWithAuth(url, options = {}) {
        const defaultOptions = {
            headers: {
                'X-CSRFToken': this.getCsrfToken()
            }
        };

        return fetch(url, { ...defaultOptions, ...options });
    }

    /**
     * Obtém o token CSRF do cookie
     * @returns {string} Token CSRF
     */
    getCsrfToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
    }

    /**
     * Define o estado de loading
     * @param {boolean} isLoading - Estado de loading
     */
    setLoading(isLoading) {
        this.uiState.isLoading = isLoading;
        this.updateLoadingState();
    }

    /**
     * Manipula erros globalmente
     * @param {string} message - Mensagem de erro
     */
    handleError(message) {
        this.uiState.hasError = true;
        this.uiState.errorMessage = message;
        this.updateLoadingState();
        this.showError(message);
    }

    /**
     * Exibe mensagem de sucesso
     * @param {string} message - Mensagem de sucesso
     */
    showSuccess(message) {
        const event = new CustomEvent('show-message', {
            detail: {
                type: 'success',
                message: message
            }
        });
        document.dispatchEvent(event);
    }

    /**
     * Exibe mensagem de erro
     * @param {string} message - Mensagem de erro
     */
    showError(message) {
        const event = new CustomEvent('show-message', {
            detail: {
                type: 'error',
                message: message
            }
        });
        document.dispatchEvent(event);
    }
}

// Inicializa o gerenciador quando o documento estiver pronto
document.addEventListener('DOMContentLoaded', () => {
    window.profileManager = new ProfileManager();
});