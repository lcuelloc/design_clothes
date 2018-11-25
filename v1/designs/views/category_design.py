from django.db import IntegrityError

from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend

from v1.designs.models.category_design import CategoryDesign
from v1.designs.serializers.category_design import AdminCategoryDesignSerializer
from v1.designs.serializers.category_design import AdminCategoryDesignDetailSerializer
from v1.designs.serializers.category_design import AdminCategoryDesignParentSerializer
from v1.designs.filters.category_design import AdminCategoryDesignFilter
from v1.utils.views.mixins import MultiSerializerViewSetMixin
from v1.utils.views.paginators import NumPagesPagination


# v1/admin/category-designs/
class AdminCategoryDesignView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.DestroyModelMixin,
):

    queryset = CategoryDesign.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = NumPagesPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = AdminCategoryDesignFilter
    search_fields = []
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_action_classes = {
        "create": AdminCategoryDesignSerializer,
        "list": AdminCategoryDesignParentSerializer,
        "update": AdminCategoryDesignSerializer,
        "partial_update": AdminCategoryDesignSerializer,
        "retrieve": AdminCategoryDesignDetailSerializer,
        "destroy": AdminCategoryDesignDetailSerializer,
    }

    def create(self, request, *args, **kwargs):
        try:
            if not request.data['parent']:
                return super().create(request, *args, **kwargs)
            else:
                ca_parent = CategoryDesign.objects.get(pk=request.data["parent"])
                if not ca_parent.parent:
                    return super().create(request, *args, **kwargs)
                else:
                    return Response(
                        {"response": "Cannot create a new level"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
        except IntegrityError as e:
            return Response(
                {"response": "Category already created"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    # v1/admin/category-designs/parents
    @action(
        methods=["get"],
        detail=False,
        permission_classes=[IsAuthenticated],
    )
    def parents(self, request, pk=None):
        #import ipdb; ipdb.set_trace()
        qs = self.get_queryset()
        result = qs.filter(parent=None)
        serializer = AdminCategoryDesignSerializer(result, many=True)
        return Response({"results": serializer.data}, status=status.HTTP_200_OK)