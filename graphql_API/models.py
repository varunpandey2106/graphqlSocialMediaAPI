from django.db import models


# Create your models here.

class User(models.Model):
    name= models.CharField(max_length=250)
    followers=models.ManyToManyField('graphql_API.User')

#referencing an existing django model

class Post(models.Model):
    content=models.CharField(max_length=1000)
    created_by= models.ForeignKey(User,related_name='User' ,on_delete=models.DO_NOTHING)