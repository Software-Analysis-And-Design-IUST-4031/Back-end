from rest_framework import serializers
from .models import Painting
from .models import Like

class PaintingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['painting_id', 'title', 'description','image', 'creation_date', 'artist' , 'price', 'material' , 'style' , 'year' , 'vertical_depth' , 'horizontal_depth']
        read_only_fields = ['artist', 'creation_date'] 

class PaintingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['painting_id', 'title', 'description' ,'image' , 'creation_date' , 'price','material' , 'style' , 'year' , 'vertical_depth' , 'horizontal_depth']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'painting', 'created_at']





