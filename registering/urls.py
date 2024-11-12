from django.urls import path
from registering.views import (
	UserRegistrationAPIView,
	UserLoginAPIView,
	UserViewAPI,
	UserLogoutViewAPI,
    UserDetailAPIView,
    UserUpdateAPIView,
)


urlpatterns = [
	path('user/register/', UserRegistrationAPIView.as_view()),
	path('user/login/', UserLoginAPIView.as_view()),
	path('user/', UserViewAPI.as_view()),
	path('user/logout/', UserLogoutViewAPI.as_view()),
    path('user/<int:user_id>/detail/', UserDetailAPIView.as_view(), name='user-detail'), 
    path('user/<int:user_id>/update/', UserUpdateAPIView.as_view(), name='user-update'),
]