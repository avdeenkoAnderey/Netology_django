from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)

class AdvertisementSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at', 'author', 'author_username']
        read_only_fields = ['author', 'created_at', 'updated_at']
