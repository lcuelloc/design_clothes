from rest_framework import serializers

from v1.accounts.models.user import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "ci", "password", "first_name", "last_name", "phone", "customer"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
