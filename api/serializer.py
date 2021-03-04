from rest_framework import serializers
from api.models import Banner,MiniBanner,SuccessStory

class BannerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Banner
    fields = ['tag', 'heading1', 'heading2', 'tagline', 'subText', 'cta', 'img_url', 'bg_color']

class MiniBannerSerializer(serializers.ModelSerializer):
  class Meta:
    model = MiniBanner
    fields = ['tag', 'img_url']

class SuccessStorySerializer(serializers.ModelSerializer):
  class Meta:
    model = SuccessStory
    fields = ['title', 'subTitle', 'body', 'img', 'company_logo', 'company_name', 'college', 'course']