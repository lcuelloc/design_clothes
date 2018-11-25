from rest_framework import generics
from rest_framework import filters
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import action

from django_filters.rest_framework import DjangoFilterBackend

from v1.products.models.product import Product
from v1.products.client.serializers import ClientProductListSerializer
from v1.products.client.filters import ClientProductFilter
from v1.utils.views.paginators import NumPagesPagination


# v1/client/products/first/
class ClientFirstProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    authentication_classes = []

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        result = qs.get(slug='polera-hombre-dogo')
        serializer = ClientProductListSerializer(result)
        return Response({"result": serializer.data}, status=status.HTTP_200_OK)


# v1/client/products/
class ClientProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = ClientProductFilter
    search_fields = []
    pagination_class = NumPagesPagination
    authentication_classes = []
    serializer_class = ClientProductListSerializer
