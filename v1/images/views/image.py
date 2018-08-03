from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.images.models.image import Image
from v1.images.serializers.image import AdminImageSerializer
from v1.utils.views.mixins import MultiSerializerViewSetMixin


class AdminImageView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Image.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = AdminImageSerializer
