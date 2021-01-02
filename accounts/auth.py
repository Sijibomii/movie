import jwt
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.hashers import check_password
from datetime import datetime
from rest_framework.authentication import BaseAuthentication
User = get_user_model()


class authurize():
  #decode token and return user details
  def decode_token(token):
    try:
      decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithm="HS256")
    except Exception:
      return None
    return decoded_data

  #decode token and check the validity of the token, if token is expired user re-logs in
  
  #decode token and return true if user is admin
  def check_is_admin(token):
    data= authurize.decode_token(token)
    return data['is_staff']
    

  #get token from headers and return it
  def get_user_token(headers):
    authorization = headers.get("Authorization", None)
    if not authorization:
      return None
    token = authorization.split()
    return token[1]
