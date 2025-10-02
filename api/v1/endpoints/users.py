"""
Views da API do módulo users
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status, views, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from .serializers.users import (
    UserProfileSerializer,
    UserAvatarSerializer,
    UserRegistrationSerializer,
    UserSerializer,
    UserUpdateSerializer,
    ChangePasswordSerializer
)
from ..users.utils import format_profile_data

User = get_user_model()

class UserViewSet(ModelViewSet):
    """
    ViewSet para gerenciar usuários.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        """Retorna o serializer apropriado para cada ação"""
        if self.action == 'create':
            return UserRegistrationSerializer
        elif self.action in ['update', 'partial_update']:
            return UserUpdateSerializer
        return UserSerializer
    
    def get_permissions(self):
        """Define permissões específicas para cada ação"""
        if self.action in ['update', 'partial_update', 'change_password']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        """Retorna informações do usuário atual"""
        if not request.user.is_authenticated:
            return Response(
                {'detail': 'Autenticação necessária.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def change_password(self, request):
        """Altera a senha do usuário atual"""
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            
            return Response({
                'detail': 'Senha alterada com sucesso.'
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(views.APIView):
    """
    View da API para gerenciar perfil do usuário
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        """
        Retorna dados do perfil do usuário
        """
        user_data = format_profile_data(request.user)
        return Response(user_data)
    
    def post(self, request):
        """
        Atualiza dados do perfil do usuário
        """
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            user_data = format_profile_data(request.user)
            return Response(user_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AvatarAPIView(views.APIView):
    """
    View da API para gerenciar avatar do usuário
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        """
        Atualiza avatar do usuário
        """
        serializer = UserAvatarSerializer(request.user.profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'avatar_url': request.user.profile.avatar.url
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_permissions(self):
        """Define permissões específicas para cada ação"""
        if self.action in ['update', 'partial_update']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        """Retorna o perfil do usuário atual"""
        if not request.user.is_authenticated:
            return Response(
                {'detail': 'Autenticação necessária.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        try:
            profile = request.user.userprofile
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            # Cria o perfil se não existir
            profile = UserProfile.objects.create(user=request.user)
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def update_me(self, request):
        """Atualiza o perfil do usuário atual"""
        if not request.user.is_authenticated:
            return Response(
                {'detail': 'Autenticação necessária.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        try:
            profile = request.user.userprofile
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(user=request.user)
        
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthView(APIView):
    """
    View para autenticação de usuários.
    """
    
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        """Autentica um usuário e retorna tokens JWT"""
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response(
                {'detail': 'Username e password são obrigatórios.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        else:
            return Response(
                {'detail': 'Credenciais inválidas.'},
                status=status.HTTP_401_UNAUTHORIZED
            )


class RegisterView(APIView):
    """
    View para registro de novos usuários.
    """
    
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        """Registra um novo usuário"""
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

