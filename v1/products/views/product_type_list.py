from django.core.exceptions import PermissionDenied
from django.db import IntegrityError

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from v1.products.models.product_type import ProductType
from v1.products.serializers.product_type import ProductTypeSerializer


class ProductTypeList(generics.ListCreateAPIView):
    """
    Association between category and products
    """

    # authentication_classes = []
    permission_classes = []
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

    def post(self, request, *args, **kwargs):
        try:
            if not request.user.is_superuser:
                raise PermissionDenied("You cannot create product type")
            return super().post(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"response": "Product type already created"},
                status=status.HTTP_400_BAD_REQUEST,
            )
