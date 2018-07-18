from rest_framework import generics
from rest_framework import permissions

from v1.accounts.models.user import User
from v1.accounts.serializers.registration import RegistrationSerializer


class RegistrationUserList(generics.ListAPIView):
    """
    Get list of all registered users
    """

    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = RegistrationSerializer
