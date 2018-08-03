from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.prints.models.print import Print
from v1.prints.serializers.print_product import AdminPrintProductSerializer


class AdminPrintSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    print_product = AdminPrintProductSerializer(many=True, required=False)

    class Meta:
        model = Print
        fields = ["id", "name", "slug", "description", "price", "print_product"]
        lookup_field = "slug"
        extra_kwargs = {"slug": {"read_only": True}}
        expandable_fields = {
            "print_products": (AdminPrintProductSerializer, (), {"many": True})
        }
