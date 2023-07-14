from django.db import models


# Create your models here.

class User(models.Model):
    name= models.CharField(max_length=250)
    followers=models.ManyToManyField('graphql_API.User')

#referencing an existing django model