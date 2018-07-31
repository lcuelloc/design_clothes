from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.products.models.category_product import CategoryProduct
from v1.products.serializers.product_type import ProductTypeSerializer


class CategoryProductSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    product_type = ProductTypeSerializer(many=True, required=False)

    class Meta:
        model = CategoryProduct
        fields = ["category", "product", "product_type"]
        expandable_fields = {
            'product_types': (ProductTypeSerializer, (), {'many': True}),
            }
