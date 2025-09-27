# models.py
from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    icon_url = models.URLField(max_length=500, blank=True, null=True)
    color_hex = models.CharField(max_length=7, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Content(models.Model):
    CONTENT_TYPES = [
        ('movie', 'Filme'),
        ('series', 'Série'),
        ('documentary', 'Documentário'),
        ('special', 'Especial'),
    ]
    
    STATUS_CHOICES = [
        ('draft', 'Rascunho'),
        ('published', 'Publicado'),
        ('archived', 'Arquivado'),
    ]
    
    content_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.TextField(blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    
    # Metadados principais
    release_date = models.DateField(blank=True, null=True)
    duration_minutes = models.IntegerField(blank=True, null=True)
    age_rating = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    
    # Mídia
    poster_url = models.URLField(max_length=500, blank=True, null=True)
    backdrop_url = models.URLField(max_length=500, blank=True, null=True)
    trailer_url = models.URLField(max_length=500, blank=True, null=True)
    preview_url = models.URLField(max_length=500, blank=True, null=True)
    
    # Estatísticas
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    rotten_tomatoes_rating = models.IntegerField(blank=True, null=True)
    popularity_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    # Controle
    is_featured = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='published')
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    genres = models.ManyToManyField(Genre, through='ContentGenre')
    
    def __str__(self):
        return self.title

class ContentGenre(models.Model):
    content_genre_id = models.AutoField(primary_key=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['content', 'genre']

class Season(models.Model):
    season_id = models.AutoField(primary_key=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    season_number = models.IntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    poster_url = models.URLField(max_length=500, blank=True, null=True)
    
    episode_count = models.IntegerField(default=0)
    total_duration_minutes = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['content', 'season_number']

class Episode(models.Model):
    episode_id = models.AutoField(primary_key=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    episode_number = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration_minutes = models.IntegerField()
    release_date = models.DateField(blank=True, null=True)
    
    video_url_1080p = models.URLField(max_length=500, blank=True, null=True)
    video_url_720p = models.URLField(max_length=500, blank=True, null=True)
    video_url_480p = models.URLField(max_length=500, blank=True, null=True)
    thumbnail_url = models.URLField(max_length=500, blank=True, null=True)
    subtitle_url = models.URLField(max_length=500, blank=True, null=True)
    
    file_size_mb = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    video_codec = models.CharField(max_length=20, blank=True, null=True)
    audio_codec = models.CharField(max_length=20, blank=True, null=True)
    resolution = models.CharField(max_length=20, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['season', 'episode_number']