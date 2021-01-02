from django.contrib import admin
from .views import movieList ,movieDetail, movieSearch, movieAdminDetail, movieAdminCreate,movieTop
from django.urls import path, include, re_path
urlpatterns = [
    path('',movieList ),
    path('<int:pk>/',movieDetail),
    path('search/<str:name>/', movieSearch),
    path('admin/<int:pk>/', movieAdminDetail),
    path('admin/', movieAdminCreate),#not working yet!
    path('top/', movieTop)
]
