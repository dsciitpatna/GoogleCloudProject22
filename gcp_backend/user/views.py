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
from .utility import autherize

pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
s = r'(0|91)?[6-9][0-9]{9}'
class UserCreation(APIView):
    # queryset= User.objects.all()
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if(request.data['role']=="2" and Organization.objects.get(id=request.data['organization'])):
                if re.match(pat,request.data['email']) and (True if request.data.get('ph_num', '') is '' else re.match(s, request.data['ph_num'])):
                    serializer.validated_data['password'] = hash_password(serializer.validated_data['password'])
                    serializer.save()
                    return Response({"status": "success", "user_id": serializer.data['id']}, status=status.HTTP_200_OK)
                else:
                    return Response({"status": "error", "data": "Invalid email or Phone number"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({"status":"error", "Message":"Either Role is not Student or Organisation is not Registered"}, status=status.HTTP_406_NOT_ACCEPTABLE)
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
    @autherize
    def put(self, request, **kwargs):
        User_instance = kwargs['user']
        if not User_instance:
            return Response(
                {"Message": "User with id does not exists"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        if(request.data.get('id', '') is not '' or request.data.get('created_at', '') is not '' or request.data.get('updated_at', '') is not '' or request.data.get('is_active', '') is not '' or request.data.get('role', '') is not ''):
            return Response({"status":"error", "Message":"You cannot edit id, created by, updated by, is active and role through api call"}, status=status.HTTP_409_CONFLICT)
        if(request.data.get('email', '') is not '' and not re.match(pat,request.data['email'])):
            return Response(
                {"Message": "Email is not valid"}, 
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        if(request.data.get('ph_num', '') is not '' and not re.match(s, request.data['ph_num'])):
            return Response(
                {"Message": "Phone number is not valid"}, 
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        serializer = UserSerializer(instance=User_instance, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response( status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Get Profile API
    @autherize
    def get(self, request, **kwargs):
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
    @autherize
    def delete(self, request, **kwargs):
        user = kwargs['user']
        user.is_active = False
        user.save()
        response = Response(status=status.HTTP_200_OK)
        response.data = {'message': 'User logged out successfully'}
        response.delete_cookie('jwt')
        return response


class OrganisationView(APIView):
    queryset = Organization.objects.all()
    def get(self, request):
        a = list()
        for i in Organization.objects.values_list('id').filter():
            i = i[0]
            a.append(i)
        b = []
        for i in a:
            x = Organization.objects.values_list('name').filter(id = i)
            x = x[0]
            b.append({"name":x[0], "id":i})
        

        return Response(b, status=status.HTTP_200_OK)
