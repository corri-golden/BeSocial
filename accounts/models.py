from django.db import models
from django.contrib import auth

# Create your models here.
# inheriting from auth
class User(auth.models.User, auth.models.PermissionsMixin):


    #string representation of the object
    def __str__(self):
    # username is built into the USER class
        return "@{}".format(self.username)