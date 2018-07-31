from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.colors.models.product_color import ProductColor
from v1.sizes.serializers.product_size import ProductSizeSerializer
from v1.images.serializers.image import ImageSerializer


class ProductColorSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    product_size = ProductSizeSerializer(many=True, required=False)
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = ProductColor
        fields = ["pk", "color", "product_type", "product_size", "images"]
        expandable_fields = {
            'product_sizes': (ProductSizeSerializer, (), {'many': True}),
            'images': (ImageSerializer, (), {'many': True}),
            }
