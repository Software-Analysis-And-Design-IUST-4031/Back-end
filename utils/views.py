# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.models import Country, City
from utils.serializers import CountrySerializer, CitySerializer

class CountryListAPIView(APIView):
    """
    API view to list all countries.
    """

    def get(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CityListAPIView(APIView):
    """
    API view to list cities based on the selected country.
    """

    def get(self, request, country_iso3):
        # Get the country using its ISO3 code
        try:
            country = Country.objects.get(iso3_code=country_iso3)
        except Country.DoesNotExist:
            return Response({"detail": "Country not found."}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve all cities for the given country
        cities = City.objects.filter(country=country)
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
