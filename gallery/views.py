from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Gallery
from .serializers import GallerySerializer
from rest_framework import status

class GalleryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        galleries = Gallery.objects.prefetch_related('owner').all()
        
        gallery_data = [
            {
                "gallery_name": gallery.name,
                "description": gallery.description,
                "image_url": gallery.cover_painting.image_url if gallery.cover_painting else None,
                "number_of_paintings": gallery.number_of_paintings(),
                "number_of_artists": gallery.number_of_artists(),
                "owner_id": gallery.owner.user_id if gallery.owner else None
            }
            for gallery in galleries
        ]
        return Response(gallery_data, status=status.HTTP_200_OK)

