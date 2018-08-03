from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.tags.models.tag import Tag
from v1.tags.serializers.tag import AdminTagSerializer
from v1.utils.views.mixins import MultiSerializerViewSetMixin


class AdminTagView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Tag.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = AdminTagSerializer
