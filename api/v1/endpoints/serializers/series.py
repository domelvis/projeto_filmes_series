from rest_framework import serializers
from series.models import Serie
from reviews.models import Review
from .users import UserSerializer

class SerieSerializer(serializers.ModelSerializer):
    criado_por = UserSerializer(read_only=True)
    
    class Meta:
        model = Serie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    serie = SerieSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'