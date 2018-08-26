from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.tags.models.tag import Tag
from v1.tags.serializers.tag import AdminTagSerializer
from v1.tags.filters.tag import AdminTagFilter
from v1.utils.views.mixins import MultiSerializerViewSetMixin
from v1.utils.views.paginators import NumPagesPagination


# v1/admin/tags/
class AdminTagView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Tag.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = NumPagesPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = AdminTagFilter
    search_fields = []
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = AdminTagSerializer
    serializer_action_classes = {
        'create': AdminTagSerializer,
        'list': AdminTagSerializer,
        'update': AdminTagSerializer,
        'partial_update': AdminTagSerializer,
    }
