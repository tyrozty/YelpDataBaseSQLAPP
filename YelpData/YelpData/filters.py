import django_filters
from YelpData.models import *


class UserFilter(django_filters.FilterSet):
    user_name = django_filters.CharFilter(field_name='user_name',label='Yelp User Name',lookup_expr='icontains')
    user_identifier = django_filters.CharFilter(field_name='user_identifier',label='Yelp User ID',lookup_expr='icontains')
    #heritage_site_category = django_filters.ModelChoiceFilter(field_name='heritage_site_category',label='Category',queryset=HeritageSiteCategory.objects.all().order_by('category_name'),lookup_expr='exact')
    #region = django_filters.ModelChoiceFilter(field_name='country_area__location__region__region_name',label='Heritage Region',queryset=Region.objects.all().order_by('region_name'),lookup_expr='exact')
    #sub_region = django_filters.ModelChoiceFilter(field_name='country_area__location__sub_region__sub_region_name',label='SubRegion',queryset=SubRegion.objects.all().order_by('sub_region_name'), lookup_expr='exact')
    #intermediate_region = django_filters.ModelChoiceFilter(field_name='country_area__location__intermediate_region__intermediate_region_name',label='Intermediate Region',queryset=IntermediateRegion.objects.all().order_by('intermediate_region_name'),lookup_expr='exact')
    #country_area = django_filters.ModelChoiceFilter(field_name='country_area',label='Country/Area',queryset=CountryArea.objects.all().order_by('country_area_name'),lookup_expr='exact')
    #date_inscribed = django_filters.NumberFilter(field_name='data_inscribed',label='Data Inscribed',lookup_expr='contains')

    class Meta:
        model = User
        # form = SearchForm
        # fields [] is required, even if empty.
        fields = []
