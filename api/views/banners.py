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

class BannerList(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class MiniBanner(generics.RetrieveAPIView):
    queryset = MiniBanner.objects.all()
    serializer_class = MiniBannerSerializer

    def get_object(self):
        try:
            return self.get_queryset()[0]
        except:
            raise Http404