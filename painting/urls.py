from django.urls import path
from .views import PaintingDetailView, UserPaintingsView, AddPaintingView

urlpatterns = [
    path('user/painting/<int:pk>/', PaintingDetailView.as_view()),
    path('user/paintings/', UserPaintingsView.as_view()),
    path('user/painting/add/', AddPaintingView.as_view()),
]




