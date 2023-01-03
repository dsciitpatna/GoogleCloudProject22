from multiprocessing import AuthenticationError
from rest_framework import status
from .serializer import UserSerializer
from .models import User, Organization
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import re
from gcp_backend.utility import hash_password, check_password
import jwt
import datetime
from gcp_backend.settings import COOKIE_ENCRYPTION_SECRET
from .utility import Autherize, EmailSending  



pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
s = r'(0|91)?[6-9][0-9]{9}'
class UserCreation(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():                
            if(request.data['role']=="2" and Organization.objects.get(id=request.data['organization'])):
                if re.match(pat,request.data['email']) and (True if request.data.get('ph_num', '') == '' else re.match(s, request.data['ph_num'])):
                    serializer.validated_data['password'] = hash_password(serializer.validated_data['password'])
                    serializer.save()
                    return Response({"status": "success", "user_id": serializer.data['id']}, status=status.HTTP_200_OK)
                else:
                    return Response({"status": "error", "data": "Invalid email or Phone number"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({"status":"error", "Message":"Either Role != Student or Organisation != Registered"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    # Login API
    def post(self, request):
        try:
            user = User.objects.get(email = request.data['email'])
            if not user:
                return Response(
                    {"Message": "User with email does not exists"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            if check_password(request.data['password'], user.password):
                user.is_active = True
                user.save()

                payload = {
                    "id" : user.userid,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                    "iat": datetime.datetime.utcnow(),
                }

                token = jwt.encode(payload, COOKIE_ENCRYPTION_SECRET, algorithm = 'HS256')
                
                data = {
                    "user_id": user.id,
                    "role": user.role,
                }
                response =  Response(data, status=status.HTTP_200_OK)
                response.set_cookie(key='jwt', value=token, httponly=True, samesite='Strict')
                return response 
            return Response(
                {"Message": "Invalid Password"}, 
                status=status.HTTP_304_NOT_MODIFIED
            )
        except Exception as e:
            return Response(
                {"Message": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            ) 

    # update Profile API
    @Autherize()
    def put(self, request, **kwargs):
        User_instance = kwargs['user']
    
        if not User_instance:
            return Response(
                {"Message": "User with id does not exists"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        if(request.data.get('id', '') != '' or request.data.get('created_at', '') != '' or request.data.get('updated_at', '') != '' or request.data.get('is_active', '') != '' or request.data.get('role', '') != ''):
            return Response({"status":"error", "Message":"You cannot edit id, created by, updated by, is active and role through api call"}, status=status.HTTP_409_CONFLICT)
        if(request.data.get('email', '') != '' and not re.match(pat,request.data['email'])):
            return Response(
                {"Message": "Email != valid"}, 
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        if(request.data.get('ph_num', '') != '' and not re.match(s, request.data['ph_num'])):
            return Response(
                {"Message": "Phone number != valid"}, 
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        serializer = UserSerializer(instance=User_instance, data = request.data, partial=True)
        
        if serializer.is_valid():
            if(request.data.get('password', '') is not ''):
                serializer.validated_data['password'] = hash_password(serializer.validated_data['password'])
            serializer.save()
            return Response( status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Get Profile API
    @Autherize()
    def get(self, request, **kwargs):
        print("flag1")
        user = kwargs['user']
        data = {
            "user_id": user.id,
            "role": user.role,
            "name": user.name,
            "email": user.email,
            "ph_num": user.ph_num,
            "organization": user.organization.name,
            "is_active": user.is_active,
        }
        return Response(data, status=status.HTTP_200_OK)
    # Logout API
    @Autherize()
    def delete(self, request, **kwargs):
        user = kwargs['user']
        user.is_active = False
        user.save()
        response = Response(status=status.HTTP_200_OK)
        response.data = {'message': 'User logged out successfully'}
        response.delete_cookie('jwt')
        return response

#This will not require authorisation because it will be called before sign in
class OrganisationView(APIView):
    def __init__(self, **kwargs):
        self.Organizations = Organization.objects.filter(is_active=True)
        super().__init__(**kwargs)
    
    def get(self, request):
        data = []   
        for org in self.Organizations:
            data.append({
                "id": org.id,
                "name": org.name,
            })

        return Response(data, status=status.HTTP_200_OK)


class ClubAdminView(APIView):
    @Autherize("0")
    def get(self, request, **kwargs):
        user = kwargs['user']
        club_admins = User.objects.filter(role="1", organization = user.organization)
        data = []
        for ca in club_admins:
            data.append({
                "userid" : ca.userid,  
                "name" : ca.name,
                "email" : ca.email,
                "ph_num" : ca.ph_num,
                "is_locked" : ca.is_locked
            })
        response = Response()
        response.data = data
        return response
        
    @Autherize("0")
    def post(self, request, **kwargs):
        user = kwargs['user']
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = hash_password(serializer.validated_data['password'])
            serializer.save(role="1", organization = user.organization)
            return Response( status=status.HTTP_200_OK)
        return Response({"message" : "User Created"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @Autherize("0")
    def put(self, request, **kwargs):
        user = kwargs['user']
        _userid = request.data['userid']
        _islocked = request.data['islocked']

        # input check of __islocked 
        if _islocked not in [True, False]:
            return Response(
                {"Message": "islocked != valid"}, 
                status=status.HTTP_406_NOT_ACCEPTABLE
            )

        # check the club admin exists or not
        try:
            club_admin = User.objects.get(userid = _userid, organization = user.organization, role = "1")
        except User.DoesNotExist:
            return Response(
                {"Message": "Club Admin with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # update the club admin
        club_admin.is_locked = _islocked 
        print(club_admin.is_locked)
        club_admin.save()

        return Response( {"message" : "Updated User"}, status=status.HTTP_200_OK)


class EmailVarification(APIView):
    def get(self, request,token):
        if not token:
            return Response({"message" : "Token is missing"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            payload = jwt.decode(token, COOKIE_ENCRYPTION_SECRET, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({"message" : "Token is expired"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.get(userid = payload['userid'])
        user.is_verified = True
        user.save()
        
        return Response({"message" : "Email Varification Done"}, status=status.HTTP_200_OK)

    @Autherize()
    def post(self, request,token,**kwargs): # sending varification mail
        if not request.data['email']:
            return Response({"message" : "Email is missing"}, status=status.HTTP_400_BAD_REQUEST)
        
        mail_client = EmailSending(request.data['email'])
        res = mail_client.varification_mail()
            
        return Response({"message" : "Email Varification Mail Sent", "response" : res }, status=status.HTTP_200_OK)


class ForgetPassword(APIView):
    def get(): # for clicking the sent link
        pass

    def post(self, request): # posting the email address // mail the link
        if not request.data['email']:
            return Response({"message" : "Email is missing"}, status=status.HTTP_400_BAD_REQUEST)
        
        mail_client = EmailSending(request.data['email'])
        res = mail_client.reset_password()
        return Response({"message" : "Reset Link sent"}, status = status.HTTP_201_CREATED)
        

    def put(self, request): # chanfing the password
        token = request.data['token']
        password = request.data['password']

        try:
            payload = jwt.decode(token, COOKIE_ENCRYPTION_SECRET, 'HS256')
        except jwt.ExpiredSignatureError:
            return Response({"message" : "Cookie Expired"}, status = status.HTTP_408_REQUEST_TIMEOUT)

        try:
            user = User.objects.get(userid = payload['userid'])
        except:
            return Response({"message": "Invalid cookie"}, status = status.HTTP_404_NOT_FOUND)
        
        password = hash_password(password)
        user.password = password
        user.save()

        mail_client = EmailSending(user.email)
        res = mail_client.confirmation(user.name)
        return Response({"message" : "Password updated"}, status = status.HTTP_200_OK)

# class Oauth(APIView):
#     def get(self, request):
#         # Get {% provider_login_url 'google' %} and send in json response
        
# URL for google O-auth -> http://127.0.0.1:8000/accounts/google/login/

class OauthHelper(APIView):
    def get(self, request, org_id):
        try:
            payload = { "org_id" : org_id }
        except:
            return Response({"message" : "Organization id is missing"}, status=status.HTTP_400_BAD_REQUEST)
        
        token = jwt.encode(payload, COOKIE_ENCRYPTION_SECRET, algorithm='HS256')
        response = Response({"message" : "Token generated"}, status=status.HTTP_200_OK)
        response.set_cookie(key='org_id', value=token, httponly=True )
        return response