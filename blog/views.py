from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.generics import ListAPIView

class BlogListCreateView(ListCreateAPIView):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.get_object().author != self.request.user:
            raise PermissionDenied("You are not allowed to edit this blog.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("You are not allowed to delete this blog.")
        instance.delete()




class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        blog_id = self.kwargs['blog_id']
        parent_id = self.request.data.get('parent')

        if parent_id:
            try:
                parent_comment = Comment.objects.get(id=parent_id)
                if parent_comment.parent is not None:
                    raise ValidationError("Replies to replies are not allowed.")
            except Comment.DoesNotExist:
                raise ValidationError("Parent comment does not exist.")
        else:
            parent_comment = None

        serializer.save(author=self.request.user, blog_id=blog_id, parent=parent_comment)

class BlogCommentListView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        blog_id = self.kwargs['blog_id']
        return Comment.objects.filter(blog_id=blog_id).order_by('-created_at')