from rest_framework import serializers
from .models import Painting
from .models import Like

class PaintingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['painting_id', 'title', 'description','image', 'creation_date', 'artist']
        read_only_fields = ['artist', 'creation_date'] 

class PaintingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['painting_id', 'title', 'description' ,'image' , 'creation_date']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'painting', 'created_at']





