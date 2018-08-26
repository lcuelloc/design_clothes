from django_filters.rest_framework import FilterSet
from django_filters.filters import OrderingFilter

from v1.sizes.models.size import Size


class AdminSizeFilter(FilterSet):
    o = OrderingFilter(
        fields=(
            ('name', 'name'),
        )
    )

    class Meta:
        model = Size
        fields = []
