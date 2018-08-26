from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.prints.models.print_type import PrintType
from v1.prints.serializers.print_type import AdminPrintTypeSerializer
from v1.prints.filters.print_type import AdminPrintTypeFilter
from v1.utils.views.mixins import MultiSerializerViewSetMixin
from v1.utils.views.paginators import NumPagesPagination


# v1/admin/print_types/
class AdminPrintTypeView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = PrintType.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = NumPagesPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = AdminPrintTypeFilter
    search_fields = []
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_action_classes = {
        'create': AdminPrintTypeSerializer,
        'list': AdminPrintTypeSerializer,
        'update': AdminPrintTypeSerializer,
        'partial_update': AdminPrintTypeSerializer,
    }
