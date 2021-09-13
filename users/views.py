from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from users.models import User
from users.serializers import UserModelSerializer


class UsersViewSet(ViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    queryset = User.objects.all()

    def list(self, request):
        users = User.objects.all()
        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserModelSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserModelSerializer(user)
        return Response(serializer.data)
