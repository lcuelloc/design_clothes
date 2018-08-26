from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.images.models.image import Image
from v1.images.serializers.image import AdminImageSerializer
from v1.images.filters.image import AdminImageFilter
from v1.utils.views.mixins import MultiSerializerViewSetMixin
from v1.utils.views.paginators import NumPagesPagination


# v1/admin/images/
class AdminImageView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Image.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = NumPagesPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = AdminImageFilter
    search_fields = []
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = AdminImageSerializer
    serializer_action_classes = {
        'create': AdminImageSerializer,
        'list': AdminImageSerializer,
        'update': AdminImageSerializer,
        'partial_update': AdminImageSerializer,
    }
