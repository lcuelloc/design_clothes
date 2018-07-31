from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.categories.models.category import Category
from v1.products.serializers.product import CategoryProductSerializer

# from v1.items.serializers.item import ItemSerializer


class CategorySerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    category_product = CategoryProductSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "category_product"]
        lookup_field = "slug"
        extra_kwargs = {"slug": {"read_only": True}}
        expandable_fields = {
            "category_products": (CategoryProductSerializer, (), {"many": True})
        }
        # expandable_fields = {
        #    'items': (ItemSerializer, (), {'many': True}),
        #    }
