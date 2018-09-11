from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()


class ProductLoadSerializer(serializers.Serializer):
    category = serializers.CharField()
    product_name = serializers.CharField()
    product_price = serializers.IntegerField()
    size = serializers.CharField()
    print_type = serializers.CharField()
    color = serializers.CharField()
    front = serializers.CharField()
    back = serializers.CharField(allow_null=True)
    left = serializers.CharField(allow_null=True)
    right = serializers.CharField(allow_null=True)
