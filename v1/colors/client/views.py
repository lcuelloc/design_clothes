from rest_framework import generics
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from v1.colors.models.product_color import ProductColor
from v1.colors.client.serializers import ClientProductColorListSerializer
from v1.colors.client.filters import ClientProductColorFilter
from v1.utils.views.paginators import NumPagesPagination


# v1/client/product-colors/
class ClientProductColorListView(generics.ListAPIView):
    queryset = ProductColor.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filter_class = ClientProductColorFilter
    search_fields = []
    pagination_class = NumPagesPagination
    authentication_classes = []
    serializer_class = ClientProductColorListSerializer
