import graphene
from graphene_django import DjangoObjectType
from graphql_API import models
from django.urls import path

class User(DjangoObjectType):
    class Meta:
        model=models.User

class Post(User):
    class Meta:
        model=models.User


class UserInput(graphene.InputObjectType):
    name=graphene.String()


class UserType(DjangoObjectType):
    postSet = graphene.List("graphql_SM_API.schema.PostType")

    class Meta:
        model = models.User
        fields = ("id", "name", "postSet", "followers")



class CreateUser(graphene.Mutation):
    class Arguments:
        input=UserInput(required= True)
    
    ok=graphene.Boolean()
    user=graphene.Field(User)

    @staticmethod
    def mutate(root, info,input):
        instance=models.User(name=input.name)

        try:
            instance.save()
        except Exception:
            return CreateUser(ok=False, User=None)
        
        instance.followers.set([])
        return CreateUser(ok=True, user=instance)
    
class PostType(DjangoObjectType):
    class Meta:
        model = models.Post

class Query(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.Int(required=True))

    def resolve_user(self, info, id):
        try:
            return models.User.objects.get(id=id)
        except models.User.DoesNotExist:
            return None
        
class Mutation(graphene.ObjectType):
    create_user=CreateUser.Field()

#get method of the User model manager to fetch the user based on the provided id. If the user does not exist, returning None.

schema = graphene.Schema(query=Query)