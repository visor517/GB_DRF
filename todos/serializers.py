from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from todos.models import Project, ToDo


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class GetProjectSerializer(ProjectSerializer):
    authors = StringRelatedField(many=True)


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'


class GetToDoSerializer(ToDoSerializer):
    author = StringRelatedField()
    project = StringRelatedField()
