from django.core.exceptions import PermissionDenied
from django.db import IntegrityError

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from v1.sizes.models.product_size import ProductSize
from v1.sizes.serializers.product_size import ProductSizeSerializer


class ProductSizeList(generics.ListCreateAPIView):
    """
    Get list of all colors and admin create
    """

    # authentication_classes = []
    permission_classes = []
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer

    def post(self, request, *args, **kwargs):
        try:
            if not request.user.is_superuser:
                raise PermissionDenied("You cannot create a new instance")
            return super().post(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"response": "Association already created"},
                status=status.HTTP_400_BAD_REQUEST,
            )
