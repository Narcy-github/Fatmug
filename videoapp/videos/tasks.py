import subprocess
from celery import shared_task
from .models import VideoUpload, Subtitle

@shared_task
def process_video(video_id):
    print("process_video stated..")
    video = VideoUpload.objects.get(id = video_id)
    video_path = video.video_file.path
    subtitle_path = f"{video_path}.vtt"
    stream_index = 0

    command = [
                'ffmpeg',
                '-i', video_path,        # Input video file
                '-map', f'0:s:{stream_index}',  # Select subtitle stream
                subtitle_path]             # Output subtitle file
    
    try:
    # Run the ffmpeg command
        subprocess.run(command, stderr=subprocess.PIPE, check=True)

        with open(subtitle_path, 'r') as file:
            print("opening srt file..")
            subtitles = file.read()
            Subtitle.objects.create(video=video, content =subtitles, language = 'en' )
    except subprocess.CalledProcessError as e:
    # Print out the error message for debugging
        print(f"Error: {e.stderr.decode('utf-8')}")