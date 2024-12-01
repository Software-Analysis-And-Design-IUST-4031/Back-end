from django.urls import path
from .views import PaintingDetailView, UserPaintingsView, AddPaintingView , LikePaintingView ,  GetPaintingLikesView

urlpatterns = [
    path('<int:painting_id>/', PaintingDetailView.as_view()),
    path('user/<int:user_id>/paintings/', UserPaintingsView.as_view()),
    path('user/<int:user_id>/paintings/add/', AddPaintingView.as_view()),
    path('paintings/<int:painting_id>/like/', LikePaintingView.as_view(), name='like_painting'),
    path('paintings/<int:painting_id>/likes/', GetPaintingLikesView.as_view(), name='get_painting_likes'),
]








