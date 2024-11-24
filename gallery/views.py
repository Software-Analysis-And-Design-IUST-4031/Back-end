from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Gallery
from .serializers import GallerySerializer
from rest_framework import status
from django.conf import settings
from registering.models import CustomUser

class GalleryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users_with_gallery = CustomUser.objects.filter(is_gallery=True)
        gallery_data = []

        for user in users_with_gallery:
            galleries = Gallery.objects.filter(owner=user)
            print(galleries)
            for gallery in galleries:
                gallery_data.append({
                    "name": gallery.name,
                    "description": gallery.description,
                    "cover_image": gallery.cover_painting.image_url if gallery.cover_painting else None,
                    "number_of_paintings": gallery.number_of_paintings(),
                    "number_of_artists": gallery.number_of_artists(),
                    "owner_id": gallery.owner.user_id if gallery.owner else None
                })
        
        
        return Response(gallery_data, status=status.HTTP_200_OK)




