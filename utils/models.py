from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    iso3 = models.CharField(max_length=3, blank=True)  
    def __str__(self):
        return f"{self.name} ({self.iso3})"
