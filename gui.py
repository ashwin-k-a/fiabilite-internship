from tkinter import*
import tkinter.filedialog as f
from PIL import ImageTk,Image

from PyQt5.QtCore import QProcess
import sys
import subprocess
from pathlib import Path
root = Tk()


root.title('GUI')
#You can set the geometry attribute to change the root windows size
root.geometry("500x500") #You want the size of the app to be 500x500
root.resizable(10000, 10000)
root.configure(background='cyan')


background_image=PhotoImage(file="bgrnd.png")
background_label=Label(root, image = background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


w=Label(root, fg = "dark blue", bg = "black", font = "Times 24 bold", text="Welcome to Fiablite Projects!")

w.pack()



def openPattern():
    fileName = f.askopenfilename()
    print(fileName)

    
    aa = fileName.replace("/", "\\\\")
    print(aa)
    

    a=open(aa, "r")
    contents=a.read()
    exec(contents)



b=Button(root,height=2,  font = "Times 14 bold", text="Open Projects",bg="yellow",fg="red", command=openPattern,
         highlightbackground='green')
b.place(x=625,y=500)
root.mainloop()
