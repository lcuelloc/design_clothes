from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.tags.models.tag_design import TagDesign


class AdminTagDesignSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = TagDesign
        fields = ["tag", "design"]
