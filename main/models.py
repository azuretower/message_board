from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
#     date_of_birth = models.DateField(blank=True, null=True)
#     height = models.FloatField(blank=True, null=True)


class Message(models.Model):
    title = models.CharField(max_length=255, default="i can't think of a title")
    text = models.TextField()
    author = models.ForeignKey(User)
    date_posted = models.DateTimeField(auto_now_add=True)
    favorite = models.ManyToManyField(User, related_name='favorites', blank=True)

    def __unicode__(self):
        return self.title
