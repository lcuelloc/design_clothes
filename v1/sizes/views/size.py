from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.sizes.models.size import Size
from v1.sizes.serializers.size import AdminSizeSerializer
from v1.utils.views.mixins import MultiSerializerViewSetMixin


class AdminSizeView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Size.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = AdminSizeSerializer
