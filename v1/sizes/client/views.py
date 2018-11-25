from rest_framework import generics
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from v1.sizes.models.product_size import ProductSize
from v1.sizes.client.serializers import ClientProductColorListSerializer
from v1.sizes.client.filters import ClientProductSizeFilter
from v1.utils.views.paginators import NumPagesPagination


# v1/client/product-sizes/
class ClientProductSizeListView(generics.ListAPIView):
    queryset = ProductSize.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filter_class = ClientProductSizeFilter
    search_fields = []
    pagination_class = NumPagesPagination
    authentication_classes = []
    serializer_class = ClientProductColorListSerializer
