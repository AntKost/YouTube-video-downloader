import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from pytube import YouTube

root = tk.Tk()
root.geometry("760x480")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="white")

def Widgets():
    lbl_link = Label(root, font=("Courier", 14), width=15, height=2, text="Video link:", fg="white", bg="#80CFB6")
    lbl_link.grid(row=1, column=0, pady=10, padx=10)
    root.ent_link = Entry(root, font=("Courier", 12), width=55, fg="white", bg="#80CFB6", textvariable=video_link)
    root.ent_link.grid(row=1, column=1, padx=5, pady=5, columnspan=2)
    lbl_destination = Label(root, font=("Courier", 14), width=15, height=2, text="Destination:", fg="white", bg="#80CFB6")
    lbl_destination.grid(row=2, column=0, pady=10, padx=10)
    root.ent_destination = Entry(root, font=("Courier", 12), width=42, fg="white", bg="#80CFB6", textvariable=download_path)
    root.ent_destination.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    btn_browse = Button(root, font=("Courier", 14), width=10, height=1, text="Browse", command=Browse, fg="white", bg="#7DC5DB")
    btn_browse.grid(row=2, column=2, pady=1, padx=5, sticky="e")
    btn_download = Button(root, font=("Courier", 14), text="Download", command=Download, width=20, fg="white", bg="#7DC5DB")
    btn_download.grid(row=3, column=1, pady=10, padx=3)

def Browse():
    download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    download_path.set(download_directory)

def Download():
    youtube_link = video_link.get()
    download_folder = download_path.get()
    get_video = YouTube(youtube_link)
    video_stream = get_video.streams.first()
    video_stream.download(download_folder)
    messagebox.showinfo("Successfully downloaded and saved in\n" + download_folder)

video_link = StringVar()
download_path = StringVar()

Widgets()
root.mainloop()