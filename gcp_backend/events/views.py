from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Subscription, Tag, Type
from user.models import User
from .serializer import EventSerializer, SubscriptionSerializer, TagSerializer
import datetime, re
from datetime import datetime, date
#  Create your views here.
regex = r"\d{4}-\d{1,2}-\d{1,2}"
format = "%Y-%m-%d"

def to_python(value: str) -> date:
    return datetime.strptime(value, format).date()
class EventCreation(APIView):
    queryset= Event.objects.all()
    def post(self, request):

        serializer = EventSerializer(data=request.data)
        org_id = request.GET.get('org_id', '')
        user_id = request.GET.get('user_id', '')
        if org_id is '':
            return Response(
                {"status":"error",
                    "Message": "Organisation with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if user_id is '' or not User.objects.get(organization = org_id, id = user_id):
            return Response(
                {"status":"error",
                    "Message": "User doesn't exist within organisation"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        if User.objects.values_list('role').filter(id = user_id)[0][0] != "club_admin":
            return Response(
                {"status":"error",
                    "Message": "User is not club admin"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        if serializer.is_valid():
                serializer.save()
                return Response({"status":"success","Message":"Event Added Successfully"}, status=status.HTTP_201_CREATED)
            
        else:
                return Response({"status":"error","Message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        event_id = request.GET.get('event_id','')
        org_id = request.GET.get('org_id', '')
        user_id = request.GET.get('user_id', '')
        if event_id is '':
            return Response(
                {"status":"error",
                    "Message": "Event with id does not exists"}, 
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        if org_id is '':
            return Response(
                {"status":"error",
                    "Message": "Organisation with id does not exists"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        if user_id is '' or not User.objects.get(organization = org_id, id = user_id):
            return Response(
                {"status":"error",
                    "Message": "User doesn't exist within organisation"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        Event_instance = Event.objects.get(id = event_id)
        if not Event_instance:
            return Response(
                {"status":"error","Message": "Event with id does not exists"}, 
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        if User.objects.values_list('role').filter(id = user_id)[0][0]!="club_admin":
            return Response(
                {"status":"error",
                    "Message": "User is not club admin"}, 
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        if(request.data.get('organization', '') is not '' and request.data.get('created_by', '') is not ''):
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
    queryset= Subscription.objects.all()
    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        
        if serializer.is_valid():
                
                if(Event.objects.get(id = request.data['event'], created_by=request.data['user'])):
                    serializer.save()
                    return Response({"status":"success", "Message":"Subscription Added Successfully"}, status=status.HTTP_201_CREATED)
                else :
                    return Response({"status":"error","Message": "Your Organisation doesn't have this event"}, status=status.HTTP_404_NOT_FOUND)
        else:
                    return Response({"status":"error","Message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        user_id = request.GET.get('user_id', '')
        if user_id is '':
            return Response({"status":"error", "Message":"User id not Provided"}, status =status.HTTP_401_UNAUTHORIZED)
        a = list()
        for i in Subscription.objects.values_list('id').filter(user_id=user_id):
            i = i[0]
            a.append(i)
        b = []
        if(len(a)):
            for i in a:
                z = Subscription.objects.values_list('event_id').filter(id = i)
                z = z[0][0]
                x = Event.objects.values_list('id','name','description', 'start_date', 'end_date','social_links','rsvp_link','image').filter(id=z)
                x = x[0]
                c = []
                y = Event.objects.values_list('tags').filter(id = i)
                for j in y:
                    for z in j:
                        if(y!=None):
                            m = Tag.objects.values_list('tag').filter(id = z)
                            if(len(m)!=0):
                                m = m[0][0]
                                
                            c.append(m)
                d =Event.objects.values_list('_type').filter(id=i)
                e = []
                for j in d:
                    for z in j:
                        if(y!=None):
                            m = Type.objects.values_list('type').filter(id = z)
                            if(len(m)!=0):
                                m = m[0][0]
                                
                            e.append(m)
                b.append({"id":x[0], "name":x[1],'description':x[2], 'start_date':x[3],'end_date':x[4],'social_links':x[5],'rsvp_link':x[6],'image':x[7],'tags':c,'Type':e[0]})

        

        return Response({"Number":len(a), "List": b}, status=status.HTTP_200_OK)
class TagView(APIView):
    def get(self, request):
        a = list()
        for i in Tag.objects.values_list('id').filter():
            i = i[0]
            a.append(i)
        b = []
        for i in a:
            x = Tag.objects.values_list('tag').filter(id = i)
            x = x[0]
            b.append({"tag":x[0], "id":i})
        

        return Response(b, status=status.HTTP_200_OK)

class Filter(APIView):
    def get(self, request, org_id):
        a =list()
        q ={'organization': org_id}
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
        a =list()
        for i in  Event.objects.values_list('id').filter(**q):
            i = i[0]
            a.append(i)
        b= []
        for i in a:
            x = Event.objects.values_list('id','name','description', 'start_date', 'end_date','social_links','rsvp_link','image').filter(id=i)
            x = x[0]
            c = []
            y = Event.objects.values_list('tags').filter(id = i)
            for j in y:
                for z in j:
                    if(y!=None):
                        m = Tag.objects.values_list('tag').filter(id = z)
                        if(len(m)!=0):
                            m = m[0][0]
                            
                        c.append(m)
            d =Event.objects.values_list('_type').filter(id=i)
            e = []
            for j in d:
                for z in j:
                    if(y!=None):
                        m = Type.objects.values_list('type').filter(id = z)
                        if(len(m)!=0):
                            m = m[0][0]
                            
                        e.append(m)
            b.append({"id":x[0], "name":x[1],'description':x[2], 'start_date':x[3],'end_date':x[4],'social_links':x[5],'rsvp_link':x[6],'image':x[7],'tags':c,'Type':e[0]})
            

        return Response(b, status=status.HTTP_200_OK)
