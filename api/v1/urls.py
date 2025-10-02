from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .endpoints import users as user_views
from .endpoints import series as series_views

# Configuração do router
router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='user')
router.register(r'series', series_views.SeriesViewSet, basename='serie')

app_name = 'api_v1'

urlpatterns = [
    # Rotas do router
    path('', include(router.urls)),

    # Rotas do perfil
    path('users/profile/', user_views.ProfileAPIView.as_view(), name='user-profile'),
    path('users/profile/avatar/', user_views.AvatarAPIView.as_view(), name='user-avatar'),

    # Outras rotas personalizadas podem ser adicionadas aqui
]
