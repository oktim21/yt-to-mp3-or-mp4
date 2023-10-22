from pytube import YouTube
import os

# Function to download a video from a given URL
def download_video(url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Choose the stream with the best video quality (MP4 format)
        video_stream = yt.streams.filter(file_extension="mp4").get_audio_only()
        # Download the video to the specified output path
        video_stream.download(output_path)

        print(f"Downloaded {yt.title} successfully to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def download_vid(url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Choose the stream with the best video quality (MP4 format)
        video_stream = yt.streams.filter(file_extension="mp4").get_highest_resolution()
        # Download the video to the specified output path
        video_stream.download(output_path)

        print(f"Downloaded {yt.title} successfully to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    check = input("Do you want an mp3 or mp4")
    if check == "mp3":
           directory = input("The name of the folder you want to keep your music(it will create it for you if you don't have): ")
           parent_directory = input("The directory you want to keep your music (it will create it for you if you don't have): ")
           path = os.path.join( parent_directory,directory)
           try: 
               os.makedirs(path, exist_ok = True) 
               print("Directory '%s' created successfully" % directory) 
           except OSError as error: 
               print("Directory '%s' can not be created" % directory) 
           na = input("URL:")
           video_url = na
           output_directory = path 
           download_video(video_url, output_directory)
else:
    directory = input("The name of the folder you want to keep your music(it will create it for you if you don't have): ")
    parent_directory = input("The directory you want to keep your music (it will create it for you if you don't have): ")
    path = os.path.join( parent_directory,directory)
    try: 
               os.makedirs(path, exist_ok = True) 
               print("Directory '%s' created successfully" % directory) 
    except OSError as error: 
               print("Directory '%s' can not be created" % directory) 
    na = input("URL:")
    video_url = na
    output_directory = path 
    download_vid(video_url, output_directory)
    
    
        
 

