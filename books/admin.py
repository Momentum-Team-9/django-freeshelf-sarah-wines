from django.contrib import admin
from .models import Book, Author, User, Category
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(User)
admin.site.register(Category)
# Register your models here.
