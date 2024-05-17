from tkinter import *

from PIL import Image,ImageTk
root = Tk()
root.title('Photo Viewer')
root.iconbitmap('apple.ico')

def quit_file():
    root.quit()

img1 = ImageTk.PhotoImage(Image.open("italy-map.jpg"))
Label - Label(root, image = img1)
Label.pack()


Button_quit = Button(root, text= "Exit Image", command = quit_file)