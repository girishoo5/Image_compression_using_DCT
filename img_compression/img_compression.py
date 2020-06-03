import PIL.Image
import cv2
import tkinter as tk
from tkinter import *
import os
import compression as p1a
import decompression as p1b
import time

def convert(seconds):
   seconds = seconds % (24 * 3600)
   seconds %= 3600
   minutes = seconds // 60
   seconds %= 60
   return "%02d:%02d" % ( minutes, seconds) #formatting

def dcompres():
    t1=time.time()
    p1b.abc()
    t2=time.time()
    t=str(convert(t2-t1))
    tk.Label(master,text="Decompression done  and saved as ").grid(row=34,column=6)
    tk.Label(master,text="uncompressed_imager.bmp  with execution time ").grid(row=36,column=6)
    tk.Label(master,text=t +"sec").grid(row=38,column=6)
    file_stats2=os.stat("uncompressed_image.png")
    size=file_stats2.st_size/ (1024 * 1024)
    tk.Label(master,text="Deccompressed image size:  "+str(round(size,2))+"MB").grid(row=40,column=6)

def compress():
    img=e1.get()
    if img!="":
        imge=cv2.imread(img,cv2.IMREAD_GRAYSCALE )
        cv2.imshow("original image in grayscale",imge)
        t1= time.time()
        p1a.abc(img)
        t2=time.time()
        t=str(convert(t2-t1))
        tk.Label(master,text="Compression done  and saved as img.txt \n with execution time"+ t +"sec").grid(row=16,column=6)   
        file_stats = os.stat(img)
       
        file_stats1 = os.stat("image.txt")
        size=file_stats.st_size/ (1024 * 1024)
        size1=file_stats1.st_size/ (1024 * 1024)
        tk.Label(master,text="original image size:  "+str(round(size,2))+"MB").grid(row=18,column=6)
        tk.Label(master,text="compressed txt file size:"+str(round(size1,2))+"MB").grid(row=20,column=6)

master = tk.Tk()
#master.geometry("400x400")
master.title("Image Compression using DCT")
#for img input 
label1=tk.Label(master,text="Img Name").grid(row=1,column=5)      

tk.Label(master,text="Note image wil be converted to grayscale ").grid(row=4,column=6) 
tk.Label(master,text="and then compressed and decompressed").grid(row=6,column=6)
tk.Label(master,text="resulting in grayscale img as output").grid(row=8,column=6)
tk.Label(master,text="even if original image is in RGB").grid(row=10,column=6)  
e1 = tk.Entry(master, width=20)

e1.grid(row=1, column=6)

tk.Button(master,text='Quit', command=master.quit).grid(row=14,column=12,sticky=tk.W,pady=4)  
tk.Button(master,text='Compress', command=compress).grid(row=14,column=5,sticky=tk.W,pady=4)
tk.Button(master,text='Decompress', command=dcompres).grid(row=14,column=6,sticky=tk.W,pady=4)
                               
tk.mainloop()