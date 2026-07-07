from django_filters import rest_framework as filters
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    status = filters.ChoiceFilter(choices=Advertisement.status.field.choices)
    created_after = filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_before = filters.DateFilter(field_name='created_at', lookup_expr='lte')
    creator = filters.NumberFilter(field_name='creator', lookup_expr='exact')

    class Meta:
        model = Advertisement
        fields = ('status', 'created_after', 'created_before','creator')
