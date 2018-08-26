from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django_filters.rest_framework import DjangoFilterBackend

from v1.colors.models.color import Color
from v1.colors.serializers.color import AdminColorSerializer
from v1.colors.filters.color import AdminColorFilter
from v1.utils.views.mixins import MultiSerializerViewSetMixin
from v1.utils.views.paginators import NumPagesPagination


# v1/admin/colors/
class AdminColorView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Color.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = NumPagesPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = AdminColorFilter
    search_fields = []
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_action_classes = {
        'create': AdminColorSerializer,
        'list': AdminColorSerializer,
        'update': AdminColorSerializer,
        'partial_update': AdminColorSerializer,
    }
