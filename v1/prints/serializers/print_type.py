from rest_framework import serializers

from v1.prints.models.print_type import PrintType


class AdminPrintTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrintType
        fields = ["id", "name", "slug", "description", "price"]
        lookup_field = "slug"
        extra_kwargs = {"slug": {"read_only": True}}
