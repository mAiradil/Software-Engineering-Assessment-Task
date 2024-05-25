from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox, Frame, ttk
from random import shuffle
from tkinter.messagebox import showinfo
import tkinter as tk
from PIL import Image,ImageTk
#This code creates a program with buttons, labels, and images that you can interact with using your mouse.
import json
import html

THEME_COLOR = "#375362" #variable for theme colour

class Question: #class number 1
    # overriding abstract method init = initialise
    def __init__(self, question: str, correct_answer: str, choices: list,question_category : str):
        self.question_text = question
        self.correct_answer = correct_answer
        self.choices = choices
        self.question_category = question_category 
        #This code creates a question with its answer choices and category.

class QuizBrain: #class number 2

    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None
        self.current_question_category = None

    def has_more_questions(self):
        """To check if the quiz has more questions"""
        
        return self.question_no < len(self.questions)

    def next_question(self):
        """Get the next question by incrementing the question number"""
        
        self.current_question = self.questions[self.question_no]

        self.question_no += 1
        self.current_question_category =self.current_question.question_category

        q_text = self.current_question.question_text
        return f"Q.{self.question_no}: {q_text}"

    def check_answer(self, user_answer):
        """Check the user answer against the correct answer and maintain the score"""
        correct_answer = self.current_question.correct_answer

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def get_score(self):
        """Get the number of correct answers, wrong answers and score percentage."""
        
        wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        return (self.score, wrong, score_percent) 
    

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain,  general_window) -> None:
        self.quiz = quiz_brain
        general_window.destroy()
        self.window = Tk()
        self.window.title("Geography Application")
        self.window.geometry("720x850")
        self.holder_list = []
        # Display Title
        self.display_title()


        # Creating a canvas for question text, and dsiplay question
        self.canvas = Canvas(width=800, height=250)
        self.question_text = self.canvas.create_text(350, 125,
                                                     text="Question here",
                                                     width=630,
                                                     fill=THEME_COLOR,
                                                     font=(
                                                         'Ariel', 15, 'italic')
                                                     )
        self.canvas.pack()
        #self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        

        
    


        self.display_question()

        # Declare a StringVar to store user's answer
        self.user_answer = StringVar()


        q_cat = self.quiz.current_question_category  
        ############################################
        if q_cat == 'image': 
            # Display four options(radio buttons)
            self.radio_buttons_images()

        else:

            self.opts = self.radio_buttons()
            self.display_options()
        ############################################

        # To show whether the answer is correct or wrong
        self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback.place(x=250, y=510)

        # Next and Quit Button
        self.buttons()

        # Mainloop
        self.window.mainloop()


    def myimage(self, photo):
        p=Image.open(photo)
        img=ImageTk.PhotoImage(p)
        return(img)

    def display_title(self):
        """To display title"""

        # Title
        title = Label(self.window, text="iQuiz Application",
                      width=50, bg="#FFA07A", fg="white", font=("ariel", 20, "bold"))

        # place of the title
        title.place(x=0, y=2)

    def display_question(self):
        """To display the question"""
        for widget in self.holder_list:
            widget.destroy()
        q_text = self.quiz.next_question()
        q_cat = self.quiz.current_question_category  
        self.canvas.itemconfig(self.question_text, text=q_text)

    def radio_buttons_images(self):
        """To create four options (radio buttons)"""
        # position of the first option
        y_pos = 220