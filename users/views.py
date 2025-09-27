from django.http import HttpResponse

def login_view(request):
    return HttpResponse('Pagina de Login')

def logout_view(request):
    return HttpResponse('Logout realizado')

def register_view(request):
    return HttpResponse('Pagina de Registro')
