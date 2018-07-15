from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from v1.accounts.serializers.registration import RegistrationSerializer
from v1.utils.QVO import clients


# v1/registration
class RegistrationView(APIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        Register a new user
        """
        # import ipdb; ipdb.set_trace()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            email = request.data['email']
            username = request.data['username']
            client = clients.new_client(email, username)
            serializer.save(customer=client['id'])
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
