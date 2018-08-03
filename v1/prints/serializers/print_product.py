from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.prints.models.print_product import PrintProduct


class AdminPrintProductSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = PrintProduct
        fields = ["id", "print", "product_type"]
