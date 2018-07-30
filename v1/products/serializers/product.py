from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.products.models.product import Product
from v1.products.serializers.category_product import CategoryProductSerializer


class ProductSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    category_product = CategoryProductSerializer(many=True)

    class Meta:
        model = Product
        fields = ["id", "name", "slug"]
        lookup_field = "slug"
        extra_kwargs = {"slug": {"read_only": True}}
