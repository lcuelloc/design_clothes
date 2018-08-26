from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.products.models.product_type import ProductType
from v1.products.serializers.product_type import AdminProductTypeSerializer
from v1.utils.views.mixins import MultiSerializerViewSetMixin
from v1.utils.views.paginators import NumPagesPagination


# v1/admin/product-types/
class AdminProductTypeView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = ProductType.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = NumPagesPagination
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_action_classes = {
        'create': AdminProductTypeSerializer,
        'list': AdminProductTypeSerializer,
        'update': AdminProductTypeSerializer,
        'partial_update': AdminProductTypeSerializer,
    }
