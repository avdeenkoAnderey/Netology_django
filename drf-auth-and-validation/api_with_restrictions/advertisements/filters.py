from django_filters import rest_framework as filters
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    status = filters.ChoiceFilter(
        choices=Advertisement.status.field.choices,
        label="Статус"
    )

    created_at = filters.DateFromToRangeFilter(
        field_name='created_at',
        label='Дата создания'
    )

    creator = filters.NumberFilter(
        field_name='creator',

    )

    class Meta:
        field = ['status', 'created_at']
