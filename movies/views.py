from django.shortcuts import render
from .serializers import movieSerializer
from accounts.token import token
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.auth import authurize
from rest_framework.decorators import api_view,permission_classes
from rest_framework import authentication, exceptions
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import Movie
# @desc    GET all movies
# @route   GET movie/
# @access  Public
@api_view(['GET'])
@permission_classes(())
def movieList(request):
  try:
    movies= Movie.objects.all()
  except Movie.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method=='GET':
    serializer= movieSerializer(movies, many=True)
    return Response(serializer.data)  



# @desc    GET movie by id
# @route   GET movie/:id
# @access  Public
@api_view(['GET'])
@permission_classes(())
def movieDetail(request,pk):
  try:
    movies= Movie.objects.get(pk=pk)
  except Movie.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method=='GET':
    serializer= movieSerializer(movies)
    return Response (serializer.data)

# @desc    GET movies by search term
# @route   GET movie/search/<str: name>/
# @access  Public
@api_view(['GET'])
@permission_classes(())
def movieSearch(request, name):
  try:
    movies= Movie.objects.all().filter(title__icontains=name)
    movies |= Movie.objects.all().filter(description__icontains=name)
    movies |= Movie.objects.all().filter(genre__icontains=name)
    movies |= Movie.objects.all().filter(cast__icontains=name)
  except Movie.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method=='GET':
    serializer= movieSerializer(movies, many=True)
    return Response (serializer.data)


# @desc    DELETE movie by id
# @route   DELETE movie/admin/:id
# @access  Private/admin
# use the check_admin in auth.py to confirm the user is an admin

# @desc    GET movie by id
# @route   GET movie/admin/:id
# @access  Private/admin
# use the check_admin in auth.py to confirm the user is an admin

# @desc    UPDATE movie
# @route   PUT movie/admin/:id
# @access  Private/admin
# use the check_admin in auth.py to confirm the user is an admin
@api_view(['GET','PUT','DELETE'])
@permission_classes(())
def movieAdminDetail(request,pk):
  token=authurize.get_user_token(request.headers)
  data=authurize.check_is_admin(token)
  if not data:
    return Response({"error": "User Not Authorized"}, status="400")
  try:
    movie= Movie.objects.get(pk=pk)
  except Movie.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method=='GET':
    serializer= movieSerializer(movie)
    return Response (serializer.data)

  elif request.method=='PUT':
    serializer=movieSerializer(Movie, data= request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method=='DELETE':
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
# @desc    CREATE movie
# @route   POST movie/admin/
# @access  Private/admin
# use the check_admin in auth.py to confirm the user is an admin
@api_view(['GET','POST'])
@permission_classes(())
def movieAdminCreate(request):
  token=authurize.get_user_token(request.headers)
  data=authurize.check_is_admin(token)
  if not data:
    return Response({"error": "User Not Authorized"}, status="400")
  if request.method =='POST':
    serializer=movieSerializer(Movie, data=request.data)
    if serializer.is_valid():
      movie = Movie(title=serializer.validated_data['title'], duraration=serializer.validated_data['duraration'],trailer=serializer.validated_data['trailer'],images=serializer.validated_data['images'], genre=serializer.validated_data['genre'], director=serializer.validated_data['director'], cast=serializer.validated_data['cast'], description=serializer.validated_data['description'])
      movie = Movie.objects.create(title=serializer.validated_data['title'], duraration=serializer.validated_data['duraration'],trailer=serializer.validated_data['trailer'],images=serializer.validated_data['images'], genre=serializer.validated_data['genre'], director=serializer.validated_data['director'], cast=serializer.validated_data['cast'], description=serializer.validated_data['description'])
      movie.save()
      #serializer.save()
      #serializer refused to save, type error (needs self arguement)
      return Response({"success":"movie created"},status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @desc    GET top movies by rating
# @route   GET movie/top
# @access  Public

@api_view(['GET'])
@permission_classes(())
def movieTop(request):
  try:
    movies= Movie.objects.order_by('-release_date')
  except Movie.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method=='GET':
    serializer= movieSerializer(movies, many=True)
    return Response (serializer.data)

