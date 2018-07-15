from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from v1.accounts.models.user import User


class AdminUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'is_active', 'customer']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data.get('password'))
        return super().validate(validated_data)
