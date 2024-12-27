import django_filters
from .models import Painting
from django.db.models import Q

class PaintingFilter(django_filters.FilterSet):

    search = django_filters.CharFilter(method='filter_search')

   
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')  
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')  

   
    min_year = django_filters.NumberFilter(field_name='year', lookup_expr='gte') 
    max_year = django_filters.NumberFilter(field_name='year', lookup_expr='lte')  

  
    min_vertical_depth = django_filters.NumberFilter(field_name='vertical_depth', lookup_expr='gte')  # عمق عمودی بیشتر یا مساوی
    max_vertical_depth = django_filters.NumberFilter(field_name='vertical_depth', lookup_expr='lte')  # عمق عمودی کمتر یا مساوی
    min_horizontal_depth = django_filters.NumberFilter(field_name='horizontal_depth', lookup_expr='gte')  # عمق افقی بیشتر یا مساوی
    max_horizontal_depth = django_filters.NumberFilter(field_name='horizontal_depth', lookup_expr='lte')  # عمق افقی کمتر یا مساوی

   
    title = django_filters.CharFilter(lookup_expr='icontains') 
    description = django_filters.CharFilter(lookup_expr='icontains') 
    style = django_filters.CharFilter(lookup_expr='icontains')  
    material = django_filters.CharFilter(lookup_expr='icontains')  
    artist__username = django_filters.CharFilter(lookup_expr='icontains')  

    class Meta:
        model = Painting
        fields = [
            'search', 'title', 'description', 'style', 'material', 'artist__username',
            'min_price', 'max_price', 'min_year', 'max_year',
            'min_vertical_depth', 'max_vertical_depth', 'min_horizontal_depth', 'max_horizontal_depth'
        ]

  
    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |  
            Q(description__icontains=value) | 
            Q(style__icontains=value) | 
            Q(material__icontains=value) | 
            Q(artist__username__icontains=value)  
        )



















