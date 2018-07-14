from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from v1.accounts.serializers.registration import RegistrationSerializer


# v1/registration
class RegistrationView(APIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        Register a new user
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
