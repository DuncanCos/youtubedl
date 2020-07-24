import tkinter
from tkinter import filedialog, messagebox
from pytube import YouTube

def info():
     yt = YouTube(var_entry.get())
     titletext.config(text="titre: " + yt.title)
     vidlength=yt.length/60
     lengthtext.config(text="temp de la video: " + str(vidlength) + "min")




def chooseGoodVideo():
    yt = YouTube(var_entry.get())
    stream = yt.streams.get_highest_resolution()
    file_path= tkinter.filedialog.askdirectory()
    stream.download(file_path)
    messagebox.showinfo("telechargement finit", "La video ce trouve dans: " + file_path)


def chooseBadVideo():
    yt = YouTube(var_entry.get())
    stream = yt.streams.get_lowest_resolution()
    file_path= tkinter.filedialog.askdirectory()
    stream.download(file_path)
    messagebox.showinfo("telechargement finit", "La video ce trouve dans: " + file_path)
    
    

def effacer ():
     var_entry.set("")


def chooseAudio():
  
    yt = YouTube(var_entry.get())
    stream = yt.streams.filter(only_audio=True).first()
    file_path= tkinter.filedialog.askdirectory()
    stream.download(file_path)



app = tkinter.Tk()
app.title("youtube downloader")
app.minsize(300,200)

var_entry= tkinter.StringVar()

videoUrl = tkinter.Entry(app, textvariable=var_entry)

butonsearch=tkinter.Button(app, text="info", command=info)
butonhighvideo = tkinter.Button(app, text="choisir la video en bonne qualité", command=chooseGoodVideo)
butonlowvideo = tkinter.Button(app, text="choisir la video en mauvaise qualité", command=chooseBadVideo)
butonAudio = tkinter.Button(app, text="choisir la musique", command=chooseAudio)
butonEfface = tkinter.Button(app, text="X", command=effacer)

titletext=tkinter.Label(app)
lengthtext=tkinter.Label(app)
dltext=tkinter.Label(app)

videoUrl.pack()
butonEfface.pack()

butonhighvideo.pack()
butonlowvideo.pack()
butonAudio.pack()
butonsearch.pack()
titletext.pack()
lengthtext.pack()
dltext.pack()

app.mainloop() 
