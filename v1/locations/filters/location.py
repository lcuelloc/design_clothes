from django_filters.rest_framework import FilterSet
from django_filters.filters import OrderingFilter

from v1.locations.models.location import Location


class AdminLocationFilter(FilterSet):
    o = OrderingFilter(
        fields=(
            ('region', 'region'),
            ('city', 'city'),
            ('commune', 'commune'),
            ('address', 'address'),
            ('number', 'number'),
            ('alias', 'alias'),
        )
    )

    class Meta:
        model = Location
        fields = []
