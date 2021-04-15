from django.http import HttpResponse, Http404
from api.models import *
from api.serializer import *
from services.oneauth import get_oneauth_service
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Prefetch, Q
import datetime
import requests
import json

class EventsList(generics.ListAPIView):
    queryset = Event.objects.filter(eventDate__gte=datetime.date.today()).all()
    serializer_class = EventsSerializer
    filterset_fields = ['title']


class EventRetrieveView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    lookup_field = 'slug'

class EventStatusView(APIView):

    def get(self, request, format=None):
        try:
            code = self.request.query_params.get('code', None)
            events_slug = self.request.query_params.get('slug', None)
            event = Event.objects.get(slug=events_slug)      
            isRegistered = EventRegistration.objects.get(event = event.id, oneauthId= code)
            if(isRegistered):
                content = {'isRegistered': True}
            else:
                content = {'isRegistered': False}
            return Response(content)
        except Exception as e:
            return Response({'isRegistered': False})


class EventsCallbackView(APIView):
    
    def post(self, request, format=None):
        try:
            serializer = EventCallbackSerializer(data=request.data)
            if serializer.is_valid() :
                code = serializer.data['code']
                events_slug = serializer.data['event']
                event = Event.objects.get(slug=events_slug)

                oneauth_service = get_oneauth_service()
                user = oneauth_service.exchange_grant_with_user(code)
                body = json.loads(user.content)
                serializer = EventRegistrationSerializer(data={'oneauthId': body['id'], 'user': body, 'event': event.id})
                if serializer.is_valid() :
                    serializer.save()
                else : 
                    print(serializer.errors)    
                return Response(user)
            print(serializer.errors)
            return Response({"a": "a"})
        except Exception as e:
            print(e)
            return Response({"error": str(e)})