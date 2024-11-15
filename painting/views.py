from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.views import APIView
from .models import Painting
from .serializers import PaintingDetailSerializer, PaintingListSerializer
from registering.models import CustomUser


class PaintingDetailView(APIView):
    """
    View to retrieve details of a specific painting.
    """
    serializer_class = PaintingDetailSerializer
    permission_classes = [AllowAny]

    def get(self, request, painting_id):
        try:
            painting = get_object_or_404(Painting, painting_id=painting_id)
            serializer = self.serializer_class(painting)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Painting.DoesNotExist:
            return Response({"error": "Painting not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": "Internal server error", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class UserPaintingsView(ListAPIView):
    """
    View to list all paintings of a specific user.
    """
    serializer_class = PaintingListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(CustomUser, user_id=user_id)
        return Painting.objects.filter(artist=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = request.query_params.get('page', 1)
        limit = request.query_params.get('limit', 10)
        
        paginator = Paginator(queryset, limit)
        try:
            paintings = paginator.page(page)
        except PageNotAnInteger:
            paintings = paginator.page(1)
        except EmptyPage:
            paintings = paginator.page(paginator.num_pages)

        serializer = self.serializer_class(paintings, many=True)
        response_data = {
            "userId": self.kwargs['user_id'],
            "paintings": serializer.data,
            "pagination": {
                "page": int(page),
                "limit": int(limit),
                "totalPages": paginator.num_pages,
                "totalPaintings": paginator.count
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)







class AddPaintingView(CreateAPIView):
    """
    View to add a new painting.
    """
    serializer_class = PaintingDetailSerializer
    permission_classes = [AllowAny]

    def post(self, request, user_id):
        user = get_object_or_404(CustomUser, user_id=user_id)
        serializer = self.serializer_class(data=request.data, files=request.FILES)  # Handle image files
        if serializer.is_valid():
            painting = serializer.save(artist=user)
            response_data = {
                "message": "Painting added successfully.",
                "painting": self.serializer_class(painting).data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response({"error": "Invalid request body", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)









































































































































# from django.shortcuts import render, get_object_or_404, redirect
# from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.response import Response
# from rest_framework import status
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from rest_framework.views import APIView
# from .models import Painting
# from .serializers import PaintingDetailSerializer, PaintingListSerializer
# from registering.models import CustomUser



# class PaintingDetailView(APIView):
#     serializer_class = PaintingDetailSerializer
#     permission_classes = [AllowAny]

#     def get(self, request, painting_id):
#         try:
#             painting = get_object_or_404(Painting, painting_id=painting_id)
#             serializer = self.serializer_class(painting)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Painting.DoesNotExist:
#             return Response({"error": "Painting not found"}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({"error": "Internal server error", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# class UserPaintingsView(ListAPIView):
#     serializer_class = PaintingListSerializer
#     permission_classes = [AllowAny]

#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         user = get_object_or_404(CustomUser, user_id=user_id)
#         return Painting.objects.filter(artist=user)

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         page = request.query_params.get('page', 1)
#         limit = request.query_params.get('limit', 10)
        
#         paginator = Paginator(queryset, limit)
#         try:
#             paintings = paginator.page(page)
#         except PageNotAnInteger:
#             paintings = paginator.page(1)
#         except EmptyPage:
#             paintings = paginator.page(paginator.num_pages)

#         serializer = self.serializer_class(paintings, many=True)
#         response_data = {
#             "userId": self.kwargs['user_id'],
#             "paintings": serializer.data,
#             "pagination": {
#                 "page": int(page),
#                 "limit": int(limit),
#                 "totalPages": paginator.num_pages,
#                 "totalPaintings": paginator.count
#             }
#         }
#         return Response(response_data, status=status.HTTP_200_OK)



# class AddPaintingView(CreateAPIView):
#     serializer_class = PaintingDetailSerializer
#     permission_classes = [AllowAny]

#     def post(self, request, user_id):
#         user = get_object_or_404(CustomUser, user_id=user_id)
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             painting = serializer.save(artist=user)
#             response_data = {
#                 "message": "Painting added successfully.",
#                 "painting": self.serializer_class(painting).data
#             }
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response({"error": "Invalid request body", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

















































































































# class PaintingDetailView(APIView):
#     serializer_class = PaintingDetailSerializer
#     permission_classes = [AllowAny]

#     def get(self, request, painting_id):
#         try:
#             painting = get_object_or_404(Painting, painting_id=painting_id)
#             serializer = self.serializer_class(painting)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Painting.DoesNotExist:
#             return Response(
#                 {"error": "Painting not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )
#         except Exception as e:
#             return Response(
#                 {"error": "Internal server error", "details": str(e)},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )







# class UserPaintingsView(ListAPIView):
#     serializer_class = PaintingListSerializer
#     permission_classes = [AllowAny]

#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         user = get_object_or_404(CustomUser, user_id=user_id)
#         return Painting.objects.filter(artist=user)

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         page = request.query_params.get('page', 1)
#         limit = request.query_params.get('limit', 10)
        
#         paginator = Paginator(queryset, limit)
#         try:
#             paintings = paginator.page(page)
#         except PageNotAnInteger:
#             paintings = paginator.page(1)
#         except EmptyPage:
#             paintings = paginator.page(paginator.num_pages)

#         serializer = self.serializer_class(paintings, many=True)
#         response_data = {
#             "userId": self.kwargs['user_id'],
#             "paintings": serializer.data,
#             "pagination": {
#                 "page": int(page),
#                 "limit": int(limit),
#                 "totalPages": paginator.num_pages,
#                 "totalPaintings": paginator.count
#             }
#         }
#         return Response(response_data, status=status.HTTP_200_OK)












# class AddPaintingView(CreateAPIView):
#     serializer_class = PaintingDetailSerializer
#     permission_classes = [AllowAny]

#     def post(self, request, user_id):
#         user = get_object_or_404(CustomUser, user_id=user_id)
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             painting = serializer.save(artist=user)
#             response_data = {
#                 "message": "Painting added successfully.",
#                 "painting": self.serializer_class(painting).data
#             }
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response(
#             {"error": "Invalid request body", "details": serializer.errors},
#             status=status.HTTP_400_BAD_REQUEST
#         )

















# class PaintingDetailView(RetrieveAPIView):
#     queryset = Painting.objects.all()
#     serializer_class = PaintingDetailSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         painting_id = self.kwargs['painting_id']
#         painting = get_object_or_404(Painting, painting_id=painting_id)
#         return painting

#     def handle_exception(self, exc):
#         if isinstance(exc, Painting.DoesNotExist):
#             return Response({"error": "Painting not found"}, status=status.HTTP_404_NOT_FOUND)
#         return super().handle_exception(exc)





# class UserPaintingsView(ListAPIView):
#     serializer_class = PaintingListSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         user = get_object_or_404(CustomUser, user_id=user_id)
#         return Painting.objects.filter(artist=user)




# class AddPaintingView(CreateAPIView):
#     serializer_class = PaintingDetailSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         user_id = self.kwargs['user_id']
#         user = get_object_or_404(CustomUser, user_id=user_id)
#         serializer.save(artist=user)
































# from django.shortcuts import render

# # Create your views here.

# from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
# from rest_framework.permissions import IsAuthenticated
# from .models import Painting
# from .serializers import PaintingDetailSerializer, PaintingListSerializer



# #  نمایش جزئیات یک نقاشی خاص
# class PaintingDetailView(RetrieveAPIView):
#     queryset = Painting.objects.all()
#     serializer_class = PaintingDetailSerializer




# #  برای نمایش تمام نقاشی‌های کاربر
# class UserPaintingsView(ListAPIView):
#     serializer_class = PaintingListSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Painting.objects.filter(artist=self.request.user)




# #  برای افزودن نقاشی جدید
# class AddPaintingView(CreateAPIView):
#     serializer_class = PaintingDetailSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(artist=self.request.user)











