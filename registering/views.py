from django.shortcuts import render
from registering.serializers import UserRegistrationSerializer, UserLoginSerializer
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
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationAPIView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'message': 'User registered successfully.',
            }
            response = Response(data, status=status.HTTP_201_CREATED)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user_model = get_user_model()

            user_instance = authenticate(username=username, password=password)
            if not user_instance:
                raise AuthenticationFailed('Invalid username or password.')
            if not user_instance.is_active:
                raise AuthenticationFailed('This account is inactive.')

            refresh = RefreshToken.for_user(user_instance)
            access_token = str(refresh.access_token)
            return Response({
                'message': 'Login successful.',
                'access': access_token,
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)
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
