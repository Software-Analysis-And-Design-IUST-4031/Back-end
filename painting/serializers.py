from rest_framework import serializers
from .models import Painting

class PaintingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['painting_id', 'title', 'description','image', 'creation_date', 'artist']
        read_only_fields = ['artist', 'creation_date'] 

class PaintingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['painting_id', 'title', 'description' ,'image' , 'creation_date']


