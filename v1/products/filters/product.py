from django_filters.rest_framework import FilterSet
from django_filters.filters import OrderingFilter

from v1.products.models.product import Product


class AdminProductFilter(FilterSet):
    o = OrderingFilter(
        fields=(
            ('name', 'name'),
            ('slug', 'slug'),
        )
    )

    class Meta:
        model = Product
        fields = []
