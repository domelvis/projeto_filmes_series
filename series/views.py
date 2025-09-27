from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'series/index.html')

def serie_list(request):
    return HttpResponse('Lista de Series')

def serie_detail(request, pk):
    return HttpResponse(f'Detalhes da Serie {pk}')
