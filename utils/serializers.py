from rest_framework import serializers
from utils.models import City

class CountrySerializer(serializers.Serializer):
    """
    Serializer for listing unique ISO3 country codes.
    """
    iso3 = serializers.CharField()

class CitySerializer(serializers.ModelSerializer):
    """
    Serializer for listing cities filtered by ISO3 country code.
    """
    class Meta:
        model = City
        fields = ['name']
