
from django.db import models

class Country(models.Model):
    """
    Country model that uses ISO3 country codes.
    """
    name = models.CharField(max_length=255)  
    iso3_code = models.CharField(max_length=3, unique=True, null=True)  

    def __str__(self):
        return self.name


class City(models.Model):
    """
    City model that is related to a specific country.
    """
    name = models.CharField(max_length=255)  
    country = models.ForeignKey(Country, on_delete=models.CASCADE)  

    def __str__(self):
        return self.name
