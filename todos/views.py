from rest_framework.viewsets import ModelViewSet

from todos.models import Project, ToDo
from todos.serializers import ProjectModelSerializer, ToDoModelSerializer


class ProjectsViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDosViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
