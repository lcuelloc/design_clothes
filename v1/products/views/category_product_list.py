from django.core.exceptions import PermissionDenied
from django.db import IntegrityError

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from v1.products.models.category_product import CategoryProduct
from v1.products.serializers.category_product import CategoryProductSerializer


class CategoryProductList(generics.ListCreateAPIView):
    """
    Association between category and products
    """

    # authentication_classes = []
    permission_classes = []
    queryset = CategoryProduct.objects.all()
    serializer_class = CategoryProductSerializer

    def post(self, request, *args, **kwargs):
        try:
            if not request.user.is_superuser:
                raise PermissionDenied("You cannot create category product")
            return super().post(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"response": "Category Product already created"},
                status=status.HTTP_400_BAD_REQUEST,
            )
