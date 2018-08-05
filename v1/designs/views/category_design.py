from django.db import IntegrityError

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework import status

from v1.designs.models.category_design import CategoryDesign
from v1.designs.serializers.category_design import AdminCategoryDesignSerializer
from v1.utils.views.mixins import MultiSerializerViewSetMixin


class AdminCategoryDesignView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = CategoryDesign.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = AdminCategoryDesignSerializer

    def create(self, request, *args, **kwargs):
        try:
            parent = request.data["parent"]
            if not parent:
                return super().create(request, *args, **kwargs)
            else:
                ca_parent = CategoryDesign.objects.get(pk=parent)
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
