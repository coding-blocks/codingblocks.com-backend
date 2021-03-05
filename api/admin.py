from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(MiniBanner)
admin.site.register(Banner)
admin.site.register(SuccessStory)
admin.site.register(Course)
admin.site.register(Queries)
admin.site.register(Company)
admin.site.register(Member)


