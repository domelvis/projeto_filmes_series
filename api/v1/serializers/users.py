"""
Serializers para o módulo de usuários
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import Profile

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer para atualização do perfil do usuário
    """
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    bio = serializers.CharField(required=False, allow_blank=True)
    favorite_genres = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'bio', 'favorite_genres')

    def validate_email(self, value):
        """
        Valida se o email já está em uso
        """
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError("Este email já está em uso.")
        return value

    def update(self, instance, validated_data):
        """
        Atualiza os dados do usuário e do perfil
        """
        # Atualiza dados do usuário
        for attr in ('first_name', 'last_name', 'email'):
            if attr in validated_data:
                setattr(instance, attr, validated_data[attr])
        instance.save()

        # Atualiza dados do perfil
        profile_data = {}
        if 'bio' in validated_data:
            profile_data['bio'] = validated_data['bio']
        if 'favorite_genres' in validated_data:
            profile_data['favorite_genres'] = validated_data['favorite_genres']

        if profile_data:
            Profile.objects.filter(user=instance).update(**profile_data)

        return instance


class UserAvatarSerializer(serializers.ModelSerializer):
    """
    Serializer para atualização do avatar do usuário
    """
    avatar = serializers.ImageField(required=True)

    class Meta:
        model = Profile
        fields = ('avatar',)

    def validate_avatar(self, value):
        """
        Valida o arquivo de avatar
        """
        if value.size > 5242880:  # 5MB
            raise serializers.ValidationError(
                "O tamanho máximo permitido é 5MB."
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
        fields = ['username', 'email', 'password', 'password_confirm', 'first_name', 'last_name']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Senhas não conferem."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """Serializer para atualização de usuários"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ChangePasswordSerializer(serializers.Serializer):
    """Serializer para alteração de senha"""
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=8)
    new_password_confirm = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError({"new_password": "Senhas não conferem."})
        
        user = self.context['request'].user
        if not user.check_password(attrs['old_password']):
            raise serializers.ValidationError({"old_password": "Senha atual incorreta."})
        
        return attrs
    
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

