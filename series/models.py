from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Serie(models.Model):
    """
    Model para representar uma série de TV ou streaming.
    """
    GENERO_CHOICES = [
        ('acao', 'Ação'),
        ('aventura', 'Aventura'),
        ('comedia', 'Comédia'),
        ('drama', 'Drama'),
        ('fantasia', 'Fantasia'),
        ('ficcao', 'Ficção Científica'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('suspense', 'Suspense'),
        ('terror', 'Terror'),
        ('thriller', 'Thriller'),
        ('documentario', 'Documentário'),
        ('animacao', 'Animação'),
        ('outros', 'Outros'),
    ]
    
    titulo = models.CharField(
        max_length=200,
        verbose_name='Título',
        help_text='Título da série'
    )
    descricao = models.TextField(
        verbose_name='Descrição',
        help_text='Descrição da série'
    )
    ano = models.PositiveIntegerField(
        verbose_name='Ano de Lançamento',
        help_text='Ano em que a série foi lançada'
    )
    genero = models.CharField(
        max_length=20,
        choices=GENERO_CHOICES,
        verbose_name='Gênero',
        help_text='Gênero da série'
    )
    imagem = models.ImageField(
        upload_to='series/',
        verbose_name='Imagem',
        help_text='Imagem da série',
        blank=True,
        null=True
    )
    criado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Criado por',
        help_text='Usuário que criou a série'
    )
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação'
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de Atualização'
    )
    
    class Meta:
        verbose_name = 'Série'
        verbose_name_plural = 'Séries'
        ordering = ['-data_criacao']
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        """Retorna a URL para visualizar os detalhes da série."""
        return reverse('series:detail', kwargs={'pk': self.pk})
    
    def get_genero_display_color(self):
        """Retorna uma cor CSS baseada no gênero para estilização."""
        cores = {
            'acao': 'danger',
            'aventura': 'warning',
            'comedia': 'success',
            'drama': 'primary',
            'fantasia': 'info',
            'ficcao': 'secondary',
            'horror': 'dark',
            'romance': 'pink',
            'suspense': 'purple',
            'terror': 'dark',
            'thriller': 'indigo',
            'documentario': 'teal',
            'animacao': 'orange',
            'outros': 'gray',
        }
        return cores.get(self.genero, 'secondary')
