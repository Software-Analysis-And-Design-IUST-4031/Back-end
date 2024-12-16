import django_filters
from registering.models import CustomUser

class CustomUserFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = {
            'firstname': ['exact', 'icontains'],
            'lastname': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            # Add other fields as necessary
        } 