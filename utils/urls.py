# urls.py
from django.urls import path
from utils import views

urlpatterns = [
    path('api/countries/', views.CountryListAPIView.as_view(), name='country-list'),
    path('api/cities/<str:country_iso3>/', views.CityListAPIView.as_view(), name='city-list'),
]
