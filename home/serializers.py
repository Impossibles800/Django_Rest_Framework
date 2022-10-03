from dataclasses import fields
from rest_framework import serializers
from .models import Student

""" We use the model serializers vastly
->  serializers name should be lightly matched with the model name
  
 """


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(default=18)
    father_name = serializers.CharField(max_length=100)

    class Meta:
        # meta should have the model name
        model = Student
        """fields should have the model fields, include those items which we want to show in the api"""
        fields = "__all__"
