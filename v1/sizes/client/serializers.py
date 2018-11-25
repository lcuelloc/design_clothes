from rest_framework import serializers

from v1.sizes.models.product_size import ProductSize
from v1.sizes.models.size import Size


class ClientSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = ["id", "name"]


class ClientProductColorListSerializer(serializers.ModelSerializer):
    size = ClientSizeSerializer()

    class Meta:
        model = ProductSize
        fields = ["pk", "stock", "size", "product_color"]
