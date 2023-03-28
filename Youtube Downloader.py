import tkinter as tk
import pytube.exceptions
from pytube import YouTube
from tkinter import ttk
from sys import platform
from pathlib import Path


def divider(bytes, x):
    if (bytes % x) / x < 0.1:
        return round(bytes / x)
    else:
        return round(bytes / x, 1)


def size_converter(bytes):
    if bytes > 1048576:
        return str(divider(bytes, 1048576)) + " MB"
    elif bytes > 1024:
        return str(divider(bytes, 1024)) + " KB"
    else:
        return str(bytes) + " bytes"


def len_convert(seconds):
    return str(seconds // 60) + " min " + str(seconds % 60) + " seconds"


def confirmation_window(link, res):
    details = get_details(link, res)

    global window1
    window1 = tk.Tk()
    window1.title("Confirmation")

    frame1 = tk.Frame(master=window1, width=350, height=200)
    label1 = tk.Label(
        master=frame1,
        text="Please confirm your download",
        bg="#4ac74a",
        fg="black",
        height=2,
        width=30,
    )
    label2 = tk.Label(master=frame1, text="Name: " + details[0])
    label3 = tk.Label(master=frame1, text="Length: " + details[1])
    label4 = tk.Label(master=frame1, text="Size: " + details[2])
    button1 = tk.Button(
        master=frame1, text="Download", command=lambda: download(details[3])
    )
    button2 = tk.Button(
        master=frame1, text="Cancel", command=lambda: close_window(window1, True, True)
    )

    label1.place(x=160, y=40, anchor="center")
    label2.place(x=30, y=70)
    label3.place(x=30, y=90)
    label4.place(x=30, y=110)
    button1.place(x=100, y=150)
    button2.place(x=200, y=150)
    frame1.pack()

    window1.mainloop()


def success_window():

    window2 = tk.Tk()
    window2.title("Success")

    frame1 = tk.Frame(master=window2, width=350, height=130)
    label1 = tk.Label(
        master=frame1, text="Successful!", bg="#0ce813", fg="black", height=2, width=20
    )
    button1 = tk.Button(
        master=frame1,
        text="OK",
        width=5,
        command=lambda: close_window(window2, True, True),
    )

    label1.place(x=175, y=40, anchor="center")
    button1.place(x=175, y=100, anchor="center")
    frame1.pack()

    window2.mainloop()


def error_window(message):

    window3 = tk.Tk()
    window3.title("Error")

    frame1 = tk.Frame(master=window3, width=250, height=130)
    label1 = tk.Label(
        master=frame1, text=message, bg="#87010a", fg="white", height=2, width=30
    )
    if message == "Invalid link":
        button1 = tk.Button(
            master=frame1,
            text="OK",
            width=6,
            command=lambda: close_window(window3, True, False),
        )
    else:
        button1 = tk.Button(
            master=frame1,
            text="OK",
            width=6,
            command=lambda: close_window(window3, False, True),
        )

    label1.place(x=125, y=40, anchor="center")
    button1.place(x=125, y=90, anchor="center")
    frame1.pack()

    window3.mainloop()


def close_window(window, dlt_link, dlt_res):
    window.destroy()
    if dlt_link:
        entry1.delete(0, tk.END)
    if dlt_res:
        cmb_box.set("")


def select_stream(video, res):
    resolution = str(res)
    if resolution == "144p":
        stream = video.streams.filter(res="144p").first()
    elif resolution == "240p":
        stream = video.streams.filter(res="240p").first()
    elif resolution == "360p":
        stream = video.streams.filter(res="360p").first()
    elif resolution == "480p":
        stream = video.streams.filter(res="480p").first()
    elif resolution == "720p":
        stream = video.streams.filter(res="720p").first()
    elif resolution == "1080p":
        stream = video.streams.filter(res="1080p").first()
    return stream


def get_details(link, res):
    video = YouTube(link)
    stream = select_stream(video, res)
    v_length = len_convert(int(video.length))
    v_size = size_converter(stream.filesize)
    return [video.title, v_length, v_size, stream]


def download(stream):

    close_window(window1, True, True)
    home = str(Path.home())
    if platform == "win32":
        stream.download(home + r"/Downloads")
    elif platform == "linux" or platform == "linux2":
        stream.download(home + r"/Downloads")
    success_window()


def click_download():
    try:
        video_link = entry1.get()
        video_res = cmb_box.get()
        if video_res in option_list:
            confirmation_window(video_link, video_res)
        else:
            error_window("Please enter a valid resolution!")
    except pytube.exceptions.RegexMatchError:
        error_window("Invalid link!")
    except AttributeError:
        error_window("Resolution not available!")


window = tk.Tk()
window.title("YT Downloader")

frame1 = tk.Frame(master=window, width=500, height=150)
frame2 = tk.Frame(master=window, width=500, height=150)

label1 = tk.Label(
    master=frame1,
    text="Welcome to the YouTube Downloader",
    fg="white",
    bg="black",
    width=40,
    height=4,
)
label2 = tk.Label(
    master=frame1, text="Enter the Link:", fg="white", bg="red", width=20, height=2
)

entry1 = tk.Entry(master=frame2, width=70, bg="#bec2be")

option_list = ["144p", "240p", "360p", "480p", "720p", "1080p"]
cmb_box = ttk.Combobox(master=frame2, values=option_list, width=20)
cmb_box.set("Select resolution")

button1 = tk.Button(
    master=frame2,
    text="Download",
    fg="black",
    bg="#4ac74a",
    width=15,
    height=2,
    command=click_download,
)

label1.place(x=125, y=0)
label2.place(x=50, y=100)

entry1.place(x=50, y=0)
cmb_box.place(x=50, y=40)

button1.place(x=200, y=85)

frame1.pack()
frame2.pack()

window.mainloop()
