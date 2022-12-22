from rest_framework import status
from .serializer import UserSerializer
from .models import User, Organization
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import re
pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
s = r'(0|91)?[6-9][0-9]{9}'
class Userinfo(APIView):
    queryset= User.objects.all()
    def get(self, request, user_id):
        x = User.objects.values_list('name', 'email','ph_num', 'organization', 'role').filter(id = user_id)
        x= x[0]
        return Response({"name": x[0], "email": x[1], "ph_num":x[2], "organization": x[3], "role": x[4]},status=status.HTTP_200_OK)
class UserCreation(APIView):
    queryset= User.objects.all()
    def post(self, request):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                
                if(request.data['role']=="student" and Organization.objects.get(id=request.data['organization'])):
                    if re.match(pat,request.data['email']) and (True if request.data.get('ph_num', '') is '' else re.match(s, request.data['ph_num'])):
                            serializer.save()
                            return Response({"status": "success", "user_id": serializer.data['id']}, status=status.HTTP_200_OK)
                    else:
                        return Response({"status": "error", "data": "Invalid email or Phone number"}, status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return Response({"status":"error", "Message":"Either Role is not Student or Organisation is not Registered"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
            try:
                user_id = User.objects.filter(email = request.data['email'], password=request.data['password']).values()[0]['id']
                role = User.objects.filter(email = request.data['email'], password=request.data['password']).values()[0]['role']
                organization_id = User.objects.filter(email = request.data['email'], password=request.data['password']).values()[0]['organization_id']
                return Response({"status": "success", "user_id": user_id, "role": role,"organization_id":organization_id}, status=status.HTTP_202_ACCEPTED)
            except:
                return Response({"status": "Error", "data": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    def put(self, request, user_id):
        User_instance = User.objects.get(id = user_id)
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
            return Response({"status":"success","user id":user_id}, status=status.HTTP_200_OK)
        return Response({"status":"success", "Message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

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