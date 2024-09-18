import subprocess
input = 'videoapp/media/videos/6548176-hd_1920_1080_24fps_jUWFyMT.mp4'
output = 'D:\Django\subtitle\ouputfile.srt'

def extract(input, output,stream_index=0):
    command = [
                'ffmpeg',
                '-i', input,        # Input video file
                '-map', f'0:s:{stream_index}',  # Select subtitle stream
                output]             # Output subtitle file
    subprocess.run(command, check=True)

extract(input, output)