from django.shortcuts import render
from .serializers import registrationSerializer,LoginSerializer,userSerializer  # write serializer
from .token import token
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,get_user_model
from rest_framework.decorators import api_view,permission_classes
from rest_framework import authentication, exceptions
from rest_framework import status
from .models import UserAccount
from .auth import authurize
User = get_user_model()
# Create your views here.


# @desc    Update user profile
  # @route   PUT to accounts/user/<id>
  # @access  Private
  #use the decode token in auth.py to get userid
@api_view(['PUT'])
@permission_classes(())
def userDetail(request,pk):
  try:
    user= User.objects.get(pk=pk)
  except User.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method=='PUT':
    token=authurize.get_user_token(request.headers)
    data=authurize.decode_token(token)
    if not data:
      return Response({"error": "User Not Authenticated"}, status="400")
    serializer=userSerializer(user, data= request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#desc: register a new user
# POST req to accounts/register
#access Public
class RegisterView(APIView):
  serializer_class = registrationSerializer
 
  def post(self, request):
    data = {}
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      account = serializer.save()
      data['response'] = "successfully registered new user"
      data['email'] = account.email
      data['name']=account.name
      data['is_staff'] = account.is_staff
      data['id']=account.id
      tokendata = token.get_access_token(data)
      data['token'] = tokendata
    else:
      data = serializer.errors
    return Response(data)


#desc: Login a user
# POST req to accounts/login
#access Public
class LoginView(APIView):
  serializer_class = LoginSerializer

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    #tom=authurize.get_user_token(request.headers)
    ##t=authurize.decode_token(tom)
    #print(t)
    serializer.is_valid(raise_exception=True)
    data={}
    user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
    if not user:
      return Response({"error": "Invalid email or password"}, status="400")
    data['email'] = user.email
    data['name']=user.name
    data['is_staff'] = user.is_staff
    data['id']=user.id
    tokendata = token.get_access_token(data)
    data['token'] = tokendata   
    return Response(data)


class UserProfileView(APIView):
  #desc: Get a users profile
  # GET req to accounts/user
  #access Private
  #use the decode token in auth.py to get userid
  def get(self, request):
    token=authurize.get_user_token(request.headers)
    data=authurize.decode_token(token)
    if not data:
      return Response({"error": "User Not Authenticated"}, status="400")
    user_id= data['id']
    user= User.objects.get(pk=user_id)
    serializer= userSerializer(user)
    return Response (serializer.data)

 

#----------------------------

# @desc    Get all users
# @route   GET accounts/admin/users
# @access  Private/Admin
# use the check_admin in auth.py to confirm the user is an admin
@api_view(['GET'])
@permission_classes(())
def usersList(request):
  try:
    user= User.objects.all()
  except User.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method=='GET':
    token=authurize.get_user_token(request.headers)
    data=authurize.check_is_admin(token)
    if not data:
      return Response({"error": "User Not Authorized"}, status="400")
    serializer= userSerializer(user, many=True)
    return Response(serializer.data)  
    

# @desc    Delete user
# @route   DELETE accounts/admin/users/:id
# @access  Private/Admin
# use the check_admin in auth.py to confirm the user is an admin

# @desc    Get user by ID
# @route   GET accounts/admin/users/:id
# @access  Private/Admin
# use the check_admin in auth.py to confirm the user is an admin

# @desc    Update user
# @route   PUT accounts/admin/users/:id
# @access  Private/Admin
# use the check_admin in auth.py to confirm the user is an admin
@api_view(['GET','PUT','DELETE'])
@permission_classes(())
def userAdminDetail(request,pk):
  token=authurize.get_user_token(request.headers)
  data=authurize.check_is_admin(token)
  if not data:
    return Response({"error": "User Not Authorized"}, status="400")
  try:
    user= User.objects.get(pk=pk)
  except User.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method=='GET':
    serializer= userSerializer(user)
    return Response (serializer.data)

  elif request.method=='PUT':
    serializer=userSerializer(User, data= request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method=='DELETE':
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# @desc    Create Admin user
# @route   POST accounts/admin/new
# @access  Private/Admin
# use the check_admin in auth.py to confirm the user is an admin

 