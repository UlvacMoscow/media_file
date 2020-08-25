# ссылка для подготовки 
# https://www.geeksforgeeks.org/video-to-audio-convert-using-python/

# Python code to convert video to audio 
import moviepy.editor as mp 
  
# Insert Local Video File Path  
clip = mp.VideoFileClip(r"source.gif", audio=True) 
  
# Insert Local Audio File Path
clip.write_videofile("result.mp4", audio=r"audio.wav")



