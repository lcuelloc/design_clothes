from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.categories.models.category import Category
from v1.categories.serializers.category import AdminCategorySerializer
from v1.utils.views.mixins import MultiSerializerViewSetMixin


class AdminCategoryView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = AdminCategorySerializer
