from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.products.models.product import Product
from v1.products.serializers.category_product import AdminCategoryProductSerializer


class AdminProductSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    category_product = AdminCategoryProductSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ["id", "name", "slug", "category_product"]
        lookup_field = "slug"
        extra_kwargs = {"slug": {"read_only": True}}
        expandable_fields = {
            'category_products': (AdminCategoryProductSerializer, (), {'many': True}),
            }
