# Import Module
from tkinter import *
from PIL import Image, ImageTk

# Create Tkinter Object
root = Tk()

# Read the Image
image = Image.open("./italy-map.jpg")

# Resize the image using resize() method
resize_image = image.resize(("width=500, height=200"))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()

# Execute Tkinter
root.mainloop()
