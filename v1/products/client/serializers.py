from rest_framework import serializers

from v1.products.models.product import Product


class ClientProductListSerializer(serializers.ModelSerializer):
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
        ]
