from django.contrib import admin

# Register your models here.

from .models import MiniBanner,Banner,SuccessStory

admin.site.register(MiniBanner)
admin.site.register(Banner)
admin.site.register(SuccessStory)

