import tkinter as tk
from PIL import Image, ImageTk

# Function to display an image in Tkinter with specified size
def show_image(image_path, width, height):
    root = tk.Tk()
    root.title("Image Display")

    # Open and resize the image
    img = Image.open(image_path)
    img = img.resize((width, height), Image)
    tk_img = ImageTk.PhotoImage(img)

    # Create and pack the label with the image
    label = tk.Label(root, image=tk_img)
    label.image = tk_img  # Keep a reference to avoid garbage collection
    label.pack()

    root.mainloop()

# Example usage
show_image("india-map.jpg", 200,200)