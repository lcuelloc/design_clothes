from django.core.exceptions import PermissionDenied
from django.db import IntegrityError

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from v1.products.models.product import Product
from v1.products.serializers.product import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    """
    Get list of all products and admin create
    """

    # authentication_classes = []
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        print(request.user)
        try:
            if not request.user.is_superuser:
                raise PermissionDenied("You cannot create a new Product")
            return super().post(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"response": "Product already created"},
                status=status.HTTP_400_BAD_REQUEST,
            )
