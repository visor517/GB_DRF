from graphene import Schema, ObjectType, String, List, Int, Mutation, ID, Field
from graphene_django import DjangoObjectType

from todos.models import Project, ToDo
from users.models import User


class UserDjangoType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectDjangoType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoDjangoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class Query(ObjectType):
    all_users = List(UserDjangoType)
    all_projects = List(ProjectDjangoType)
    all_todos = List(ToDoDjangoType)
    todos_by_project_id = List(ToDoDjangoType, id=Int())

    def resolve_all_users(self, info):
        return User.objects.all()

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_all_todos(self, info):
        return ToDo.objects.all()

    def resolve_todos_by_project_id(self, info, id):
        return ToDo.objects.filter(project_id=id)


class ToDoMutation(Mutation):
    class Arguments:
        pk = ID()
        description = String(required=True)

    todo = Field(ToDoDjangoType)

    @classmethod
    def mutate(cls, root, info, pk, description):
        todo = ToDo.objects.get(pk=pk)
        todo.description = description
        todo.save()
        return ToDoMutation(todo=todo)


class Mutation(ObjectType):
    update_todo_description = ToDoMutation.Field()


schema = Schema(query=Query, mutation=Mutation)
