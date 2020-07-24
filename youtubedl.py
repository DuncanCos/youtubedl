#code by duncanCos

#import lybrary
import tkinter
from tkinter import filedialog, messagebox
from pytube import YouTube

#all the function


#function to get the info of the video(title and length of the video)
def info():
     yt = YouTube(var_entry.get())
     titletext.config(text="titre: " + yt.title)
     vidlength=yt.length/60
     lengthtext.config(text="temp de la video: " + str(vidlength) + "min")



#function to get the video in 720p
def chooseGoodVideo():
    yt = YouTube(var_entry.get())
    stream = yt.streams.get_highest_resolution()
    file_path= tkinter.filedialog.askdirectory()
    stream.download(file_path)
    messagebox.showinfo("telechargement finit", "La video ce trouve dans: " + file_path)

#function to get the video in 360p
def chooseBadVideo():
    yt = YouTube(var_entry.get())
    stream = yt.streams.get_lowest_resolution()
    file_path= tkinter.filedialog.askdirectory()
    stream.download(file_path)
    messagebox.showinfo("telechargement finit", "La video ce trouve dans: " + file_path)
    
    
#function to erase the video choose entry
def effacer ():
     var_entry.set("")

 #function to get the audio in mp4
def chooseAudio():
  
    yt = YouTube(var_entry.get())
    stream = yt.streams.filter(only_audio=True).first()
    file_path= tkinter.filedialog.askdirectory()
    stream.download(file_path)


#initialisation of the UI
app = tkinter.Tk()
app.title("youtube downloader")
app.minsize(300,200)


var_entry= tkinter.StringVar()

#creation of entry button and text

#creation of the entry
videoUrl = tkinter.Entry(app, textvariable=var_entry, width=60)

#creation of the button
butonsearch=tkinter.Button(app, text="info", command=info)
butonhighvideo = tkinter.Button(app, text="choisir la video en bonne qualité", command=chooseGoodVideo)
butonlowvideo = tkinter.Button(app, text="choisir la video en mauvaise qualité", command=chooseBadVideo)
butonAudio = tkinter.Button(app, text="choisir la musique", command=chooseAudio)
butonEfface = tkinter.Button(app, text="X", command=effacer)

#creation of the text
titletext=tkinter.Label(app, text="titre:")
lengthtext=tkinter.Label(app,text="durré de la video: ")



#position of the UI
videoUrl.grid(row=0, column=0)
butonEfface.grid(row=0, column=1)
butonsearch.grid(row=1, column=0)
titletext.grid(row=2, column=0)
lengthtext.grid(row=3, column=0)
butonhighvideo.grid(row=4, column=0)
butonlowvideo.grid(row=4, column=1)
butonAudio.grid(row=6, column=0)

app.mainloop() 
