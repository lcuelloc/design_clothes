from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.accounts.models.user import User
from v1.accounts.serializers.user import AdminUserSerializer
from v1.accounts.filters.user import AdminUserFilter
from v1.utils.views.mixins import MultiSerializerViewSetMixin
from v1.utils.views.paginators import NumPagesPagination


# v1/admin/users/
class AdminUserView(
    MultiSerializerViewSetMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = NumPagesPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = AdminUserFilter
    search_fields = ['last_name', 'email']
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_action_classes = {
        'create': AdminUserSerializer,
        'list': AdminUserSerializer,
        'update': AdminUserSerializer,
        'partial_update': AdminUserSerializer,
    }
