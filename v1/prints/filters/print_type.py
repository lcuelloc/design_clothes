from django_filters.rest_framework import FilterSet
from django_filters.filters import OrderingFilter

from v1.prints.models.print_type import PrintType


class AdminPrintTypeFilter(FilterSet):
    o = OrderingFilter(
        fields=(
            ('name', 'name'),
            ('slug', 'slug'),
            ('price', 'price'),
        )
    )

    class Meta:
        model = PrintType
        fields = []
