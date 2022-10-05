from dataclasses import fields
from unicodedata import category
from rest_framework import serializers
from .models import *

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

    def validate(self, data):
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError(
                        'Name should not contain numbers')

        if data['age'] < 18:
            raise serializers.ValidationError({
                'error':   'You are not eligible to apply'
            })
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']
        # fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = "__all__"
        # depth = 1
