from django.urls import path
from .views import PaintingDetailView, UserPaintingsView, AddPaintingView ,LikePaintingView ,  GetPaintingLikesView , TopPaintingView , SortedPaintingsByLikesView

urlpatterns = [
    path('paintings/<int:painting_id>/', PaintingDetailView.as_view()),
    path('user/<int:user_id>/paintings/', UserPaintingsView.as_view()),
    path('user/<int:user_id>/paintings/add/', AddPaintingView.as_view()),
    path('paintings/<int:painting_id>/like/', LikePaintingView.as_view(), name='like_painting'),
    path('paintings/<int:painting_id>/likes/', GetPaintingLikesView.as_view(), name='get_painting_likes'),
    path('paintings/top/', TopPaintingView.as_view(), name='top_painting'),
    path('paintings/sorted-by-likes/', SortedPaintingsByLikesView.as_view(), name='sorted_paintings_by_likes'),
]








