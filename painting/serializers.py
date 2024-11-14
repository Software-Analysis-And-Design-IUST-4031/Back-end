from rest_framework import serializers
from .models import Painting

class PaintingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['painting_id', 'title', 'description', 'creation_date', 'artist']
        read_only_fields = ['artist'] 

class PaintingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['painting_id', 'title', 'creation_date']
































# from rest_framework import serializers
# from .models import Painting



# class PaintingDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Painting
#         fields = ['id', 'title', 'description', 'creation_date', 'artist', 'gallery']


# class PaintingListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Painting
#         fields = ['id', 'title', 'creation_date']




