from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.colors.models.product_color import ProductColor
from v1.sizes.serializers.product_size import ProductSizeSerializer


class ProductColorSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    product_size = ProductSizeSerializer(many=True)

    class Meta:
        model = ProductColor
        fields = ["pk", "color", "product_type"]
