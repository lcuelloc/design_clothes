from django.db import IntegrityError

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework import status

from v1.designs.models.design import Design
from v1.designs.serializers.design import AdminDesignSerializer
from v1.designs.models.category_design import CategoryDesign
from v1.utils.views.mixins import MultiSerializerViewSetMixin


class AdminDesignView(
    MultiSerializerViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Design.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = AdminDesignSerializer

    def create(self, request, *args, **kwargs):
        try:
            # import ipdb; ipdb.set_trace()
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
