from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter()
    print('AdvertisementFilter')
    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at', 'status']
