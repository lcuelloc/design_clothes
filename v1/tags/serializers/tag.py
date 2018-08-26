from rest_framework import serializers

from v1.tags.models.tag import Tag


class AdminTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]
        lookup_field = "slug"
        extra_kwargs = {"slug": {"read_only": True}}
