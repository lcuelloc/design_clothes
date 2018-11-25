from rest_framework import serializers

from v1.designs.models.design import Design
from v1.designs.models.category_design import CategoryDesign


class ClientDesignSerializer(serializers.ModelSerializer):

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


class ClientCategoryDesignSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryDesign
        fields = ["id", "name", "slug", "parent"]


class ClientDesignListSerializer(serializers.ModelSerializer):
    # category_design = ClientCategoryDesignSerializer()

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
