from django.core.exceptions import PermissionDenied
from django.db import IntegrityError

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from v1.categories.models.category import Category
from v1.categories.serializers.category import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    """
    Get list of all categories and admin create
    """

    # authentication_classes = []
    permission_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        try:
            if request.user.is_superuser == False:
                raise PermissionDenied("You cannot create a new category")
            return super().post(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"response": "Category already created"},
                status=status.HTTP_400_BAD_REQUEST,
            )
