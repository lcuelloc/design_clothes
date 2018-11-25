import logging

import django_filters as df
from django_filters.rest_framework import FilterSet

from v1.designs.models.design import Design
from v1.designs.models.category_design import CategoryDesign


logging.getLogger(__name__)


class ClientDesignFilter(FilterSet):
    #event_code = df.CharFilter(field_name="dispatchpalletregister__event__code")
    #box_code = df.CharFilter(field_name="palletbox__box__code")

    class Meta:
        model = Design
        fields = [
            "id",
            "name",
            "slug",
            "img",
            "is_custom",
            "height",
            "width",
            "category_design",
        ]


class ClientCategoryDesignFilter(FilterSet):
    #event_code = df.CharFilter(field_name="dispatchpalletregister__event__code")
    #box_code = df.CharFilter(field_name="palletbox__box__code")

    class Meta:
        model = CategoryDesign
        fields = ["id", "name", "slug", "parent"]
