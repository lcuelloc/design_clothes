import django_filters as df
from django_filters.rest_framework import FilterSet

from v1.sizes.models.product_size import ProductSize


class ClientProductSizeFilter(FilterSet):

    class Meta:
        model = ProductSize
        fields = ["id", "stock", "size", "product_color"]
