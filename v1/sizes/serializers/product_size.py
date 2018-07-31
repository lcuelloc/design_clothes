from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.sizes.models.product_size import ProductSize


class ProductSizeSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ["pk", "size", "product_color"]
