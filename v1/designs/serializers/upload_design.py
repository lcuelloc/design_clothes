from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()


class DesignLoadSerializer(serializers.Serializer):
    category = serializers.CharField()
    name = serializers.CharField()
    image = serializers.CharField()
