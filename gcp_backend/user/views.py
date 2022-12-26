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
from .utility import Autherize

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
                    "iat": datetime.datetime.utcnow()
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
                status=status.HTTP_400_BAD_REQUEST
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


# Addition of Organization --> Handeled by Admin
# Addition of club admin -< Handeled by Organization Admin
# -- needed api > get all club admin, create club admin, lock club admin, unlock club admin
# -- Extend view, update, login, logout, get profile for club admin & organization admin, also send user type in response
# -- email validation for normal user
# -- forget user
# -- O-auth

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


