from datetime import timedelta

from django.conf import settings
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *


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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student_obj = Student.objects.all()
        serializer = StudentSerializer(student_obj, many=True)
        return Response({
            'status': 200,
            'data': serializer.data,
            'message': 'data successfully fetched'
        })

    def patch(self, request):
        try:
            #                                    id from front end
            student_obj = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(
                student_obj, data=request.data, partial=True)

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
                    'message': 'data successfully updated'
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


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            refresh = RefreshToken.for_user(user)


            return Response({
                'status': 200,
                'data': serializer.data,
                'message': 'user successfully created',
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        else:
            return Response({
                'status': 404,
                'error': serializer.errors,
                'message': 'Something went wrong'
            })

    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
        'ROTATE_REFRESH_TOKENS': False,
        'BLACKLIST_AFTER_ROTATION': True,
        'UPDATE_LAST_LOGIN': False,

        'ALGORITHM': 'HS256',
        'SIGNING_KEY': settings.SECRET_KEY,
        'VERIFYING_KEY': None,
        'AUDIENCE': None,
        'ISSUER': None,

        'AUTH_HEADER_TYPES': ('Bearer',),
        'USER_ID_FIELD': 'id',
        'USER_ID_CLAIM': 'user_id',
        'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

        'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
        'TOKEN_TYPE_CLAIM': 'token_type',

        'JTI_CLAIM': 'jti',

        'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
        'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
        'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    }
