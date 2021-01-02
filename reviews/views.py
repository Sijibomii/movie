from django.shortcuts import render
from .models import Review
from accounts.token import token
from accounts.auth import authurize
from rest_framework.response import Response
from .serializers import reviewSerializer
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
# Create your views here.

# @desc    GET Reviews by movie
# @route   GET reviews/:id
# @access  Public


# @desc    POST a review to a new movie
# @route   POST reviews/:id
# @access  Private
@api_view(['GET', 'POST'])
@permission_classes(())
def reviews(request, pk):
  try:
    reviews= Review.objects.all().filter(movie=pk)
  except Review.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method=='GET':
    serializer= reviewSerializer(reviews, many=True)
    return Response(serializer.data)
  elif request.method=='POST':
    token=authurize.get_user_token(request.headers)
    data=authurize.decode_token(token)
    serializer=reviewSerializer(Review, data=request.data)
    if serializer.is_valid():
      print(serializer.validated_data)
      review = Review(movie=serializer.validated_data['movie'], user=serializer.validated_data['user'], comment=serializer.validated_data['comment'],star_rating=serializer.validated_data['star_rating'])
      review = Review.objects.create(movie=serializer.validated_data['movie'], user=serializer.validated_data['user'], comment=serializer.validated_data['comment'],star_rating=serializer.validated_data['star_rating'])
      review.save()
      #serializer.save()
      return Response({"success": "review created"}, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

