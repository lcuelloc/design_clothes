from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.colors.models.product_color import ProductColor
from v1.sizes.serializers.product_size import AdminProductSizeSerializer
from v1.images.serializers.image import AdminImageSerializer


class AdminProductColorSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    product_size = AdminProductSizeSerializer(many=True, required=False)
    images = AdminImageSerializer(many=True, required=False)

    class Meta:
        model = ProductColor
        fields = ["pk", "color", "product_type", "product_size", "images"]
        expandable_fields = {
            'product_sizes': (AdminProductSizeSerializer, (), {'many': True}),
            'images': (AdminImageSerializer, (), {'many': True}),
            }
