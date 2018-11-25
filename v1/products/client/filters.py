import logging

import django_filters as df
from django_filters.rest_framework import FilterSet

from v1.products.models.product import Product


logging.getLogger(__name__)


class ClientProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = ["id", "name", "thumbnail", "html_content", "price", "slug", "category"]
