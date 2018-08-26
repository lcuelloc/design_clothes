from django_filters.rest_framework import FilterSet
from django_filters.filters import OrderingFilter

from v1.designs.models.category_design import CategoryDesign


class AdminCategoryDesignFilter(FilterSet):
    o = OrderingFilter(
        fields=(
            ('parent', 'parent'),
            ('name', 'name'),
            ('slug', 'slug'),
        )
    )

    class Meta:
        model = CategoryDesign
        fields = []
