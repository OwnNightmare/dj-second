from django.conf.global_settings import AUTH_USER_MODEL
from django_filters import rest_framework as filters, DateFromToRangeFilter, DateTimeFromToRangeFilter, NumberFilter, \
    ModelChoiceFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
