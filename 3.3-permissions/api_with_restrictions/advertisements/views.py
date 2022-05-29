from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwned
from advertisements.serializers import AdvertisementSerializer, UserSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filterset_class = AdvertisementFilter
    # filterset_fields = ['creator', 'status', 'created_at']
    search_fields = ['title', 'description', 'status']
    ordering_fields = ['created_at', 'updated_at']
    permission_classes = [IsAuthenticated, IsOwned]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsOwned()]
        return []
