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

class UniverseRetrieveView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = UniverseSerializer

    @method_decorator(cache_page(60*60))
    def dispatch(self, *args, **kwargs):
        return super.dispatch(*args, **kwargs) 

    def get_queryset(self, *args, **kwargs):
        query = super().get_queryset(*args, **kwargs)

        companies = ['Microsoft', 'Nagarro', 'Goldman']
        if (companies):
            query = query.filter(
                name__in=companies)

        return query