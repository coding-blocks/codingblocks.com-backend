from django.http import HttpResponse, Http404
from api.models import *
from api.serializer import *
from rest_framework import generics
from rest_framework.views import APIView

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class BannerList(generics.ListAPIView):
    queryset = Banner.objects.all()[:3]
    serializer_class = BannerSerializer

class SuccessStoryList(generics.ListAPIView):
    queryset = SuccessStory.objects.all()[:5]
    serializer_class = SuccessStorySerializer
    
class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_fields = ['title']
  

class MembersList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer    

class PostQuery(generics.CreateAPIView):
    queryset = Queries.objects.all()
    serializer_class = QuerySerializer

class Universe(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

class MiniBanner(generics.RetrieveAPIView):
    queryset = MiniBanner.objects.all()
    serializer_class = MiniBannerSerializer

    def get_object(self):
        try:
            return self.get_queryset()[0]
        except:
            raise Http404

class CourseRetrieveView(generics.RetrieveAPIView):
    queryset = Course.objects.all().prefetch_related('batch_set')
    serializer_class = CourseSerializer
    lookup_field = 'slug'







