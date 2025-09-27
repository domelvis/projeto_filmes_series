from django.http import JsonResponse

def serie_list(request):
    return JsonResponse({'message': 'API Series List'})

def serie_detail(request, pk):
    return JsonResponse({'message': f'API Series Detail {pk}'})
