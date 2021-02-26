from rest_framework import serializers
from api.models import Banner

class BannerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Banner
    fields = ['tag', 'heading1', 'heading2', 'tagline', 'subText', 'cta', 'img_url', 'bg_color']