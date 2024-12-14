# serializers.py
from rest_framework import serializers
<<<<<<< Updated upstream
from utils.models import Country, City

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['iso3_code', 'name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'country']
=======
from .models import City

class UserSelectionSerializer(serializers.Serializer):
    country = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)

    def validate(self, data):
        country = data.get('country')
        city = data.get('city')

        # Validate if the city exists for the given country
        if not City.objects.filter(country=country, name=city).exists():
            raise serializers.ValidationError("The specified city does not exist in the given country.")
        
        return data
>>>>>>> Stashed changes
