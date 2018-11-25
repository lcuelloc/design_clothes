from rest_framework import serializers

from v1.categories.models.category import Category


class ClientCategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name", "slug"]
