from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.products.models.product_type import ProductType
from v1.colors.serializers.product_color import ProductColorSerializer


class ProductTypeSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    product_color = ProductColorSerializer(many=True)

    class Meta:
        model = ProductType
        fields = ["pk", "name", "html_content", "price", "slug", "category_product"]
        lookup_field = "slug"
        extra_kwargs = {"slug": {"read_only": True}}
