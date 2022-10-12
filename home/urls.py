from django.urls import path
from home import views
from .views import *
from django.urls import path

from home import views
from .views import *

urlpatterns = [
    # path('', views.home, name='home'),
    # path('post/', views.post_student, name='post'),
    # path('update-student/<id>/', views.update_student, name='update_student'),
    # path('delete-student/<id>/', views.delete_student, name='delete_student'),
    path('get-book/', views.get_book, name='get_book'),
    # path('student/', StudentAPI.as_view(), name='student'),
    # path('register/', RegisterUser.as_view(), name='register'),
    path('generic-student/', StudentGeneric.as_view(), name='generic-student'),
    path('generic-student/<id>/', StudentGeneric1.as_view(), name='generic-student'),
    path('pdf/', GeneratePdf.as_view(), name='pdf'),
]
