from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.products.models.product_type import ProductType
from v1.colors.serializers.product_color import AdminProductColorSerializer


class AdminProductTypeSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    product_color = AdminProductColorSerializer(many=True, required=False)

    class Meta:
        model = ProductType
        fields = ["pk", "name", "html_content", "price", "slug", "category_product", "product_color"]
        lookup_field = "slug"
        extra_kwargs = {"slug": {"read_only": True}}
        expandable_fields = {
            'product_colors': (AdminProductColorSerializer, (), {'many': True}),
            }
