from rest_framework import serializers

from v1.images.models.image import Image


class AdminImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ["pk", "product_color", "path"]
