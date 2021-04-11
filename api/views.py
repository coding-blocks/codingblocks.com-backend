from django.http import HttpResponse, Http404
from api.models import *
from api.serializer import *
from rest_framework import generics
from rest_framework.views import APIView
from django.db.models import Prefetch, Q
import datetime


class BannerList(generics.ListAPIView):
    queryset = Banner.objects.all()[:3]
    serializer_class = BannerSerializer


class TopStoriesList(generics.ListAPIView):
    queryset = SuccessStory.objects.all()[:5]
    serializer_class = SuccessStorySerializer


class SuccessStoryList(generics.ListAPIView):
    queryset = SuccessStory.objects.all()
    serializer_class = SuccessStorySerializer


class MembersList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class PostQuery(generics.CreateAPIView):
    queryset = Queries.objects.all()
    serializer_class = QuerySerializer


class MiniBanner(generics.RetrieveAPIView):
    queryset = MiniBanner.objects.all()
    serializer_class = MiniBannerSerializer

    def get_object(self):
        try:
            return self.get_queryset()[0]
        except:
            raise Http404


class CourseList(generics.ListAPIView):
    queryset = Course.objects.prefetch_related(Prefetch('batch_set')).filter(batch__enrollmentEndDate__gte=datetime.date.today()).all()
    serializer_class = CourseSerializer
    filterset_fields = ['title']

    def get_queryset(self, *args, **kwargs):
        query = super().get_queryset(*args, **kwargs)

        centres = self.request.query_params.get('centres', None)
        if (centres):
            query = query.filter(
                batch__centre__name__in=centres.split(',')).distinct()

        return query


class CourseRetrieveView(generics.RetrieveAPIView):
    queryset = Course.objects.prefetch_related(Prefetch('batch_set')).filter(batch__enrollmentEndDate__gte=datetime.date.today()).all()
    serializer_class = CourseSerializer
    lookup_field = 'slug'


class UniverseRetrieveView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = UniverseSerializer

    def get_queryset(self, *args, **kwargs):
        query = super().get_queryset(*args, **kwargs)

        companies = ['Microsoft', 'Nagarro', 'Goldman']
        if (companies):
            query = query.filter(
                name__in=companies)

        return query


class EventsList(generics.ListAPIView):
    queryset = Event.objects.filter(eventDate__gte=datetime.date.today()).all()
    serializer_class = EventsSerializer
    filterset_fields = ['title']


class EventRetrieveView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    lookup_field = 'slug'
