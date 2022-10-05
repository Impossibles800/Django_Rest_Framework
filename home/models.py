from email.policy import default
from django.db import models

# Create your models here.


# we use the serializers to convert the data into json format

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=100)


class Category(models.Model):
    category_name = models.CharField(max_length=100)

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)
