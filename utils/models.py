# models.py
from django.db import models

class Country(models.Model):
    """
    Country model that uses ISO3 country codes.
    """
    name = models.CharField(max_length=255)  # Name of the country
    iso3_code = models.CharField(max_length=3, unique=True, null=True)  # ISO3 code

    def __str__(self):
        return self.name


class City(models.Model):
    """
    City model that is related to a specific country.
    """
    name = models.CharField(max_length=255)  # Name of the city
    country = models.ForeignKey(Country, on_delete=models.CASCADE)  # Foreign key to Country

    def __str__(self):
        return self.name
