from graphene import Schema, ObjectType, String


class Query(ObjectType):
    goodbye = String()
    hello = String(name=String())

    def resolve_goodbye(root, info):
        return f'goodbye'

    def resolve_hello(root, info, name="Bob"):
        return f'Hello {name}!'


schema = Schema(query=Query)
