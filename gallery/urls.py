from django.urls import path
from .views import GalleryListView

urlpatterns = [
    path('galleries/', GalleryListView.as_view(), name='gallery-list'),  
]
