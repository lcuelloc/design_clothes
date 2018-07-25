from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.sizes.models.size import Size


class SizeSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ["id", "name"]
