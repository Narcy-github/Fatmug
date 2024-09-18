from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.upload_video, name='upload-video'),
    path('list-videos/', views.list_videos, name= 'list-videos'),
    path('list-videos/<str:video_id>/', views.video_details, name= 'video-details'),
    path('search-subtitles', views.search_subtitles, name='search_subtitles'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
