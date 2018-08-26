from rest_framework import serializers

from v1.prints.models.print_product import PrintProduct


class AdminPrintProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrintProduct
        fields = ["id", "print_type", "product_type"]
