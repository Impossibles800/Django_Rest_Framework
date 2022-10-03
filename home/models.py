from email.policy import default
from django.db import models

# Create your models here.


# we use the serializers to convert the data into json format

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=100)
