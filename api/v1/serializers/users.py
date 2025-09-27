from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer para o perfil do usuário"""
    
    avatar_url = serializers.SerializerMethodField()
    user_username = serializers.CharField(source='user.username', read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_first_name = serializers.CharField(source='user.first_name', read_only=True)
    user_last_name = serializers.CharField(source='user.last_name', read_only=True)
    user_date_joined = serializers.DateTimeField(source='user.date_joined', read_only=True)
    user_last_login = serializers.DateTimeField(source='user.last_login', read_only=True)
    
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user',
            'user_username',
            'user_email',
            'user_first_name',
            'user_last_name',
            'user_date_joined',
            'user_last_login',
            'bio',
            'avatar',
            'avatar_url',
            'data_nascimento',
            'website',
        ]
        read_only_fields = ['id', 'user']
    
    def get_avatar_url(self, obj):
        """Retorna a URL do avatar se existir"""
        if obj.avatar:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.avatar.url)
            return obj.avatar.url
        return None
    
    def validate_avatar(self, value):
        """Validação do avatar"""
        if value:
            # Verifica o tamanho do arquivo (5MB)
            max_size = 5 * 1024 * 1024  # 5MB
            if value.size > max_size:
                raise serializers.ValidationError("O avatar deve ter no máximo 5MB.")
            
            # Verifica a extensão
            allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
            file_extension = value.name.split('.')[-1].lower()
            if file_extension not in allowed_extensions:
                raise serializers.ValidationError(
                    f"Extensões permitidas: {', '.join(allowed_extensions)}"
                )
        
        return value


class UserSerializer(serializers.ModelSerializer):
    """Serializer para o modelo User"""
    
    profile = UserProfileSerializer(read_only=True)
    series_count = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'last_login',
            'profile',
            'series_count',
        ]
        read_only_fields = ['id', 'date_joined', 'last_login']
    
    def get_series_count(self, obj):
        """Retorna o número de séries criadas pelo usuário"""
        return obj.serie_set.count()


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer para registro de usuários"""
    
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password_confirm',
        ]
    
    def validate(self, attrs):
        """Validação dos dados"""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("As senhas não coincidem.")
        return attrs
    
    def validate_username(self, value):
        """Validação do nome de usuário"""
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Este nome de usuário já está em uso.")
        return value
    
    def validate_email(self, value):
        """Validação do email"""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email já está em uso.")
        return value
    
    def create(self, validated_data):
        """Cria um novo usuário"""
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        
        user = User.objects.create_user(
            password=password,
            **validated_data
        )
        
        # Cria o perfil do usuário
        UserProfile.objects.create(user=user)
        
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """Serializer para atualização de usuários"""
    
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
        ]
    
    def validate_email(self, value):
        """Validação do email"""
        # Verifica se o email já está em uso por outro usuário
        if User.objects.filter(email=value).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError("Este email já está em uso.")
        return value


class ChangePasswordSerializer(serializers.Serializer):
    """Serializer para mudança de senha"""
    
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=8)
    new_password_confirm = serializers.CharField(required=True)
    
    def validate(self, attrs):
        """Validação dos dados"""
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError("As novas senhas não coincidem.")
        return attrs
    
    def validate_old_password(self, value):
        """Validação da senha atual"""
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("A senha atual está incorreta.")
        return value

