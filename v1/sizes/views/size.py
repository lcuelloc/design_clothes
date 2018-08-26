from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.sizes.models.size import Size
from v1.sizes.serializers.size import AdminSizeSerializer
from v1.sizes.filters.size import AdminSizeFilter
from v1.utils.views.mixins import MultiSerializerViewSetMixin
from v1.utils.views.paginators import NumPagesPagination


# v1/admin/sizes/
class AdminSizeView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Size.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = NumPagesPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = AdminSizeFilter
    search_fields = []
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_action_classes = {
        'create': AdminSizeSerializer,
        'list': AdminSizeSerializer,
        'update': AdminSizeSerializer,
        'partial_update': AdminSizeSerializer,
    }
