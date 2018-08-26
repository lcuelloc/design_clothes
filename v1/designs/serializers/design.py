from rest_framework import serializers

from v1.designs.models.design import Design


class AdminDesignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Design
        fields = [
            "pk",
            "name",
            "slug",
            "img",
            "is_custom",
            "height",
            "width",
            "category_design",
        ]
        lookup_field = "slug"
        extra_kwargs = {"slug": {"read_only": True}}
