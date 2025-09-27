from django.shortcuts import render

def home(request):
    \"\"\"
    P�gina inicial simplificada
    \"\"\"
    # Contexto vazio ou apenas com dados b�sicos
    context = {
        'page_title': 'S�ries TV - Plataforma Completa'
    }
    return render(request, 'series/index.html', context)
