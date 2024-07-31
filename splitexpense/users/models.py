from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    id=models.CharField(max_length=200,primary_key=True,unique=True,auto_created=True,)
    name=models.CharField(max_length=200)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_profile")
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    