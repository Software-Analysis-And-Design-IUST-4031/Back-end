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
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='paintings',default=None)
    price = models.IntegerField(null=True, blank=True) 

    def __str__(self):
        return self.title








class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'painting')

    def __str__(self):
        return f"{self.user.username} likes {self.painting.title}"


















