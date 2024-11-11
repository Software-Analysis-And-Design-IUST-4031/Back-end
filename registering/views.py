from django.shortcuts import render
from registering.serializers import UserRegistrationSerializer, UserSerializer, UserLoginSerializer , ProfileSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status , generics
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.conf import settings
from django.contrib.auth import get_user_model
from .utils import generate_access_token
from .models import CustomUser,Profile
import jwt



class UserRegistrationAPIView(APIView):
	serializer_class = UserRegistrationSerializer
	permission_classes = (AllowAny,)

	def post(self, request):
	
		serializer = self.serializer_class(data=request.data)
		
		if serializer.is_valid(raise_exception=True):
			new_user = serializer.save()
			
			if new_user:
				
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
		email = request.data.get('email', None)
		user_password = request.data.get('password', None)

		if not user_password:
			raise AuthenticationFailed('A user password is needed.')

		if not email:
			raise AuthenticationFailed('An user email is needed.')

		user_instance = authenticate(username=email, password=user_password)

		if not user_instance:
			raise AuthenticationFailed('User not found.')

		if user_instance.is_active:
			user_access_token = generate_access_token(user_instance)
			response = Response()
			response.set_cookie(key='access_token', value=user_access_token, httponly=True)
			response.data = {
				'access_token': user_access_token
			}
			return response

		return Response({
			'message': 'Something went wrong.'
		})



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
		if user_token:
			response = Response()
			response.delete_cookie('access_token')
			response.data = {
				'message': 'Logged out successfully.'
			}
			return response
		response = Response()
		response.data = {
			'message': 'User is already logged out.'
		}
		return response










class UserProfileDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        profile_serializer = ProfileSerializer(profile)
        user_serializer = UserSerializer(request.user)
        data = {
            'user': user_serializer.data,
            'profile': profile_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


    def put(self, request):
        profile = Profile.objects.get(user=request.user)
        profile_serializer = ProfileSerializer(profile, data=request.data.get('profile'), partial=True)
        user_serializer = UserSerializer(request.user, data=request.data.get('user'), partial=True)

        if profile_serializer.is_valid() and user_serializer.is_valid():
            profile_serializer.save()
            user_serializer.save()
            data = {
                'user': user_serializer.data,
                'profile': profile_serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)

        errors = {
            'profile_errors': profile_serializer.errors,
            'user_errors': user_serializer.errors
        }
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)
	


	


class UserEditAPI(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	




class UserDetailAPI(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)





