from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.sizes.models.size import Size
from v1.sizes.serializers.product_size import ProductSizeSerializer


class SizeSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    product_size = ProductSizeSerializer(many=True, required=False)

    class Meta:
        model = Size
        fields = ["id", "name", "product_size"]
        expandable_fields = {
            'product_size': (ProductSizeSerializer, (), {'many': True}),
            }
