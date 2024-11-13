from django.db import models
from django.conf import settings

class Painting(models.Model):
    painting_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='paintings')
    # gallery = models.ForeignKey('Gallery', on_delete=models.SET_NULL, null=True, blank=True, related_name='paintings')
    def __str__(self):
        return self.title
















# from django.db import models
# from django.conf import settings

# class Painting(models.Model):
#     painting_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     creation_date = models.DateField(auto_now_add=True)
#     artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='paintings')
#     # gallery = models.ForeignKey('Gallery', on_delete=models.SET_NULL, null=True, blank=True, related_name='paintings')

#     def __str__(self):
#         return self.title









