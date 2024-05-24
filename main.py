from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox, Frame, ttk
from random import shuffle
from tkinter.messagebox import showinfo
import tkinter as tk
from PIL import Image,ImageTk
#This code creates a program with buttons, labels, and images that you can interact with using your mouse.
import json
import html

THEME_COLOR = "#375362"



def open_general():
    general_window = tk.Toplevel(root)
    general_window.title("General Knowledge")
    general_window.geometry("700x700")
    general_label = tk.Label(general_window, text="Welcome to the General Knowledge page!", font=("Helvetica", 17))
    general_label.pack(pady=20)
    general_text = tk.Label(general_window, text="Read the passage below to help you answer the following questions", font=("Helvetica", 14))
    general_text.pack(pady=10)
    general_text = tk.Label(general_window, text=("Geography is all about exploring our world. It looks at the land, weather, and living things,\n as well as how people live on Earth. \n There are two main parts to geography: Physical and Human."))
    general_text.pack(pady=0, padx=0)
    general_button = tk.Button(general_window, text="Open", command=general_window_quiz, bg="#FFA07A", fg="white", font=("Helvetica", 12), justify="left")
    general_button.pack(pady=20)

def general_window_quiz():
    general_window = tk.Toplevel(root)
    general_window.title("Quiz Knowledge")
    general_window.geometry("700x700")
    general_label = tk.Label(general_window, text="QUIZ", font=("Helvetica", 16))
    general_label.pack(pady=20)
    general_text = tk.Label(general_window, text="Quiz")
    general_text.pack(pady=10)
    general_button = tk.Button(general_window, text="Next", command=general_window_quiz, bg="#FFA07A", fg="white", font=("Helvetica", 12))
    general_button.pack(pady=20)

def open_countries():
    countries_window = tk.Toplevel(root)
    countries_window.title("Countries")
    countries_window.geometry("700x700")
    countries_label = tk.Label(countries_window, text="Welcome to the Countries page!", font=("Helvetica", 16))
    countries_label.pack(pady=20)
    countries_text = tk.Label(countries_window, text="Here you can learn about different countries.")
    countries_text.pack(pady=10)
    countries_button = tk.Button(countries_window, text="Close", command=open_countries_quiz, bg="#FFA07A", fg="white", font=("Helvetica", 12))
    countries_button.pack(pady=20)

def open_countries_quiz():
    countries_window = tk.Toplevel(root)
    countries_window.title("Countries")
    countries_window.geometry("700x700")
    countries_label = tk.Label(countries_window, text="Welcome to the Countries page!", font=("Helvetica", 16))
    countries_label.pack(pady=20)
    countries_text = tk.Label(countries_window, text="Here you can learn about different countries.")
    countries_text.pack(pady=10)
    countries_button = tk.Button(countries_window, text="Close", command=countries_window.destroy, bg="#FFA07A", fg="white", font=("Helvetica", 12))
    countries_button.pack(pady=20)



root = tk.Tk()
root.title("Geography Introduction")
root.geometry("700x700")
root.configure(bg="#ADD8E6")

intro_label = tk.Label(root, text="Welcome to Geography!", font=("Helvetica", 24), bg="#ADD8E6")
intro_label.pack(pady=20)

intro_text = tk.Label(root, text="Explore the world with us.", font=("Helvetica", 14), bg="#ADD8E6")
intro_text.pack(pady=10)

general_button = tk.Button(root, text="General Knowledge", command=open_general, bg="#FFA07A", fg="white", font=("Helvetica", 12))
general_button.pack(pady=10)

countries_button = tk.Button(root, text="Countries", command=open_countries, bg="#FFA07A", fg="white", font=("Helvetica", 12))
countries_button.pack(pady=10)























root.mainloop()
