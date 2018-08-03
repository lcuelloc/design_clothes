from rest_framework import status
from rest_framework.response import Response


class MultiSerializerViewSetMixin(object):
    def get_serializer_class(self):
        """
        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:

        class MyViewSet(MultiSerializerViewSetMixin, ViewSet):
            serializer_class = MyDefaultSerializer
            serializer_action_classes = {
               'list': MyListSerializer,
               'my_action': MyActionSerializer,
            }

            @action
            def my_action:
                ...

        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.

        Thanks gonz: http://stackoverflow.com/a/22922156/11440

        """
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()


class ActionViewMixin(object):
    """ Mixin para generics.GenericAPIView.

        Si los actions existentes (list, create, update, delete, etc.) no resuelven
        la necesidad especifica a la cual se quiere atender, entonces se puede
        utilizar este mixin para darle un comportamiento especifico al view. Se usa
        como un APIView, pero con las capacidades y abstracciones de un
        GenericAPIView.

        Se utiliza creando el método `def action(self, serializer):` dentro del
        GenericAPIView. El método `action` retorna un `Response`.
    """

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return self.action(serializer, *args, **kwargs)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
