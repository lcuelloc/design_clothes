from rest_framework import serializers

from v1.products.models.product import Product


class AdminProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "name", "slug"]
        lookup_field = "slug"
        extra_kwargs = {"slug": {"read_only": True}}
