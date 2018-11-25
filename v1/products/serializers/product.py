from rest_framework import serializers

from v1.products.models.product import Product
from v1.categories.models.category import Category


class AdminProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["pk", "name", "thumbnail", "html_content", "price", "slug", "category"]
        lookup_field = "slug"
        extra_kwargs = {"slug": {"read_only": True}}


class AdminCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name"]


class AdminProductListSerializer(serializers.ModelSerializer):
    category = AdminCategorySerializer()

    class Meta:
        model = Product
        fields = ["pk", "name", "thumbnail", "html_content", "price", "slug", "category"]
        lookup_field = "slug"
        extra_kwargs = {"slug": {"read_only": True}}
