from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.colors.models.color import Color


class ColorSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["id", "name", "slug", "img"]
        lookup_field = "slug"
        extra_kwargs = {
            'slug': {'read_only': True}
        }
