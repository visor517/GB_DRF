from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from todos.models import Project, ToDo
from users.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    authors = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    author = StringRelatedField()
    project = StringRelatedField()

    class Meta:
        model = ToDo
        fields = '__all__'
