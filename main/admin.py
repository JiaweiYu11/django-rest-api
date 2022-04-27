from django.contrib import admin

from django.db import models
# Register your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)

admin.site.register(Book)