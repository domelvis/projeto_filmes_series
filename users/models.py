from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """
    Model de usuário personalizado que herda do AbstractUser do Django.
    """
    profile_image = models.ImageField(
        upload_to='users/profile_images/',
        null=True,
        blank=True,
        verbose_name=_('Foto de Perfil')
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name=_('Biografia'),
        help_text=_('Conte um pouco sobre você')
    )
    email_notifications = models.BooleanField(
        default=True,
        verbose_name=_('Notificações por E-mail'),
        help_text=_('Receber notificações por e-mail')
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Data de Nascimento')
    )
    website = models.URLField(
        blank=True,
        verbose_name=_('Website'),
        help_text=_('Seu site pessoal ou blog')
    )

    class Meta:
        verbose_name = _('usuário')
        verbose_name_plural = _('usuários')
        db_table = 'users'

    def __str__(self):
        return self.get_full_name() or self.username

    def get_full_name(self):
        """
        Retorna o nome completo do usuário.
        """
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username

class UserActivity(models.Model):
    """
    Model para registrar atividades do usuário.
    """
    ACTIVITY_TYPES = (
        ('review', _('Review')),
        ('watched', _('Assistido')),
        ('wishlist', _('Lista de Desejos')),
    )

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='activities',
        verbose_name=_('Usuário')
    )
    type = models.CharField(
        max_length=20,
        choices=ACTIVITY_TYPES,
        verbose_name=_('Tipo')
    )
    description = models.CharField(
        max_length=255,
        verbose_name=_('Descrição')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Data de Criação')
    )

    class Meta:
        verbose_name = _('atividade do usuário')
        verbose_name_plural = _('atividades dos usuários')
        db_table = 'user_activities'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.get_type_display()} - {self.created_at}"


class UserProfile(models.Model):
    """
    Model para estender o User padrão do Django com informações adicionais.
    """
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Usuário'
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='Biografia',
        help_text='Conte um pouco sobre você'
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name='Avatar',
        help_text='Sua foto de perfil'
    )
    data_nascimento = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de Nascimento'
    )
    website = models.URLField(
        blank=True,
        verbose_name='Website',
        help_text='Seu site pessoal ou blog'
    )
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação'
    )
    
    class Meta:
        verbose_name = 'Perfil do Usuário'
        verbose_name_plural = 'Perfis dos Usuários'
    
    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    @property
    def nome_completo(self):
        """Retorna o nome completo do usuário."""
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        return self.user.username



