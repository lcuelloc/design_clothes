from django_filters.rest_framework import FilterSet
from django_filters.filters import OrderingFilter

from v1.images.models.image import Image


class AdminImageFilter(FilterSet):
    o = OrderingFilter(
        fields=(
            ('path', 'path'),
        )
    )

    class Meta:
        model = Image
        fields = []
