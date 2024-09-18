from django.db import models

# Create your models here.

class VideoUpload(models.Model):
    title = models.CharField(max_length=250)
    video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add= True)

class Subtitle(models.Model):
    video = models.ForeignKey(VideoUpload, related_name='subtitles', on_delete=models.CASCADE)
    content = models.TextField()
    language = models.CharField(max_length=10, default= 'en')
