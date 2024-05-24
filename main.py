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
