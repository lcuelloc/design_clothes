from django_filters.rest_framework import FilterSet
from django_filters.filters import OrderingFilter

from v1.designs.models.design import Design


class AdminDesignFilter(FilterSet):
    o = OrderingFilter(
        fields=(
            ('name', 'name'),
            ('slug', 'slug'),
            ('is_custom', 'is_custom'),
        )
    )

    class Meta:
        model = Design
        fields = []
