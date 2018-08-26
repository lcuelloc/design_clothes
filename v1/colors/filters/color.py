from django_filters.rest_framework import FilterSet
from django_filters.filters import OrderingFilter

from v1.colors.models.color import Color


class AdminColorFilter(FilterSet):
    o = OrderingFilter(
        fields=(
            ('name', 'name'),
            ('slug', 'slug'),
        )
    )

    class Meta:
        model = Color
        fields = []
