from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.colors.models.color import Color
from v1.colors.serializers.product_color import AdminProductColorSerializer


class AdminColorSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    product_color = AdminProductColorSerializer(many=True, required=False)

    class Meta:
        model = Color
        fields = ["id", "name", "slug", "img", "product_color"]
        lookup_field = "slug"
        extra_kwargs = {
            'slug': {'read_only': True}
        }
        expandable_fields = {
            'product_colors': (AdminProductColorSerializer, (), {'many': True}),
            }
