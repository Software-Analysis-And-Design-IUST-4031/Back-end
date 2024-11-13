from django.shortcuts import render
from registering.serializers import UserRegistrationSerializer, UserLoginSerializer , UserDetailSerializer ,  UserUpdateSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.conf import settings
from django.contrib.auth import get_user_model
from .utils import generate_access_token
import jwt
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from registering.models import CustomUser
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView




class UserRegistrationAPIView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_user = serializer.save()
            access_token = generate_access_token(new_user)
            data = {
                'message': 'User registered successfully.',
                'access_token': access_token
            }
            response = Response(data, status=status.HTTP_201_CREATED)
            response.set_cookie(key='access_token', value=access_token, httponly=True)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            user_instance = authenticate(username=username, password=password)
            if not user_instance:
                raise AuthenticationFailed('Invalid username or password.')
            if not user_instance.is_active:
                raise AuthenticationFailed('This account is inactive.')

            token, created = Token.objects.get_or_create(user=user_instance)
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request):
        user_token = request.COOKIES.get('access_token')
        if not user_token:
            raise AuthenticationFailed('Unauthenticated user.')

        payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])
        user_model = get_user_model()
        user = user_model.objects.filter(user_id=payload['user_id']).first()
        user_serializer = UserRegistrationSerializer(user)
        return Response(user_serializer.data)


class UserLogoutViewAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request):
        user_token = request.COOKIES.get('access_token', None)
        response = Response()
        if user_token:
            response.delete_cookie('access_token')
            response.data = {'message': 'Logged out successfully.'}
        else:
            response.data = {'message': 'User is already logged out.'}
        return response
    








class UserDetailAPIView(APIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        try:
            user = get_object_or_404(CustomUser, user_id=user_id)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": "Internal server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )










class UserUpdateAPIView(APIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, user_id):
        try:
            user = get_object_or_404(CustomUser, user_id=user_id)
            
            # بررسی اعتبار درخواست و به‌روزرسانی اطلاعات کاربر
            serializer = self.serializer_class(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "User profile updated successfully.", "user": serializer.data},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"error": "Invalid data", "details": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": "Internal server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )












# class UserDetailAPIView(RetrieveAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserDetailSerializer
#     permission_classes = [IsAuthenticated]
#     # permission_classes = [AllowAny]

#     def get_object(self):
#         user_id = self.kwargs['user_id']  
#         return get_object_or_404(CustomUser, user_id=user_id)




# class UserUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserUpdateSerializer
#     permission_classes = [IsAuthenticated]
#     # permission_classes = [AllowAny]

#     def get_object(self):
#         user_id = self.kwargs['user_id']  
#         return get_object_or_404(CustomUser, user_id=user_id)
    


















