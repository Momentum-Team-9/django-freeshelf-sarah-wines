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
    author = models.ManyToManyField('Author', related_name='authors')
    description = models.TextField(max_length=2000)
    url = models.URLField(max_length=250)
    created_at = DateTimeField(auto_now_add = True)
  
    
    def __str__(self):
        return f"{self.title}, {self.author}, {self.description}"

class Author(models.Model):
    name = models.CharField(max_length=225)
    books = models.ManyToManyField(Book, related_name='book', blank=True)

    class Meta:
        ordering = ['name']
        
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return f"{self.name}"