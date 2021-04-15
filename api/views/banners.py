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
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class BannerList(generics.ListAPIView):

    @method_decorator(cache_page(60*60))
    def dispatch(self, *args, **kwargs):
        return super.dispatch(*args, **kwargs) 

    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class MiniBanner(generics.RetrieveAPIView):
    queryset = MiniBanner.objects.all()
    serializer_class = MiniBannerSerializer

    @method_decorator(cache_page(60*60))
    def dispatch(self, *args, **kwargs):
        return super.dispatch(*args, **kwargs) 


    def get_object(self):
        try:
            return self.get_queryset()[0]
        except:
            raise Http404