from rest_framework import serializers

from v1.tags.models.tag_design import TagDesign


class AdminTagDesignSerializer(serializers.ModelSerializer):

    class Meta:
        model = TagDesign
        fields = ["tag", "design"]
