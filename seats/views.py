from django.shortcuts import render
#from .serializers import seatsSerializer
from accounts.token import token
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.auth import authurize
from rest_framework.decorators import api_view,permission_classes
from rest_framework import authentication, exceptions
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import Seat
# Create your views here.
 

# @desc    GET all states of seats by aud
# @route   GET seats/<int:aud>/
# @access  Public
@api_view(['GET'])
@permission_classes(())
def seatsList(request,pk):
  try:
    seats= Seat.objects.all().filter(aud=pk).order_by('id')
  except Seat.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method=='GET':
    arr=[]
    for i in range(seats.count()):
      if seats[i].status=='EMPTY':
        arr.append('0')
      elif seats[i].status=='ASSIGNED':
        arr.append('1')
      else:
        arr.append('2')
    return Response({"seats":arr})



# @desc    POST req to change status of seats
# @route   POST seats/change/<int:aud/
# @access  Public
