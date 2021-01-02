from django.contrib import admin
from .views import  reviews
from django.urls import path, include, re_path
urlpatterns = [
    path('<int:pk>/', reviews)
]
