from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.colors.models.color import Color
from v1.colors.serializers.product_color import ProductColorSerializer


class ColorSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    product_color = ProductColorSerializer(many=True, required=False)

    class Meta:
        model = Color
        fields = ["id", "name", "slug", "img", "product_color"]
        lookup_field = "slug"
        extra_kwargs = {
            'slug': {'read_only': True}
        }
        expandable_fields = {
            'product_colors': (ProductColorSerializer, (), {'many': True}),
            }
