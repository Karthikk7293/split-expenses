# expenses/models.py

from django.db import models
from django.contrib.auth.models import User
from groups.models import Groups  # Assuming groups app is where MainTable is defined
import uuid

class Expense(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    expense_members = models.JSONField()
    paid_by = models.JSONField()
    group = models.ForeignKey(Groups, null=True, blank=True, on_delete=models.SET_NULL, related_name='expenses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
