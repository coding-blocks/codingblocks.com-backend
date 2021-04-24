from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget
from .models import *

admin.site.register(MiniBanner)
admin.site.register(Banner)
admin.site.register(SuccessStory)
admin.site.register(Batch)
admin.site.register(Centre)
admin.site.register(Queries)
admin.site.register(Company)
admin.site.register(Event)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }