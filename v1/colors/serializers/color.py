from rest_framework import serializers

from v1.colors.models.color import Color


class AdminColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ["id", "name", "slug", "img"]
        lookup_field = "slug"
        extra_kwargs = {
            'slug': {'read_only': True}
        }
