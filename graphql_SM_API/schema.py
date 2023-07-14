import graphene
from graphene_django import DjangoObjectType
from graphql_API import models

class User(DjangoObjectType):
    class Meta:
        model=models.User

class Query(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.Int(required=True))

    def resolve_user(self, info, id):
        try:
            return models.User.objects.get(id=id)
        except models.User.DoesNotExist:
            return None
#get method of the User model manager to fetch the user based on the provided id. If the user does not exist, returning None.

schema = graphene.Schema(query=Query)