import django_filters

from advertisements.models import Advertisement


class AdvertisementFilter(django_filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = django_filters.DateFromToRangeFilter(field_name='created_at')
    status = django_filters.ChoiceFilter(choices=Advertisement.STATUS_CHOICES)

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at']
