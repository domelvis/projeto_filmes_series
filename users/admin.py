from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, UserProfile, UserActivity


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
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('profile_image', 'bio', 'birth_date', 'website', 'email_notifications')}),
    )


admin.site.register(CustomUser, UserAdmin)


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    """
    Configuração do admin para UserActivity.
    """
    list_display = ('user', 'type', 'description', 'created_at')
    list_filter = ('type', 'created_at')
    search_fields = ('user__username', 'description')
    readonly_fields = ('created_at',)
