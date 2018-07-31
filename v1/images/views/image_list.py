from django.core.exceptions import PermissionDenied
from django.db import IntegrityError

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from v1.images.models.image import Image
from v1.images.serializers.image import ImageSerializer


class ImageList(generics.ListCreateAPIView):
    """
    Add images to product
    """

    # authentication_classes = []
    permission_classes = []
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        try:
            if not request.user.is_superuser:
                raise PermissionDenied("You cannot create a new instance")
            return super().post(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"response": "Image already created"},
                status=status.HTTP_400_BAD_REQUEST,
            )
