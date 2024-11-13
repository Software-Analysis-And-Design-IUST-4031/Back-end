from django.urls import path
from .views import PaintingDetailView, UserPaintingsView, AddPaintingView

urlpatterns = [
    path('<int:painting_id>/', PaintingDetailView.as_view()),
    path('user/<int:user_id>/paintings/', UserPaintingsView.as_view()),
    path('user/<int:user_id>/paintings/add/', AddPaintingView.as_view()),
]


























# from django.urls import path
# from .views import PaintingDetailView, UserPaintingsView, AddPaintingView

# urlpatterns = [
#     path('user/painting/<int:pk>/', PaintingDetailView.as_view()),
#     path('user/paintings/', UserPaintingsView.as_view()),
#     path('user/painting/add/', AddPaintingView.as_view()),
# ]




