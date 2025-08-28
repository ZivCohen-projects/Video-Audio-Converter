import subprocess
import os

def convert_video_to_mp3(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "44100",
        "-y",
        output_file ]
        
    try:
        subprocess.run(ffmpeg_cmd, check = True)
        print("Successfully Converted!")
    except subprocess.CalledProcessError as e:
        print("Conversion failed")
        

