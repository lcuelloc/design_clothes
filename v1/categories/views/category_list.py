from django.core.exceptions import PermissionDenied

from rest_framework import generics

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
        if request.user.is_superuser == False:
            raise PermissionDenied("You cannot create a new category")
        return super().post(request, *args, **kwargs)
