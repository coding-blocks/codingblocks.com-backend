from django.http import HttpResponse, Http404
from api.models import *
from api.serializer import *
from services.oneauth import get_oneauth_service
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Prefetch, Q
from utils.config import Config
from urllib.parse import urljoin
import datetime
import requests
import json
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class EventsList(generics.ListAPIView):

    @method_decorator(cache_page(60*60))
    def dispatch(self, *args, **kwargs):
        return super.dispatch(*args, **kwargs) 

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
        serializer = EventCallbackSerializer(data=request.data)
        if serializer.is_valid() :
            code = serializer.data['code']
            events_slug = serializer.data['event']
            event = Event.objects.get(slug=events_slug)

            oneauth_service = get_oneauth_service()
            user = oneauth_service.exchange_grant_with_user(code, urljoin(Config.PUBLIC_URL, 'events/callback'))
            body = json.loads(user.content)
            serializer = EventRegistrationSerializer(data={'oneauthId': body['id'], 'user': body, 'event': event.id})
            if serializer.is_valid(raise_exception=True) :
                serializer.save()  
            return Response(user)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
