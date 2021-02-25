from rest_framework import serializers
from api.models import MiniBanner

class BannerSerializer(serializers.ModelSerializer):
  class Meta:
    model = MiniBanner
    fields = ['tag', 'img_url']