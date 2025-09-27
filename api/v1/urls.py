from django.urls import path
from . import views

app_name = 'api_v1'

urlpatterns = [
    path('series/', views.serie_list, name='series-list'),
    path('series/<int:pk>/', views.serie_detail, name='series-detail'),
]
