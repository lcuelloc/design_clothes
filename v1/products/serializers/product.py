from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.products.models.product import Product


class ProductSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "slug"]
        lookup_field = "slug"
        extra_kwargs = {
            'slug': {'read_only': True}
        }
