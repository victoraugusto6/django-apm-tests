from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, db_index=True)
