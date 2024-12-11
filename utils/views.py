from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.models import City

class CountryListAPIView(APIView):
    """
    Returns a list of unique ISO3 country codes.
    """
    def get(self, request):
        iso3_codes = City.objects.values_list('iso3', flat=True).distinct()
        return Response({'countries': list(iso3_codes)}, status=status.HTTP_200_OK)


class CityListByCountryAPIView(APIView):
    """
    Returns a list of cities filtered by ISO3 country code.
    """
    def get(self, request, iso3):
        cities = City.objects.filter(iso3=iso3).values_list('name', flat=True)
        return Response({'cities': list(cities)}, status=status.HTTP_200_OK)
