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
        serializer = GallerySerializer(galleries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            gallery = serializer.save()
            return Response(GallerySerializer(gallery).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GalleryDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            gallery = Gallery.objects.get(pk=pk)
        except Gallery.DoesNotExist:
            return Response({"detail": "Gallery not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = GallerySerializer(gallery)
        return Response(serializer.data)

