from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.products.models.product import Product
from v1.products.serializers.product import AdminProductSerializer
from v1.products.serializers.product import AdminProductListSerializer
from v1.products.filters.product import AdminProductFilter
from v1.utils.views.mixins import MultiSerializerViewSetMixin
from v1.utils.views.paginators import NumPagesPagination


# v1/admin/products/
class AdminProductView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = AdminProductFilter
    pagination_class = NumPagesPagination
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_action_classes = {
        'create': AdminProductSerializer,
        'list': AdminProductListSerializer,
        'update': AdminProductSerializer,
        'partial_update': AdminProductSerializer,
    }
