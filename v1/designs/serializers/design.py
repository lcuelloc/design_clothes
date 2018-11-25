from rest_framework import serializers

from v1.designs.models.design import Design
from v1.designs.models.category_design import CategoryDesign


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


class AdminCategoryDesignSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryDesign
        fields = ["id", "name", "slug", "parent"]


class AdminDesignListSerializer(serializers.ModelSerializer):
    category_design = AdminCategoryDesignSerializer()

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
