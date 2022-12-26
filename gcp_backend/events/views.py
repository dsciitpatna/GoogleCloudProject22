from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Subscription, Tag, Type
from user.models import User
from .serializer import EventSerializer, SubscriptionSerializer, TagSerializer, TypeSerializer
import datetime, re
from datetime import datetime, date
from user.utility import autherize
import jwt
from gcp_backend.settings import COOKIE_ENCRYPTION_SECRET
#  Create your views here.
regex = r"\d{4}-\d{1,2}-\d{1,2}"
format = "%Y-%m-%d"

def to_python(value: str) -> date:
    return datetime.strptime(value, format).date()
class EventCreation(APIView):
    @autherize
    def post(self, request, **kwargs):

        serializer = EventSerializer(data=request.data)
        user = kwargs['user']
        role = kwargs['role']
        if not user:
            return Response(
                {"Message": "User with id does not exists"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        if user.organization.id is '':
            return Response(
                {"status":"error",
                    "Message": "Organisation with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if role != "1":
            return Response(
                {"status":"error",
                    "Message": "User is not club admin"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        request.data["created_by"] = user.id
        request.data["organization"] = user.organization.id
        if serializer.is_valid():
                serializer.save()
                return Response({"status":"success","Message":"Event Added Successfully"}, status=status.HTTP_201_CREATED)
            
        else:
                return Response({"status":"error","Message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    @autherize
    def put(self, request, **kwargs):
        event_id = request.GET.get('event_id','')
        user = kwargs['user']
        role = kwargs['role']
        if event_id is '':
            return Response(
                {"status":"error",
                    "Message": "Event with id does not exists"}, 
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        if user.organization.id is '':
            return Response(
                {"status":"error",
                    "Message": "Organisation with id does not exists"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        Event_instance = Event.objects.get(id = event_id)
        if not Event_instance:
            return Response(
                {"status":"error","Message": "Event with id does not exists"}, 
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        if role != "1":
            return Response(
                {"status":"error",
                    "Message": "User is not club admin"}, 
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        if(request.data.get('organization', '') is not '' or request.data.get('created_by', '') is not ''):
                        return Response(
                {"status":"error",
                    "Message": "Cannot edit Organisation name or created by"}, 
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = EventSerializer(instance=Event_instance, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "Message":"Update Successful"}, status=status.HTTP_202_ACCEPTED)
        return Response({"status":"error", "Message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    



class SubscriptionCreation(APIView):
    @autherize
    def post(self, request, **kwargs):
        user = kwargs['user']
        request.data['user'] = user.id
        serializer = SubscriptionSerializer(data=request.data)
        
        if serializer.is_valid():
                
                if(Event.objects.get(id = request.data['event'], organization=user.organization.id)):
                    serializer.save()
                    return Response({"status":"success", "Message":"Subscription Added Successfully"}, status=status.HTTP_201_CREATED)
                else :
                    return Response({"status":"error","Message": "Your Organisation doesn't have this event"}, status=status.HTTP_404_NOT_FOUND)
        else:
                    return Response({"status":"error","Message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    @autherize
    def get(self, request, **kwargs):
                b = []
                user = kwargs['user']
                for i in Subscription.objects.all().filter(user=user.id):
                    c= [x.tag for x in Tag.objects.all().filter(event = i.event.id)]
                    b.append({"id":i.event.id, "nane":i.event.name, "description": i.event.description, "start_Date":i.event.start_date, "end_date": i.event.end_date, "social_links": i.event.social_links, "rsvp_link":i.event.rsvp_link, "type": i.event._type.type, "tag": c})

        

                return Response(b, status=status.HTTP_200_OK)
class TagView(APIView):
<<<<<<< HEAD
    def get(self, request):
        alltags = Tag.objects.all()
        data = []
        for tag in alltags:
            data += [{"tag":tag.tag, "id":tag.id}]
        return Response(data, status=status.HTTP_200_OK)
        

    def post(self, request):
        user_id = request.GET.get('user_id', '')
        if user_id is '' or not User.objects.get(id = user_id):
            return Response(
                {"status":"error",
                    "Message": "User doesn't exist"}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        if User.objects.values_list('role').filter(id = user_id)[0][0] != "club_admin":
=======
    @autherize

    def get(self, request, **kwargs):
        role = kwargs['role']
        a = []
        for i in Tag.objects.all():
            a.append({"tag": i.tag, "id": i.id})
        

        return Response([a, role], status=status.HTTP_200_OK)
    
    @autherize
    def post(self, request, **kwargs):
        user = kwargs['user']
        role = kwargs['role']        
        if user.role != "1":
>>>>>>> a1851bd47454c9cfb4b08887b2a3de084975ad49
            return Response(
                {"status":"error",
                    "Message": "User is not club admin"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():

                serializer.save()
                return Response({"status":"success","Message":"Tag Added Successfully."}, status=status.HTTP_201_CREATED)
            
        else:
                return Response({"status":"error","Message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class Filter(APIView):
    @autherize
    def get(self, request, **kwargs):
        a =list()
        user = kwargs['user']
        q ={'organization': user.organization.id}
        sdate = request.GET.get('str_date','')
        if(sdate is not ''):
            q.update({'start_date__gte':to_python(sdate)})
        edate = request.GET.get('end_date','')
        if(edate is not ''):
            q.update({'end_date__lte':to_python(edate)})
        tag = request.GET.get('tag','')
        if(tag is not ''):
            q.update({'tags': tag})
        _type = request.GET.get('type','')
        if (_type is not ''):
            q.update({'_type':_type})
        b= []
        for i in  Event.objects.all().filter(**q):
            c = [x.tag for x in Tag.objects.all().filter(event = i.id)]
            b.append({"id":i.id, "name":i.name,'description':i.description, 'start_date':i.start_date,'end_date':i.end_date,'social_links':i.social_links,'rsvp_link':i.rsvp_link,'tags':c,'Type':i._type.type})
            

        return Response(b, status=status.HTTP_200_OK)

class TypeView(APIView):
    @autherize
    def get(self, request, **kwargs):
        a = []
        for i in Type.objects.all():
            a.append({"Type": i.type, "id": i.id})
        

        return Response(a, status=status.HTTP_200_OK)
    @autherize
    def post(self, request, **kwargs):
        user =kwargs['user']
        role = kwargs['role']
        if role != "1":
            return Response(
                {"status":"error",
                    "Message": "User is not club admin"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response({"status":"success","Message":"Type Added Successfully."}, status=status.HTTP_201_CREATED)
            
        else:
                return Response({"status":"error","Message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
