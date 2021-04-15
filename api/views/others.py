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

class MembersList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class PostQuery(generics.CreateAPIView):
    queryset = Queries.objects.all()
    serializer_class = QuerySerializer