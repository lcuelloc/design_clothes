from rest_framework import serializers

from v1.sizes.models.product_size import ProductSize


class AdminProductSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSize
        fields = ["pk", "stock", "size", "product_color"]
