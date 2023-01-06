from multiprocessing import AuthenticationError
from .models import User
from gcp_backend.settings import COOKIE_ENCRYPTION_SECRET
import jwt
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
import datetime
import sys
from gcp_backend.settings import EMAIL_HOST_USER
# Autherize decorator class


class Autherize:
    def __init__(self, usertype="2"):
        self.type = usertype

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if args[1].COOKIES.get('jwt') is None:
                # handling O-auth login
                if args[1].user.is_authenticated:
                    print(f'ERROR Hello', file=sys.stderr)
                    print(f'||{args[1].user}||', file=sys.stderr)
                    
                    uid = User.objects.get(email=args[1].user.email).userid
                    payload = {
                        "id": uid,
                        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                        "iat": datetime.datetime.utcnow(),
                    }
                    token = jwt.encode(
                        payload, COOKIE_ENCRYPTION_SECRET, algorithm='HS256')
                    response = Response(
                        {"message": "Cookie set"}, status=status.HTTP_200_OK)
                    response.set_cookie('jwt', token)
                    return response
                return Response({"message": "Cookie not found"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            else:
                cookie = args[1].COOKIES['jwt']

            print(cookie)
            try:
                payload = jwt.decode(
                    cookie, COOKIE_ENCRYPTION_SECRET, algorithms=['HS256'])
            except:
                if args[1].user.is_authenticated:
                    print(f'ERROR Hello', file=sys.stderr)
                    print(f'||{args[1].user}||', file=sys.stderr)
                    
                    uid = User.objects.get(email=args[1].user.email).userid
                    payload = {
                        "id": uid,
                        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                        "iat": datetime.datetime.utcnow(),
                    }
                    token = jwt.encode(
                        payload, COOKIE_ENCRYPTION_SECRET, algorithm='HS256')
                    response = Response(
                        {"message": "Cookie set"}, status=status.HTTP_200_OK)
                    response.set_cookie('jwt', token)
                    return response
                return Response({"message": "Cookie not found"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            
            user = User.objects.get(userid=payload['id'])
            if not user:
                return Response(
                    {"Message": "User with id does not exists"},
                    status=status.HTTP_204_NO_CONTENT
                )
            if self.type == "0" and user.role != "0":
                return Response(
                    {"Message": "Premission denied"},
                    status=status.HTTP_403_FORBIDDEN
                )
            if self.type == "1" and user.role != "1":
                return Response(
                    {"Message": "User with id doesn't exist"},
                    status=status.HTTP_403_FORBIDDEN
                )
            kwargs['user'] = user
            return func(*args, **kwargs)
        return wrapper


class EmailSending:
    def __init__(self, email):
        self.address = email
        self.subject = None
        self.body = None

    def varification_mail(self):
        user = User.objects.get(email=self.address)
        payload = {
            'userid': user.userid,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(
            payload, COOKIE_ENCRYPTION_SECRET, algorithm='HS256')
        link = "http://localhost:8000/user/verify/"+token

        self.subject = "No replay"
        self.body = f'''
        Hi {user.name},\n
            Please click on the link below to verify your email address:
             \n{link}
            \n\nThanks,
            \nTeam Club Management System
        '''
        res = send_mail(self.subject, self.body, EMAIL_HOST_USER, self.address)
        return res

    def reset_password(self):
        user = User.objects.get(email=self.address)
        payload = {
            'userid': user.userid,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(
            payload, COOKIE_ENCRYPTION_SECRET, algorithm='HS256')
        link = "http://localhost:8000/user/reset_password/"+token

        self.subject = "No replay"
        self.body = f'''
        Hi {user.name},\n
            Please click on the link below to reset your password:
             \n{link}
            \n\nThanks,
            \nTeam Club Management System
        '''
        res = send_mail(self.subject, self.body, EMAIL_HOST_USER, self.address)
        return res

    def confirmation(self, name):
        self.subject = "!Important"
        self.body = f"Hi {name}, Your password has been changed, if not initiated by you please take action.\n\n Thank you"
        res = send_mail(self.subject, self.body, EMAIL_HOST_USER, self.address)
        return res
