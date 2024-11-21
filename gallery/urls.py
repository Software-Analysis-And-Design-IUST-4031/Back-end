from django.urls import path
from .views import GalleryListView, GalleryDetailView

urlpatterns = [
    path('gallery/', GalleryListView.as_view(), name='gallery-list'),  
    path('gallery/<int:pk>/', GalleryDetailView.as_view(), name='gallery-detail'),  
]
