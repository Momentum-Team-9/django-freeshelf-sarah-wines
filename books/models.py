from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Author(models.Model):
    name = models.CharField(max_length=225)
    

    class Meta:
        ordering = ['name']
        
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250)
    authors = models.ManyToManyField(Author, related_name='books', blank=True)
    description = models.TextField(max_length=2000)
    categories = models.ManyToManyField('Category', related_name='books', blank=True)
    url = models.URLField(max_length=250)
    created_at = DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return f"{self.title}, {self.authors.all()[0].name}, {self.description}"



class Category(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return f"{self.name}"