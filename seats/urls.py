from django.contrib import admin
from .views import  seatsList
from django.urls import path, include, re_path
urlpatterns = [
    path('<int:pk>/',seatsList)
]
