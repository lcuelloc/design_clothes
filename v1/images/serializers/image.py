from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.images.models.image import Image


class ImageSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["pk", "product_color", "path"]
