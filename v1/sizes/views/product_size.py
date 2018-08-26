from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.sizes.models.product_size import ProductSize
from v1.sizes.serializers.product_size import AdminProductSizeSerializer
from v1.utils.views.mixins import MultiSerializerViewSetMixin
from v1.utils.views.paginators import NumPagesPagination


# v1/admin/product-sizes/
class AdminProductSizeView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = ProductSize.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = NumPagesPagination
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_action_classes = {
        'create': AdminProductSizeSerializer,
        'list': AdminProductSizeSerializer,
        'update': AdminProductSizeSerializer,
        'partial_update': AdminProductSizeSerializer,
    }
