from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.products.models.category_product import CategoryProduct
from v1.products.serializers.product_type import AdminProductTypeSerializer


class AdminCategoryProductSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    product_type = AdminProductTypeSerializer(many=True, required=False)

    class Meta:
        model = CategoryProduct
        fields = ["category", "product", "product_type"]
        expandable_fields = {
            'product_types': (AdminProductTypeSerializer, (), {'many': True}),
            }
