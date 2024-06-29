from rest_framework import serializers
from .models import Articles

from django.contrib.auth import get_user_model

class ArticlesSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "category",
            "created_at",
            "image_url",
        )
        model = Articles
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username",)