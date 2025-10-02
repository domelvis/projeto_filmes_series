from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import UserActivity

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    watched_series_count = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    wishlist_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 
                 'profile_image', 'bio', 'email_notifications', 'date_joined',
                 'watched_series_count', 'reviews_count', 'wishlist_count')
        read_only_fields = ('id', 'date_joined')

    def get_watched_series_count(self, obj):
        return obj.activities.filter(type='watched').count()

    def get_reviews_count(self, obj):
        return obj.activities.filter(type='review').count()

    def get_wishlist_count(self, obj):
        return obj.activities.filter(type='wishlist').count()

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = ('id', 'type', 'description', 'created_at')
        read_only_fields = ('id', 'created_at')