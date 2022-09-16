from pytube import  YouTube  
import pytube  
try:
    video_url = 'https://www.youtube.com/watch?v=VSZD6BEVySg'   
    youtube = pytube.YouTube(video_url)  
    video = youtube.streams.filter(only_audio=True).first()  
    video.download(r'C:/Users/jcruna/OneDrive - Gerdau/Desktop/')  
    print("Download Successfull !!")
except:
    print("Something Went Wrong !!")