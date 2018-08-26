from django_filters.rest_framework import FilterSet
from django_filters.filters import OrderingFilter

from v1.tags.models.tag import Tag


class AdminTagFilter(FilterSet):
    o = OrderingFilter(
        fields=(
            ('name', 'name'),
            ('slug', 'slug'),
        )
    )

    class Meta:
        model = Tag
        fields = []
