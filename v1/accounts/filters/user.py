from django_filters.rest_framework import FilterSet
from django_filters.filters import OrderingFilter

from v1.accounts.models.user import User


class AdminUserFilter(FilterSet):
    o = OrderingFilter(
        fields=(
            ('last_name', 'last_name'),
            ('email', 'email'),
            ('is_active', 'is_active'),
        )
    )

    class Meta:
        model = User
        fields = ['last_name', 'email', 'is_active']
