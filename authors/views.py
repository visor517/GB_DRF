from rest_framework.viewsets import ModelViewSet

from authors.models import Author
from authors.serializers import AuthorModelSerializer


class AuthorsViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

