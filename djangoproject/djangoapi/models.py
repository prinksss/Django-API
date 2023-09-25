from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.conf import settings
class CustomUsers(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="userpost",blank=True,null=True)

    def __str__(self):
        return self.title