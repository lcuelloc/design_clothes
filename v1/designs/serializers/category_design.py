from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from v1.designs.models.category_design import CategoryDesign


class AdminCategoryDesignSerializer(serializers.ModelSerializer):
    children = RecursiveField(required=False, allow_null=True, many=True)

    class Meta:
        model = CategoryDesign
        fields = ["id", "name", "slug", "parent", "children"]
        lookup_field = "slug"
        extra_kwargs = {"slug": {"read_only": True}}
