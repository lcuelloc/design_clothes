from rest_framework import serializers

from v1.categories.models.category import Category


class AdminCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name", "slug"]
        lookup_field = "slug"
        extra_kwargs = {"slug": {"read_only": True}}
