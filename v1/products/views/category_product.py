from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.products.models.category_product import CategoryProduct
from v1.products.serializers.category_product import AdminCategoryProductSerializer
from v1.utils.views.mixins import MultiSerializerViewSetMixin
from v1.utils.views.paginators import NumPagesPagination


# v1/admin/category-products/
class AdminCategoryProductView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = CategoryProduct.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = NumPagesPagination
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_action_classes = {
        'create': AdminCategoryProductSerializer,
        'list': AdminCategoryProductSerializer,
        'update': AdminCategoryProductSerializer,
        'partial_update': AdminCategoryProductSerializer,
    }
