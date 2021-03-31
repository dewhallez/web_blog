from django.contrib import admin

# Register your models here.
from web_blogs.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)