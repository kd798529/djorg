from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    message = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    sender = models.ForeignKey(User, related_name="recipient", on_delete=models.CASCADE)
    recipient = models.ManyToManyField(User)

