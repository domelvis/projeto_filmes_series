from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    Model para estender o User padrão do Django com informações adicionais.
    """
    user = models.OneToOneField(
        User,
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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Cria automaticamente um perfil quando um usuário é criado.
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Salva automaticamente o perfil quando o usuário é salvo.
    """
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
