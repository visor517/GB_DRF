from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from todos.filters import ProjectFilter, ToDoFilter
from todos.models import Project, ToDo
from todos.serializers import ProjectModelSerializer, ToDoModelSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectsViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filter_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPagination


class ToDosViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    filter_class = ToDoFilter
    pagination_class = ToDoLimitOffsetPagination

    def destroy(self, request, *args, **kwargs):
        ToDo.objects.filter(pk=kwargs['pk']).update(is_active=False)
        return Response(status=204)
