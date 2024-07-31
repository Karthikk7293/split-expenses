from django.db import models
from users.models import Users

# Create your models here.
class Groups(models.Model):
    # owner=models.ForeignKey(Users,on_delete=models.SET_NULL,related_name="groups")
    name=models.CharField(max_length=200)
    total_members=models.IntegerField(default=0)
    group_members=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    uid=models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
