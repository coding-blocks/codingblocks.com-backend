from rest_framework import serializers
from api.models import *

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

class QuerySerializer(serializers.ModelSerializer):
  class Meta:
    model = Queries
    fields = ['name', 'email', 'phoneNo', 'description', 'type']

class MemberSerializer(serializers.ModelSerializer):
  class Meta:
    model = Member
    fields = ['name', 'contact', 'img', 'description', 'designation']    