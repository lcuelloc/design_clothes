from rest_framework import serializers

from v1.products.models.category_product import CategoryProduct


class AdminCategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProduct
        fields = ["category", "product"]
