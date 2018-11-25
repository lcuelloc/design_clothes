from rest_framework import generics
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from v1.designs.models.design import Design
from v1.designs.models.category_design import CategoryDesign
from v1.designs.client.serializers import ClientDesignListSerializer
from v1.designs.client.serializers import ClientCategoryDesignSerializer
from v1.designs.client.filters import ClientDesignFilter
from v1.designs.client.filters import ClientCategoryDesignFilter
from v1.utils.views.paginators import NumPagesPagination


# v1/client/designs/
class ClientDesignListView(generics.ListAPIView):
    queryset = Design.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filter_class = ClientDesignFilter
    search_fields = []
    pagination_class = NumPagesPagination
    authentication_classes = []
    serializer_class = ClientDesignListSerializer


# v1/client/category-designs/
class ClientCategoryDesignListView(generics.ListAPIView):
    queryset = CategoryDesign.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filter_class = ClientCategoryDesignFilter
    search_fields = []
    pagination_class = NumPagesPagination
    authentication_classes = []
    # serializer_class = ClientCategoryDesignSerializer

    def list(self, request, *args, **kwargs):
        # import ipdb; ipdb.set_trace()
        qs = self.filter_queryset(self.get_queryset())
        not_parent = request.query_params.get("p")
        result = qs
        if not_parent:
            if not_parent == '0':
                # return null values
                result = qs.filter(parent__isnull=True)
            else:
                result = qs.filter(parent__isnull=False)

        serializer = ClientCategoryDesignSerializer(result, many=True)

        return Response({"result": serializer.data}, status=status.HTTP_200_OK)
