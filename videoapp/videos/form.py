from django import forms
from .models import VideoUpload, Subtitle

class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoUpload
        fields  = ['title', 'video_file']

