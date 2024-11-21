from django.urls import path
from .views import GalleryListView, GalleryDetailView

urlpatterns = [
    path('gallery/', GalleryListView.as_view(), name='gallery-list'),  # This is for GET requests for the list of galleries.
    path('gallery/<int:pk>/', GalleryDetailView.as_view(), name='gallery-detail'),  # This is for GET requests for a specific gallery by pk.
]
