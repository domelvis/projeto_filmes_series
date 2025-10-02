from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)

class UserProfileSerializer(serializers.ModelSerializer):
    series_favoritas = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'bio', 'avatar', 'series_favoritas', 'reviews')
        read_only_fields = ('id', 'series_favoritas', 'reviews')
    
    def get_series_favoritas(self, obj):
        from .series import SerieSerializer
        return SerieSerializer(obj.series_favoritas.all(), many=True).data
    
    def get_reviews(self, obj):
        from .series import ReviewSerializer
        return ReviewSerializer(obj.reviews.all(), many=True).data