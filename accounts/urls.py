from django.contrib import admin
from .views import  RegisterView,LoginView,UserProfileView, userDetail, usersList, userAdminDetail
from django.urls import path, include, re_path
urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('user/', UserProfileView.as_view()),
    path('user/<int:pk>/', userDetail),
    path('admin/users/', usersList),
    path('admin/users/<int:pk>/', userAdminDetail)
]
