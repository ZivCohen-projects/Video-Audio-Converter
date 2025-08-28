import subprocess

def convert_video_to_mp3(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "44100",
        "-y",
        output_file
    ]
    
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Successfully Converted!")
    except subprocess.CalledProcessError:
        print("Conversion failed")

def main():
    filepath = input("Drag and drop your video file here: ").strip()
    
    if filepath.startswith("& "):
        filepath = filepath[2:]
    filepath = filepath.strip('"').strip("'")
    
    if filepath.lower().endswith((".mov", ".mp4")):
        filename = filepath.replace("\\", "/").split("/")[-1]
        name_without_ext = ".".join(filename.split(".")[:-1])
        output_file = f"audio_{name_without_ext}.mp3"
        
        convert_video_to_mp3(filepath, output_file)
    else:
        print("File is not a supported video")

main()
