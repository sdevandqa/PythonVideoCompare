import  tkinter as tk
from tkinter import filedialog
from moviepy.editor import *

root = tk.Tk()
root.withdraw()
file_path_1 = filedialog.askopenfilename()
file_path_2 = filedialog.askopenfilename()

vid1 = VideoFileClip(file_path_1)
vid2 = VideoFileClip(file_path_2)

vid1 = vid1.margin(left=0, right=20, top=0, bottom=0)

v1_txt_clip = TextClip(file_path_1, fontsize = 30, color = 'white') 
v1_txt_clip = v1_txt_clip.set_pos('bottom', 'left').set_duration(10) 

v2_txt_clip = TextClip(file_path_2, fontsize = 30, color = 'white') 
v2_txt_clip = v2_txt_clip.set_pos('bottom', 'left').set_duration(10) 

vid1 = CompositeVideoClip([vid1, v1_txt_clip]) 
vid2 = CompositeVideoClip([vid2, v2_txt_clip]) 

combined = clips_array([[vid1, vid2]])
combined.write_videofile('VideoDiff.mp4')