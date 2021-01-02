from django.shortcuts import render
from .serializers import screeningSerializer
from accounts.token import token
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.auth import authurize
from rest_framework.decorators import api_view,permission_classes
from rest_framework import authentication, exceptions
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import Screening
# Create your views here.
 

# @desc    GET all screenings by date
# @route   GET screening/
# @access  Public
@api_view(['GET'])
@permission_classes(())
def screeningList(request):
  try:
    screenings= Screening.objects.order_by('-screening_date')
  except Screening.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method=='GET':
    serializer= screeningSerializer(screenings, many=True)
    return Response(serializer.data)  


# @desc    GET all screenings by movie
# @route   GET screening/<int: movie>/
# @access  Public
@api_view(['GET'])
@permission_classes(())
def screeningMovieDetail(request,pk):
  try:
    screenings= Screening.objects.all().filter(movie=pk)
  except Screening.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method=='GET':
    serializer= screeningSerializer(screenings, many=True)
    return Response(serializer.data)  


