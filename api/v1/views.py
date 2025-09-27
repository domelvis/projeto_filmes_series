from django.http import JsonResponse

def serie_list(request):
    return JsonResponse({'message': 'API V1 Series List'})

def serie_detail(request, pk):
    return JsonResponse({'message': f'API V1 Series Detail {pk}'})
