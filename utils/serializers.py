# serializers.py
from rest_framework import serializers
from utils.models import Country, City

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['iso3_code', 'name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'country']
