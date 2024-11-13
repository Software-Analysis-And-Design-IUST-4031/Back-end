from django.shortcuts import render

# Create your views here.

from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Painting
from .serializers import PaintingDetailSerializer, PaintingListSerializer



#  نمایش جزئیات یک نقاشی خاص
class PaintingDetailView(RetrieveAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingDetailSerializer




#  برای نمایش تمام نقاشی‌های کاربر
class UserPaintingsView(ListAPIView):
    serializer_class = PaintingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Painting.objects.filter(artist=self.request.user)




#  برای افزودن نقاشی جدید
class AddPaintingView(CreateAPIView):
    serializer_class = PaintingDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(artist=self.request.user)












