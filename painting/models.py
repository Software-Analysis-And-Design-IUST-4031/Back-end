from django.db import models
from django.conf import settings
# Create your models here.
# from gallery.models import Gallery


class Painting(models.Model):
    painting_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='paintings/', null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='paintings')
<<<<<<< HEAD
    gallery = models.ForeignKey(
    'gallery.Gallery', 
    on_delete=models.CASCADE, 
    related_name='paintings',
    default=None
)

=======
    # gallery = models.ForeignKey('Gallery', on_delete=models.SET_NULL, null=True, blank=True, related_name='gallery')
>>>>>>> e185d6152f32c0678fa6f38c75f1cb5bebde6217
    def __str__(self):
        return self.title





















