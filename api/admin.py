from django.contrib import admin

# Register your models here.

from .models import MiniBanner,Banner

admin.site.register(MiniBanner)
admin.site.register(Banner)

