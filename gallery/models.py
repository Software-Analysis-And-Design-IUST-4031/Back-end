from django.db import models
from django.db import models
from django.conf import settings
from painting.models import Painting

class Gallery(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='galleries'  
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    # image_url = models.URLField(max_length=500, null=True, blank=True)  
    def __str__(self):
        return self.name

    def number_of_paintings(self):
        return Painting.objects.filter(artist__gallery=self).count()

    def number_of_artists(self):
        return Painting.objects.filter(artist__gallery=self).values('artist').distinct().count()

