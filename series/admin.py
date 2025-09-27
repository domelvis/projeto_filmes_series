from django.contrib import admin
from .models import Serie


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o model Serie.
    """
    list_display = ['titulo', 'genero', 'ano', 'criado_por', 'data_criacao']
    list_filter = ['genero', 'ano', 'data_criacao', 'criado_por']
    search_fields = ['titulo', 'descricao']
    readonly_fields = ['data_criacao', 'data_atualizacao']
    list_per_page = 20
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao', 'ano', 'genero')
        }),
        ('Imagem', {
            'fields': ('imagem',)
        }),
        ('Metadados', {
            'fields': ('criado_por', 'data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        """Define o usuário que criou a série."""
        if not change:  # Se é uma nova série
            obj.criado_por = request.user
        super().save_model(request, obj, form, change)
