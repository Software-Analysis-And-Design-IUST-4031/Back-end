from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Blog, Comment

User = get_user_model()

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  

    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'content', 'image', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'blog', 'author', 'content', 'created_at']
