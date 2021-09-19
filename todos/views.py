from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from todos.filters import ProjectFilter, ToDoFilter
from todos.models import Project, ToDo
from todos.serializers import ProjectSerializer, ToDoSerializer, GetProjectSerializer, GetToDoSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectsViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return GetProjectSerializer
        return ProjectSerializer

    filter_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPagination


class ToDosViewSet(ModelViewSet):
    queryset = ToDo.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return GetToDoSerializer
        return ToDoSerializer

    filter_class = ToDoFilter
    pagination_class = ToDoLimitOffsetPagination

    def destroy(self, request, *args, **kwargs):
        ToDo.objects.filter(pk=kwargs['pk']).update(is_active=False)
        return Response(status=204)
