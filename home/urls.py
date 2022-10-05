from django.contrib import admin
from django.urls import path, include
from home import views
from home.views import StudentAPI

urlpatterns = [
    # path('', views.home, name='home'),
    # path('post/', views.post_student, name='post'),
    # path('update-student/<id>/', views.update_student, name='update_student'),
    # path('delete-student/<id>/', views.delete_student, name='delete_student'),
    path('get-book/', views.get_book, name='get_book'),
    path('student/', StudentAPI.as_view(), name='student'),
]
