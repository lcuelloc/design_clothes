from django.db import IntegrityError

from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.designs.models.design import Design
from v1.designs.serializers.design import AdminDesignSerializer
from v1.designs.filters.design import AdminDesignFilter
from v1.designs.models.category_design import CategoryDesign
from v1.utils.views.mixins import MultiSerializerViewSetMixin
from v1.utils.views.paginators import NumPagesPagination


# v1/admin/designs/
class AdminDesignView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Design.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = NumPagesPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = AdminDesignFilter
    search_fields = []
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_action_classes = {
        'create': AdminDesignSerializer,
        'list': AdminDesignSerializer,
        'update': AdminDesignSerializer,
        'partial_update': AdminDesignSerializer,
    }

    # category_design assignment
    def create(self, request, *args, **kwargs):
        try:
            if "category_design" in request.data:
                cat_id = request.data["category_design"]
                category = CategoryDesign.objects.get(pk=cat_id)
                if category.parent:
                    return super().create(request, *args, **kwargs)
                else:
                    return Response(
                        {"response": "Cannot assign design to a parent category"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            return Response(
                {"response": "Missing fields"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except IntegrityError as e:
            return Response(
                {"response": "Desgin already created"},
                status=status.HTTP_400_BAD_REQUEST,
            )
