from django.urls import path
from registering.views import (
	UserRegistrationAPIView,
	UserLoginAPIView,
	UserViewAPI,
	UserLogoutViewAPI,
    UserProfileDetailAPIView,
    UserDetailAPI,
    UserEditAPI
)


urlpatterns = [
	path('user/register/', UserRegistrationAPIView.as_view()),
	path('user/login/', UserLoginAPIView.as_view()),
	path('user/', UserViewAPI.as_view()),
	path('user/logout/', UserLogoutViewAPI.as_view()),
    path('user/profile/', UserProfileDetailAPIView.as_view()),
    path('user/profile/detail', UserDetailAPI.as_view()),
    path('user/profile/edit/', UserEditAPI.as_view() ),
]



