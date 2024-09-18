from django.shortcuts import render, redirect
from .models import VideoUpload, Subtitle
from .form import VideoForm
from .tasks import process_video
from django.db.models import Q
from django.contrib.postgres.search import SearchVector,SearchHeadline
from django.db.models import F

# Create your views here.
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            process_video(video.id)
            return redirect('list-videos')
    else:
        form = VideoForm()

    return render(request, 'videos/upload.html', {'form':form})

def list_videos(request):
    videos = VideoUpload.objects.all()
    return render(request, 'videos/videos.html', {'videos':videos})

def video_details(request, video_id):
    video = VideoUpload.objects.get(id = video_id)
    return render(request, 'videos/video_details.html', {'video':video})



def video_list(request):
    videos = VideoUpload.objects.all()
    return render(request, 'videos/video_list.html', {'videos': videos})

def search_subtitles(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        print("Entring into query mode...")
        results = Subtitle.objects.annotate(search=SearchVector('content'), 
                                            headline=SearchHeadline(F('content'), query)
                                            ).filter(Q(search=query))
        
    return render(request, 'videos/search.html', {'results': results, 'query': query})
