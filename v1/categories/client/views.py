from rest_framework import generics

from v1.categories.models.category import Category
from v1.categories.client.serializers import ClientCategoryListSerializer
from v1.utils.views.paginators import NumPagesPagination


# v1/client/categories/
class ClientCategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    pagination_class = NumPagesPagination
    authentication_classes = []
    serializer_class = ClientCategoryListSerializer
