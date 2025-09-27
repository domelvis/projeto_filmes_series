from django.shortcuts import render

def home(request):
    \"\"\"
    Página inicial simplificada
    \"\"\"
    # Contexto vazio ou apenas com dados básicos
    context = {
        'page_title': 'Séries TV - Plataforma Completa'
    }
    return render(request, 'series/index.html', context)
