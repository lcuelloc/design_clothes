from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.products.models.category_product import CategoryProduct
from v1.products.serializers.product_type import ProductTypeSerializer


class CategoryProductSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    product_type = ProductTypeSerializer(many=True)

    class Meta:
        model = CategoryProduct
        fields = ["category", "product"]
