from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'title', 
            'description',
            'timestamp',
            'owner',
            'location',
            'price',
        )