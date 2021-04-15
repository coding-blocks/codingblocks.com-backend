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


class CourseList(generics.ListAPIView):
    queryset = Course.objects.prefetch_related().all()
    serializer_class = CourseSerializer
    filterset_fields = ['title']

    def get_queryset(self, *args, **kwargs):
        query = super().get_queryset(*args, **kwargs)
        query = query.filter(batch__enrollmentEndDate__gte=datetime.date.today())
        centres = self.request.query_params.get('centres', None)
        if (centres):
            query = query.filter(
                batch__centre__name__in=centres.split(',')).distinct()

        return query


class CourseRetrieveView(generics.RetrieveAPIView):
    queryset = Course.objects.prefetch_related(Prefetch(
        'batch_set', queryset=Batch.objects.filter(enrollmentEndDate__gte=datetime.date.today()))).all()
    serializer_class = CourseSerializer
    lookup_field = 'slug'
