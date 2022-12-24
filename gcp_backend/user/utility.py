from multiprocessing import AuthenticationError
from .models import User
from gcp_backend.settings import COOKIE_ENCRYPTION_SECRET
import jwt
from rest_framework.response import Response
from rest_framework import status

# Autherize decorator
def autherize(func):
    def wrapper(*args, **kwargs):
        try:
            cookie = args[1].COOKIES['jwt']
        except :
            return Response({"message": "Cookie not found"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

        try:
            payload = jwt.decode(cookie, COOKIE_ENCRYPTION_SECRET, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response( { 'message' : 'Cookie expired' }, status=status.HTTP_408_REQUEST_TIMEOUT)
            
        user = User.objects.get(userid=payload['id'])
        if not user:
            return Response(
                {"Message": "User with id does not exists"}, 
                status=status.HTTP_204_NO_CONTENT
            )
        kwargs['user'] = user
        kwargs['role'] = user.role
        return func(*args, **kwargs)

    return wrapper