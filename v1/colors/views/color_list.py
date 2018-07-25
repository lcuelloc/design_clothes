from django.core.exceptions import PermissionDenied
from django.db import IntegrityError

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from v1.colors.models.color import Color
from v1.colors.serializers.color import ColorSerializer


class ColorList(generics.ListCreateAPIView):
    """
    Get list of all categories and admin create
    """

    # authentication_classes = []
    permission_classes = []
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

    def post(self, request, *args, **kwargs):
        try:
            if request.user.is_superuser == False:
                raise PermissionDenied("You cannot create a new color")
            return super().post(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"response": "Color already created"},
                status=status.HTTP_400_BAD_REQUEST,
            )
