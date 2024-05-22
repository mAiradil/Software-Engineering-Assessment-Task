from tkinter import *
from PIL import ImageTk, Image

root = Tk() 
image_path = "./italy-map.jpg"
image = ImageTk.PhotoImage(Image.open(image_path))


label_image = Label( root, image= image)
label_image.pack(side = TOP)

root.mainloop()


