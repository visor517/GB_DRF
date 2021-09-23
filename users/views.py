from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from users.models import User
from users.serializers import UserModelSerializer, UserModelSerializerV2


class UsersViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserModelSerializerV2
        return UserModelSerializer
