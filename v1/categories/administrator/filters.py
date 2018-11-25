from django_filters.rest_framework import FilterSet
from django_filters.filters import OrderingFilter

from v1.categories.models.category import Category


class AdminCategoryFilter(FilterSet):
    o = OrderingFilter(
        fields=(
            ('name', 'name'),
            ('slug', 'slug'),
        )
    )

    class Meta:
        model = Category
        fields = []
