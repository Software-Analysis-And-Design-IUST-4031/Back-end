from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Gallery
from .serializers import GallerySerializer

class GalleryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        galleries = Gallery.objects.all()
        
        gallery_data = [
            {
                "gallery_name": gallery.name,
                "description": gallery.description,
                "image_url": gallery.image_url,
                "number_of_paintings": gallery.number_of_paintings(),
                "number_of_artists": gallery.number_of_artists(),
                "owner_id": gallery.owner.id  
            }
            for gallery in galleries
        ]
        return Response(gallery_data)

    def post(self, request):
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            gallery = serializer.save()
            return Response(GallerySerializer(gallery).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)