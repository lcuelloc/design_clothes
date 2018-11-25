import logging

import django_filters as df
from django_filters.rest_framework import FilterSet

from v1.colors.models.product_color import ProductColor
from v1.colors.models.color import Color


logging.getLogger(__name__)


class ClientProductColorFilter(FilterSet):

    class Meta:
        model = ProductColor
        fields = ["id", "color", "product"]
