from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.prints.models.print_product import PrintProduct
from v1.prints.serializers.print_product import AdminPrintProductSerializer
from v1.utils.views.mixins import MultiSerializerViewSetMixin
from v1.utils.views.paginators import NumPagesPagination


# v1/admin/print-products/
class AdminPrintProductView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = PrintProduct.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = NumPagesPagination
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_action_classes = {
        'create': AdminPrintProductSerializer,
        'list': AdminPrintProductSerializer,
        'update': AdminPrintProductSerializer,
        'partial_update': AdminPrintProductSerializer,
    }
