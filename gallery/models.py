from django.db import models
from django.db import models
from django.conf import settings
from painting.models import Painting

class Gallery(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='galleries',
        null=False 
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    cover_painting = models.ForeignKey(
        Painting,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='galleries_as_cover'
    ) 
    def __str__(self):
        return self.name

    def number_of_paintings(self):
        return Painting.objects.filter(artist__gallery=self).count()

    def number_of_artists(self):
        return Painting.objects.filter(artist__gallery=self).values('artist').distinct().count()

