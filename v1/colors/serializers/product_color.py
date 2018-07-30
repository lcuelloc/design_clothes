from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.colors.models.product_color import ProductColor


class ProductColorSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ["pk", "color", "product_type"]
