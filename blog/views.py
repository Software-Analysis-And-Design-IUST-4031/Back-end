from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class BlogListCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # List all blogs
        blogs = Blog.objects.all().order_by('-created_at')
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new blog post
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        blog_id = request.data.get('blog')
        content = request.data.get('content')

        if not blog_id or not content:
            return Response({'detail': 'Blog and content are required fields.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({'detail': 'Blog not found.'}, status=status.HTTP_404_NOT_FOUND)

        
        comment = Comment.objects.create(blog=blog, author=request.user, content=content)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
