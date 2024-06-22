import  tkinter as tk
from tkinter import filedialog
from moviepy.editor import *

root = tk.Tk()
root.withdraw()

file_path_1 = filedialog.askopenfilename(filetypes=[("mp4 Files",".mp4"), ("Mov Files",".mov")])
file_path_2 = filedialog.askopenfilename(filetypes=[("mp4 Files",".mp4"), ("Mov Files",".mov")])

try:
    vid1 = VideoFileClip(file_path_1)
    vid1 = vid1.margin(left=0, right=20, top=0, bottom=0)
    v1_txt_clip = TextClip(file_path_1, fontsize = 30, color = 'white') 
    v1_txt_clip = v1_txt_clip.set_pos('bottom', 'left').set_duration(10) 
    vid1 = CompositeVideoClip([vid1, v1_txt_clip]) 
except IOError:
    print ('No file specified for file 1.')

try:
    vid2 = VideoFileClip(file_path_2)
    v2_txt_clip = TextClip(file_path_2, fontsize = 30, color = 'white') 
    v2_txt_clip = v2_txt_clip.set_pos('bottom', 'left').set_duration(10) 
    vid2 = CompositeVideoClip([vid2, v2_txt_clip]) 
except IOError:
    print ('No file specified for file 2.')

try:
    combined = clips_array([[vid1, vid2]])
    combined.write_videofile('VideoDiff.mp4')
except NameError:
    print("Missing files. Reload script and try again.")