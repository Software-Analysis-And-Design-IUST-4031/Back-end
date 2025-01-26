from django.urls import path

from .views import PaintingDetailView, UserPaintingsView,AddPaintingView , LikePaintingView, GetPaintingLikesView , TopPaintingView , SortedPaintingsByLikesView , UserLikesSumView , DeletePaintingView , DeletePaintingView2 , UnLikePaintingView , CheckUserLikedPaintingView , PaintingDetailWithAuthorView , PaintingSearchView, SavePaintingView, UnsavePaintingView, SavedPaintingsView, DepositCoinsView, PurchasePaintingView




urlpatterns = [
    path('<int:painting_id>/', PaintingDetailView.as_view()),
    path('<int:painting_id>/with-author/', PaintingDetailWithAuthorView.as_view()),
    path('user/<int:user_id>/paintings/', UserPaintingsView.as_view()),
    path('user/<int:user_id>/paintings/add/', AddPaintingView.as_view()),
    path('paintings/<int:pk>/delete/', DeletePaintingView.as_view(), name='delete-painting'),
    path('user/<int:user_id>/paintings/delete/<int:painting_id>/', DeletePaintingView2.as_view(), name='delete-painting'),
    path('paintings/<int:painting_id>/like/', LikePaintingView.as_view(), name='like_painting'),
    path('paintings/<int:painting_id>/Unlike/', UnLikePaintingView.as_view(), name='Unlike_painting'),
    path('paintings/<int:painting_id>/likes/', GetPaintingLikesView.as_view(), name='get_painting_likes'),
    path('paintings/top/', TopPaintingView.as_view(), name='top_painting'),
    path('user/top-painters/', UserLikesSumView.as_view(), name='user-likes-sum'),   
    path('paintings/sorted-by-likes/', SortedPaintingsByLikesView.as_view(), name='sorted_paintings_by_likes'),
    path('user/<int:user_id>/paintings/<int:painting_id>/liked/', CheckUserLikedPaintingView.as_view(), name='check_user_liked_painting'),
    path('paintings/search/', PaintingSearchView.as_view(), name='painting-search'),
     path('paintings/save/<int:painting_id>/', SavePaintingView.as_view(), name='save_painting'),
    path('paintings/unsave/<int:painting_id>/', UnsavePaintingView.as_view(), name='unsave_painting'),
    path('paintings/saved/', SavedPaintingsView.as_view(), name='saved_paintings'),
   path('paintings/deposit/', DepositCoinsView.as_view(), name='deposit_coins'),
    path('paintings/purchase/', PurchasePaintingView.as_view(), name='purchase_painting'),
]








