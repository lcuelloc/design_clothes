from rest_framework import serializers

from v1.colors.models.product_color import ProductColor


class AdminProductColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductColor
        fields = ["pk", "color", "product_type"]
