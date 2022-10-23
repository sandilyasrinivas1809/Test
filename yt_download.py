from pytube import YouTube
import os
user_input = str(input("Please paste the URL of the video you want to download: "))
yt = YouTube(f'{user_input}')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
directory = os.getcwd()
print(f"The video has been saved in mp4 format to this directory - {directory}")
