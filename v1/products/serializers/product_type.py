from rest_framework import serializers

from v1.products.models.product_type import ProductType


class AdminProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = ["pk", "name", "html_content", "price", "slug", "category_product"]
        lookup_field = "slug"
        extra_kwargs = {"slug": {"read_only": True}}
