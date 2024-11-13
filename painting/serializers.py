from rest_framework import serializers
from .models import Painting



class PaintingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['id', 'title', 'description', 'creation_date', 'artist', 'gallery']


class PaintingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['id', 'title', 'creation_date']




