from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
# we cannot use the html here as we are using rest framework which returns json data

# @api_view(['GET'])
# def home(request):
#     students = Student.objects.all()

#     serializer = StudentSerializer(students, many=True)# Using the serializer

#   return Response({
#     'status': 200,
#     'data': serializer.data
#   })


@api_view(['GET'])
def home(request):
    students = Student.objects.all()

    serializer = StudentSerializer(students, many=True)  # Using the serializer

    return Response({
        'status': 200,
        'data': serializer.data
    })


@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': 200,
            'data': serializer.data,
            'message': 'Everything is fine'
        })
    else:
        print(serializer.errors)
        return Response({
            'status': 404,
            'error': serializer.errors,
            'message': 'you send the wrong data'
        })