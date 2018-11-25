from rest_framework import serializers

from v1.colors.models.product_color import ProductColor
from v1.colors.models.color import Color
from v1.products.models.product import Product
from v1.prints.models.print_product import PrintProduct
from v1.prints.models.print_type import PrintType
from v1.images.models.image import Image


class ClientImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ["id", "name", "path"]


class ClientPrintTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrintType
        fields = ["id", "name", "slug", "description", "price"]


class ClientPrintProductSerializer(serializers.ModelSerializer):
    print_type = ClientPrintTypeSerializer()

    class Meta:
        model = PrintProduct
        fields = ["id", "print_type"]


class ClientProductListSerializer(serializers.ModelSerializer):
    print_products = ClientPrintProductSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "pk",
            "name",
            "thumbnail",
            "html_content",
            "price",
            "slug",
            "category",
            "print_products",
        ]


class ClientColorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ["id", "name", "slug", "img"]


class ClientProductColorListSerializer(serializers.ModelSerializer):
    color = ClientColorListSerializer()
    product = ClientProductListSerializer()
    images = ClientImageSerializer(many=True)

    class Meta:
        model = ProductColor
        fields = ["pk", "color", "product", "images"]
