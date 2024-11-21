from rest_framework import serializers
from .models import Gallery

class GallerySerializer(serializers.ModelSerializer):
    number_of_paintings = serializers.SerializerMethodField()
    number_of_artists = serializers.SerializerMethodField()
    owner_id = serializers.IntegerField(source='owner.id', read_only=True)  
    cover_image = serializers.ImageField(source='cover_painting.image', read_only=True)
    class Meta:
        model = Gallery
        fields = ['name', 'description', 'cover_image', 'number_of_paintings', 'number_of_artists', 'owner_id']  

    def get_number_of_paintings(self, obj):
        return obj.number_of_paintings()

    def get_number_of_artists(self, obj):
        return obj.number_of_artists()
