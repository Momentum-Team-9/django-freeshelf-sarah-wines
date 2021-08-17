from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    url = models.URLField(max_length=250)
    created_at = DateTimeField(auto_now_add = True)
  
    
    def __str__(self):
        return f"{self.title}, {self.author}, {self.description}"