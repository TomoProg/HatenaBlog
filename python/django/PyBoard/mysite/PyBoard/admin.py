from django.contrib import admin
from .models import Topic, TopicDetail

# Register your models here.

class TopicDetailInline(admin.StackedInline):
    model = TopicDetail
    extra = 3

class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'register_name',
        'register_datetime',
        'update_name',
        'update_datetime',
    )
    inlines = [TopicDetailInline]

admin.site.register(Topic, TopicAdmin)

