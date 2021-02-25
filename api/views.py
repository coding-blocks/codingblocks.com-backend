from django.http import HttpResponse
from api.models import MiniBanner
from api.serializer import BannerSerializer
from rest_framework import generics

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def banners(request):
#     latest_banner = MiniBanner.objects.all()
#     data = serializers.serialize('json', latest_banner)
#     return HttpResponse(data)

class BannerList(generics.ListAPIView):
    queryset = MiniBanner.objects.all()
    serializer_class = BannerSerializer


