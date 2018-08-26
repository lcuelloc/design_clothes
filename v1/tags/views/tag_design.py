from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.tags.models.tag_design import TagDesign
from v1.tags.serializers.tag_design import AdminTagDesignSerializer
from v1.utils.views.mixins import MultiSerializerViewSetMixin
from v1.utils.views.paginators import NumPagesPagination


# v1/admin/tag-designs/
class AdminTagDesignView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = TagDesign.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = NumPagesPagination
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_action_classes = {
        'create': AdminTagDesignSerializer,
        'list': AdminTagDesignSerializer,
        'update': AdminTagDesignSerializer,
        'partial_update': AdminTagDesignSerializer,
    }
