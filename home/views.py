from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

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
def get_book(request):
    book_objs = Book.objects.all()
    serializer = BookSerializer(book_objs, many=True)
    return Response({
        'status': 200,
        'data': serializer.data
    })


# @api_view(['GET'])
# def home(request):
#     students = Student.objects.all()

#     serializer = StudentSerializer(students, many=True)  # Using the serializer

#     return Response({
#         'status': 200,
#         'data': serializer.data
#     })


# @api_view(['POST'])
# def post_student(request):
#     data = request.data

#     serializer = StudentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({
#             'status': 200,
#             'data': serializer.data,
#             'message': 'Everything is fine'
#         })
#     else:
#         print(serializer.errors)
#         return Response({
#             'status': 404,
#             'error': serializer.errors,
#             'message': 'you send the wrong data'
#         })


# @api_view(['PATCH'])
# def update_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         serializer = StudentSerializer(student_obj, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'status': 200,
#                 'data': serializer.data,
#                 'message': 'Everything is fine'
#             })
#         else:
#             print(serializer.errors)
#             return Response({
#                 'status': 404,
#                 'error': serializer.errors,
#                 'message': 'you send the wrong data'
#             })
#     except Exception as e:
#         return Response({
#             'status': 404,
#             'error': e,
#             'message': 'invalid id'
#         })


# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({
#             'status': 200,
#             'message': 'Deleted successfully',
#         })
#     except Exception as e:
#         return Response({
#             'status': 404,
#             'error': e,
#             'message': 'invalid id'
#         })


class StudentAPI(APIView):

    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        return Response({
            'status': 200,
            'data': serializer.data
        })

    def post(self, request):
        student_obj = StudentSerializer(data=request.data)
        if student_obj.is_valid():
            student_obj.save()
            return Response({
                'status': 200,
                'data': student_obj.data,
                'message': 'Everything is fine'
            })
        else:
            # print(student_obj.errors)
            return Response({
                'status': 404,
                'error': student_obj.errors,
                'message': 'you send the wrong data'
            })

    def patch(self, request):
        try:
            #                                    id from front end
            student_obj = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student_obj, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'data': serializer.data,
                    'message': 'Data successfully updated'
                })
            else:
                print(serializer.errors)
                return Response({
                    'status': 404,
                    'error': serializer.errors,
                    'message': 'you send the wrong data'
                })
        except Exception as e:
            return Response({
                'status': 404,
                'error': e,
                'message': 'invalid id'
            })

    def delete(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            student_obj.delete()
            return Response({
                'status': 200,
                'message': 'Deleted successfully',
            })
        except Exception as e:
            return Response({
                'status': 404,
                'error': e,
                'message': 'invalid id'
            })

    def put(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student_obj, data=request.data)

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
        except Exception as e:
            return Response({
                'status': 404,
                'error': e,
                'message': 'invalid id'
            })
