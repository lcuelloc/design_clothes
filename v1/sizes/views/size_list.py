from django.core.exceptions import PermissionDenied
from django.db import IntegrityError

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from v1.sizes.models.size import Size
from v1.sizes.serializers.size import SizeSerializer


class SizeList(generics.ListCreateAPIView):
    """
    Get list of all categories and admin create
    """

    # authentication_classes = []
    permission_classes = []
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

    def post(self, request, *args, **kwargs):
        try:
            if request.user.is_superuser == False:
                raise PermissionDenied("You cannot create a new size")
            return super().post(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"response": "Size already created"}, status=status.HTTP_400_BAD_REQUEST
            )
