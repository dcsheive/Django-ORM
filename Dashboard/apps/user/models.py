from django.db import models
from django.apps import apps

# Create your models here.
from ..register.models import User

class Message(models.Model):
      text = models.TextField()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      page = models.ForeignKey(User, related_name="pages")
      poster = models.ForeignKey(User, related_name="messages")

class Comment(models.Model):
      text = models.TextField()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      message = models.ForeignKey(Message, related_name='comments')
      poster = models.ForeignKey(User, related_name="comments")
      page = models.ForeignKey(User,on_delete=models.CASCADE, related_name="pages_comments")
