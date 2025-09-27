/*
 * USERS.JS
 * Lógica de JavaScript específica para páginas de Usuário (Login, Registro, Perfil).
 */

document.addEventListener('DOMContentLoaded', function() {
    console.log('users.js carregado.');
    
    // --- 1. Lógica para alternar o formulário de edição de perfil ---
    const editProfileButton = document.getElementById('edit-profile-btn');
    const profileView = document.getElementById('profile-view');
    const profileEditForm = document.getElementById('profile-edit-form');

    if (editProfileButton && profileView && profileEditForm) {
        editProfileButton.addEventListener('click', function() {
            // Esconde a visualização e mostra o formulário
            profileView.style.display = 'none';
            profileEditForm.style.display = 'block';
        });

        // Adiciona um botão de 'Cancelar' no formulário de edição (se você tiver um)
        const cancelButton = profileEditForm.querySelector('.btn-cancel');
        if (cancelButton) {
             cancelButton.addEventListener('click', function(e) {
                e.preventDefault(); // Impede o envio do formulário
                profileView.style.display = 'block';
                profileEditForm.style.display = 'none';
            });
        }
    }
    
    // --- 2. Validação de Formulário de Login/Registro ---
    const authForms = document.querySelectorAll('#login-form, #register-form');
    
    authForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const passwordField = form.querySelector('input[type="password"]');
            
            // Exemplo de validação simples: verifica se a senha tem pelo menos 6 caracteres
            if (passwordField && passwordField.value.length < 6) {
                e.preventDefault();
                alert('A senha deve ter pelo menos 6 caracteres.');
                passwordField.focus();
            }
            
            // Adicione outras validações (email, confirmação de senha, etc.) aqui
        });
    });

});