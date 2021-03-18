from rest_framework import serializers
from api.models import *
import time

class TimestampField(serializers.Field):
    def to_representation(self, value):
        return int(time.mktime(value.timetuple()))

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
    fields = ['title', 'subTitle', 'body', 'img', 'college', 'course']
class CompanySerializer(serializers.ModelSerializer):
  success_story = SuccessStorySerializer()
  class Meta:
    model = Company
    fields = ['name', 'logo', 'success_story']    

class QuerySerializer(serializers.ModelSerializer):
  class Meta:
    model = Queries
    fields = ['name', 'email', 'phoneNo', 'description', 'type']

class MemberSerializer(serializers.ModelSerializer):
  class Meta:
    model = Member
    fields = ['name', 'contact', 'img', 'description', 'designation']   

class CentreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Centre
    fields = ['name']

class BatchSerializer(serializers.ModelSerializer):
  centre = CentreSerializer()

  class Meta:
    model = Batch
    fields = ['mrp', 'buyLink', 'enrollmentEndDate', 'startDate', 'endDate', 'price', 'centre']      

class CourseSerializer(serializers.ModelSerializer):
  batches = BatchSerializer(source='batch_set', many=True)
  mentors = MemberSerializer(many=True)

  class Meta:
    model = Course
    fields = ['title', 'description', 'logo', 'theme', 'rating', 'number_ratings', 'video_link', 'languages', 'duration', 'slug', 'difficulty','batches','mentors','projects', 'syallabus',  'highlights']
    lookup_field = 'slug'
    extra_kwargs = {
      'url': {'lookup_field': 'slug'}
    }    