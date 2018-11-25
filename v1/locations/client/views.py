from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django_filters.rest_framework import DjangoFilterBackend

from v1.locations.models.location import Location
from v1.locations.client.serializers import ClientLocationSerializer
from v1.locations.filters.location import AdminLocationFilter
from v1.utils.views.mixins import MultiSerializerViewSetMixin
from v1.utils.views.paginators import NumPagesPagination
from v1.utils.views.permissions import IsClientPermission


# v1/client/locations/
class ClientLocationView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Location.objects.all()
    permission_classes = [IsAuthenticated, IsClientPermission]
    pagination_class = NumPagesPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = AdminLocationFilter
    search_fields = []
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_action_classes = {
        'create': ClientLocationSerializer,
        'list': ClientLocationSerializer,
        'update': ClientLocationSerializer,
        'partial_update': ClientLocationSerializer,
        'destroy': ClientLocationSerializer,
    }
