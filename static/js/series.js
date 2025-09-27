/*
 * SERIES.JS
 * Lógica de JavaScript específica para páginas de Séries (Lista, Detalhe, Formulários).
 */

document.addEventListener('DOMContentLoaded', function() {
    console.log('series.js carregado.');

    // --- 1. Lógica para aplicar filtros na página de lista (list.html) ---
    const filterForm = document.getElementById('series-filter-form');
    
    if (filterForm) {
        const searchInput = document.getElementById('search-input');
        const genreSelect = document.getElementById('genero-select');
        
        // Aplica o filtro quando o usuário muda o gênero
        if (genreSelect) {
            genreSelect.addEventListener('change', function() {
                filterForm.submit();
            });
        }

        // Adiciona funcionalidade de limpar busca
        const clearSearchBtn = document.getElementById('clear-search-btn');
        if (clearSearchBtn && searchInput) {
            clearSearchBtn.addEventListener('click', function() {
                searchInput.value = '';
                filterForm.submit();
            });
        }
    }
    
    // --- 2. Lógica para Avaliações (Rating) na página de detalhes (detail.html) ---
    const ratingContainer = document.getElementById('serie-rating-stars');
    
    if (ratingContainer) {
        const stars = ratingContainer.querySelectorAll('.star');

        stars.forEach(star => {
            star.addEventListener('click', function() {
                const ratingValue = this.dataset.value;
                
                // 💡 Aqui você faria uma chamada AJAX para enviar a avaliação (ratingValue) ao Django
                // Exemplo: fetch('/api/series/' + serieId + '/rate/', { ... })
                
                alert('Sua avaliação de ' + ratingValue + ' estrelas foi registrada! (Funcionalidade AJAX simulada)');
                
                // Atualizar visualmente as estrelas
                stars.forEach(s => {
                    if (parseInt(s.dataset.value) <= parseInt(ratingValue)) {
                        s.classList.add('rated');
                    } else {
                        s.classList.remove('rated');
                    }
                });
            });
        });
    }

});