from django.urls import path
from .views import BlogListCreateAPIView, CommentCreateAPIView

urlpatterns = [
    path('', BlogListCreateAPIView.as_view(), name='blog-list-create'),  # This is now accessed via api/blogs/
    path('comments/', CommentCreateAPIView.as_view(), name='comment-create'),  # This will be api/blogs/comments/
]
