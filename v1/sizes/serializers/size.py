from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.sizes.models.size import Size
from v1.sizes.serializers.product_size import AdminProductSizeSerializer


class AdminSizeSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    #product_size = AdminProductSizeSerializer(many=True, required=False)

    class Meta:
        model = Size
        fields = ["id", "name"]
        #expandable_fields = {
        #    'product_size': (AdminProductSizeSerializer, (), {'many': True}),
        #    }
