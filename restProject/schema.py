from graphene import Schema, ObjectType, String, List
from graphene_django import DjangoObjectType

from users.models import User


class UserDjangoType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(ObjectType):
    all_users = List(UserDjangoType)

    def resolve_all_users(self, info):
        return User.objects.all()


schema = Schema(query=Query)
