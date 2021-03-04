from django.http import HttpResponse, Http404
from api.models import Banner,MiniBanner,SuccessStory
from api.serializer import BannerSerializer,MiniBannerSerializer,SuccessStorySerializer
from rest_framework import generics

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def banners(request):
#     latest_banner = MiniBanner.objects.all()
#     data = serializers.serialize('json', latest_banner)
#     return HttpResponse(data)

class BannerList(generics.ListAPIView):
    queryset = Banner.objects.all()[:3]
    serializer_class = BannerSerializer

class SuccessStoryList(generics.ListAPIView):
    queryset = SuccessStory.objects.all()[:5]
    serializer_class = SuccessStorySerializer
class MiniBanner(generics.RetrieveAPIView):
    queryset = MiniBanner.objects.all()
    serializer_class = MiniBannerSerializer

    def get_object(self):
        try:
            return self.get_queryset()[0]
        except:
            raise Http404


