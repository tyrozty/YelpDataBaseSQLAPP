import django_filters
from YelpData.models import *


class UserFilter(django_filters.FilterSet):
    user_name = django_filters.CharFilter(field_name='user_name',label='Yelp User Name',lookup_expr='icontains')
    user_identifier = django_filters.CharFilter(field_name='user_identifier',label='Yelp User ID',lookup_expr='icontains')

    class Meta:
        model = User
        fields = []
