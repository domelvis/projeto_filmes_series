# Função para gerar mensagens de erro
def get_error_messages(form):
    """
    Gera mensagens de erro formatadas a partir de erros de formulário
    Args:
        form: Formulário Django com erros
    Returns:
        dict: Dicionário com mensagens de erro organizadas por campo
    """
    errors = {}
    for field in form:
        if field.errors:
            errors[field.name] = [str(error) for error in field.errors]
    return errors

# Função para validar extensões de arquivo
def validate_file_extension(value, valid_extensions):
    """
    Valida a extensão de um arquivo
    Args:
        value: Arquivo para validar
        valid_extensions: Lista de extensões válidas
    Returns:
        bool: True se válido, False se inválido
    """
    if not value:
        return False
    ext = value.name.split('.')[-1].lower()
    return ext in valid_extensions

# Função para formatar dados de perfil
def format_profile_data(user):
    """
    Formata dados do perfil do usuário para API
    Args:
        user: Instância do modelo User
    Returns:
        dict: Dados do perfil formatados
    """
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'avatar_url': user.profile.avatar.url if user.profile.avatar else None,
        'bio': user.profile.bio,
        'date_joined': user.date_joined.strftime('%Y-%m-%d'),
        'series_watched': user.profile.series_watched.count(),
        'reviews_count': user.reviews.count(),
        'favorite_genres': [genre.name for genre in user.profile.favorite_genres.all()]
    }