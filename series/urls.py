from django.urls import path
from . import views

app_name = 'series'

urlpatterns = [
    path('', views.home, name='home'),
    path('series/', views.serie_list, name='list'),
    path('series/<int:pk>/', views.serie_detail, name='detail'),
]
