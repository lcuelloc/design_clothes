from django.core.exceptions import PermissionDenied
from django.db import IntegrityError

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from v1.colors.models.product_color import ProductColor
from v1.colors.serializers.product_color import ProductColorSerializer


class ProductColorList(generics.ListCreateAPIView):
    """
    Get list of all colors and admin create
    """

    # authentication_classes = []
    permission_classes = []
    queryset = ProductColor.objects.all()
    serializer_class = ProductColorSerializer

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
