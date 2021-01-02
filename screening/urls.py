from django.contrib import admin
from .views import  screeningList,screeningMovieDetail
from django.urls import path, include, re_path
urlpatterns = [
    path('', screeningList),
    path('<int:pk>/',screeningMovieDetail)
]
