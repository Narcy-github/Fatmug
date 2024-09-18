from django.contrib import admin

from .models import VideoUpload, Subtitle

# Register your models here.
admin.site.register(VideoUpload)
admin.site.register(Subtitle)
