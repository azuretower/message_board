from django.db import models
from django.contrib.auth.models import USER


class Message(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User)
    date_posted = models.DateTimeField(auto_now_add=True)
