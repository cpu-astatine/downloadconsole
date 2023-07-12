import tkinter as tk
import os
import subprocess

os.system("clear")

pencere = tk.Tk()
pencere.title("Download Console")
pencere.geometry("400x240")

def download():
    urltext = url.get("1.0", "end-1c")
    subprocess.run(['wget', f'{urltext}'])
    print("Transmission complete!")

def githubDownload():
    urltext = url.get("1.0", "end-1c")
    subprocess.run(['git', 'clone', f'{urltext}'])
    print("Transmission complete!")

def cikis():
    pencere.quit()

title = tk.Label(pencere, text="Download Console")
title.pack()

url = tk.Text(pencere, height=1, width=40)
url.pack()

downloadButton = tk.Button(pencere, text="WGet to Download", command=download)
downloadButton.pack()

downloadButton2 = tk.Button(pencere, text="GitHub to Download", command=githubDownload)
downloadButton2.pack()

exitButton = tk.Button(pencere, text="Exit", command=cikis)
exitButton.pack()

pencere.mainloop()