from rest_framework import serializers
from series.models import Serie
from users.models import UserProfile


class SerieSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Serie"""
    
    # Campos calculados
    criado_por_username = serializers.CharField(source='criado_por.username', read_only=True)
    genero_display = serializers.CharField(source='get_genero_display', read_only=True)
    genero_color = serializers.CharField(source='get_genero_display_color', read_only=True)
    
    # Campos de imagem
    imagem_url = serializers.SerializerMethodField()
    imagem_thumbnail = serializers.SerializerMethodField()
    
    class Meta:
        model = Serie
        fields = [
            'id',
            'titulo',
            'descricao',
            'ano',
            'genero',
            'genero_display',
            'genero_color',
            'imagem',
            'imagem_url',
            'imagem_thumbnail',
            'criado_por',
            'criado_por_username',
            'data_criacao',
            'data_atualizacao',
        ]
        read_only_fields = ['id', 'criado_por', 'data_criacao', 'data_atualizacao']
    
    def get_imagem_url(self, obj):
        """Retorna a URL da imagem se existir"""
        if obj.imagem:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.imagem.url)
            return obj.imagem.url
        return None
    
    def get_imagem_thumbnail(self, obj):
        """Retorna uma versão thumbnail da imagem"""
        if obj.imagem:
            # Aqui você pode implementar lógica para gerar thumbnails
            # Por enquanto, retorna a mesma URL
            return self.get_imagem_url(obj)
        return None
    
    def validate_ano(self, value):
        """Validação do ano"""
        if value < 1900 or value > 2030:
            raise serializers.ValidationError("O ano deve estar entre 1900 e 2030.")
        return value
    
    def validate_titulo(self, value):
        """Validação do título"""
        if len(value.strip()) < 2:
            raise serializers.ValidationError("O título deve ter pelo menos 2 caracteres.")
        return value.strip()
    
    def create(self, validated_data):
        """Cria uma nova série"""
        # Define o usuário atual como criador
        validated_data['criado_por'] = self.context['request'].user
        return super().create(validated_data)


class SerieListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listagem de séries"""
    
    criado_por_username = serializers.CharField(source='criado_por.username', read_only=True)
    genero_display = serializers.CharField(source='get_genero_display', read_only=True)
    genero_color = serializers.CharField(source='get_genero_display_color', read_only=True)
    imagem_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Serie
        fields = [
            'id',
            'titulo',
            'descricao',
            'ano',
            'genero',
            'genero_display',
            'genero_color',
            'imagem_url',
            'criado_por_username',
            'data_criacao',
        ]
    
    def get_imagem_url(self, obj):
        """Retorna a URL da imagem se existir"""
        if obj.imagem:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.imagem.url)
            return obj.imagem.url
        return None


class SerieCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer para criação e atualização de séries"""
    
    class Meta:
        model = Serie
        fields = [
            'titulo',
            'descricao',
            'ano',
            'genero',
            'imagem',
        ]
    
    def validate_ano(self, value):
        """Validação do ano"""
        if value < 1900 or value > 2030:
            raise serializers.ValidationError("O ano deve estar entre 1900 e 2030.")
        return value
    
    def validate_titulo(self, value):
        """Validação do título"""
        if len(value.strip()) < 2:
            raise serializers.ValidationError("O título deve ter pelo menos 2 caracteres.")
        return value.strip()
    
    def validate_imagem(self, value):
        """Validação da imagem"""
        if value:
            # Verifica o tamanho do arquivo (5MB)
            max_size = 5 * 1024 * 1024  # 5MB
            if value.size > max_size:
                raise serializers.ValidationError("A imagem deve ter no máximo 5MB.")
            
            # Verifica a extensão
            allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
            file_extension = value.name.split('.')[-1].lower()
            if file_extension not in allowed_extensions:
                raise serializers.ValidationError(
                    f"Extensões permitidas: {', '.join(allowed_extensions)}"
                )
        
        return value

