from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    """
    Inline admin para o UserProfile.
    """
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Perfil'


class UserAdmin(BaseUserAdmin):
    """
    Estende o UserAdmin padrão para incluir o UserProfile.
    """
    inlines = (UserProfileInline,)


# Re-registra o UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o UserProfile.
    """
    list_display = ['user', 'nome_completo', 'data_criacao']
    list_filter = ['data_criacao']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'bio']
    readonly_fields = ['data_criacao']
    
    fieldsets = (
        ('Informações do Usuário', {
            'fields': ('user',)
        }),
        ('Informações Pessoais', {
            'fields': ('bio', 'avatar', 'data_nascimento', 'website')
        }),
        ('Metadados', {
            'fields': ('data_criacao',),
            'classes': ('collapse',)
        }),
    )
