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

        self.option=self.myimage(self.quiz.current_question.choices[0])
        self.radio_btn11=tk.Radiobutton(self.window,  variable=self.user_answer ,value=self.quiz.current_question.choices[0] ,image=self.option )
        self.radio_btn11.place(x=200, y=y_pos)
        self.holder_list.append(self.radio_btn11)
        y_pos += 70
        self.option1=self.myimage(self.quiz.current_question.choices[1])
        self.radio_btn1=tk.Radiobutton(self.window,  variable=self.user_answer ,value=self.quiz.current_question.choices[1] ,image=self.option1 )
        self.radio_btn1.place(x=200, y=y_pos)
        y_pos += 70
        self.holder_list.append(self.radio_btn1)
        self.option2=self.myimage(self.quiz.current_question.choices[2])
        self.radio_btn2=tk.Radiobutton(self.window,  variable=self.user_answer ,value=self.quiz.current_question.choices[2] ,image=self.option2 )
        self.radio_btn2.place(x=200, y=y_pos)
        y_pos += 70
        self.holder_list.append(self.radio_btn2)
        self.option3=self.myimage(self.quiz.current_question.choices[3])
        self.radio_btn3=tk.Radiobutton(self.window,  variable=self.user_answer ,value=self.quiz.current_question.choices[3] ,image=self.option3 )
        self.radio_btn3.place(x=200, y=y_pos)
        self.holder_list.append(self.radio_btn3)


    def radio_buttons(self):
        """To create four options (radio buttons)"""

        # initialize the list with an empty list of options
        choice_list = []

        # position of the first option
        y_pos = 220

        # adding the options to the list
        while len(choice_list) < 4:

            # setting the radio button properties
            self.radio_btn = Radiobutton(self.window, text="", variable=self.user_answer,
                                    value='', font=("ariel", 14))

            # adding the button to the list
            choice_list.append(self.radio_btn)
            self.holder_list.append(self.radio_btn)
            # placing the button
            self.radio_btn.place(x=200, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return choice_list

    def display_options(self):
        """To display four options"""

        val = 0

        # deselecting the options
        self.user_answer.set(None)

        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in self.quiz.current_question.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    def next_btn(self):
        """To show feedback for each answer and keep checking for more questions"""

        try:
            self.label_image.destroy()
        except:
            print(" ")


        quest_cat = self.quiz.current_question_category 
         

        # Check if the answer is correct
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "#FFA07A"
            self.feedback["text"] = 'Correct answer! \U0001F44D'
        else:
            if quest_cat == 'image':
                 
        
              
                self.feedback['fg'] = 'lightblue'
                self.feedback['text'] = ('\u274E Oops! \n'
                                         f'The right answer is:  ')
                 
                """
                photo = ImageTk.PhotoImage(Image.open(self.quiz.current_question.correct_answer)) 
                 
                self.label_image = Label(image=photo)
                self.label_image.image = photo # keep a reference!
                self.label_image.pack()
                """
                photo = ImageTk.PhotoImage(Image.open(self.quiz.current_question.correct_answer)) 
                 
                self.label_image = Label(image=photo ,bg="purple")
                self.label_image.image = photo # keep a reference

                self.label_image.pack(padx=250, pady=1, side=tk.RIGHT  )



            else:    
                self.feedback['fg'] = 'lightblue'
                self.feedback['text'] = ('\u274E Oops! \n'
                                         f'The right answer is: {self.quiz.current_question.correct_answer}')


        if self.quiz.has_more_questions():
            # Moves to next to display next question and its options
            self.display_question()
            q_cat = self.quiz.current_question_category 
    
            ############################################
            if q_cat == 'image': 
                # Display four options(radio buttons)
                self.radio_buttons_images()

            else:
                self.opts = self.radio_buttons()
                self.display_options()

        else:
            # if no more questions, then it displays the score
            self.display_result()
            # destroys the self.window
            #self.window.destroy()
            #MainInterface()
            
    def quit_btn(self):

        self.window.destroy()
        MainInterface()


    def buttons(self):
        """To show next button and quit button"""

        # The first button is the Next button to move to the
        # next Question
        self.next_button = Button(self.window, text=" Next ", command=self.next_btn,
                             width=10, bg="#FFA07A", fg="black", font=("ariel", 16, "bold"))

        # palcing the button  on the screen
        self.next_button.place(x=330, y=590)

        # This is the second button which is used to Quit the self.window
        quit_button = Button(self.window, text="Quit", command=self.quit_btn,
                             width=5, bg="lightblue", fg="black", font=("ariel", 16, " bold"))

         

        # placing the Quit button on the screen
        quit_button.place(x=615, y=50)

    def display_result(self):
        """To display the result using messagebox"""
        correct, wrong, score_percent = self.quiz.get_score()

        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"

        # calculates the percentage of correct answers
        result = f"Score: {score_percent}%"

        #destroy all elements
        self.next_button.destroy()
        self.feedback.destroy()
        
        for widget in self.holder_list:
            widget.destroy()
  
        self.feedback1 = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback1.place(x=300, y=380)

        self.feedback1['fg'] = '#FFA07A'
        self.feedback1['text'] = ( f'{result}\n{correct}\n{wrong}')

        self.canvas.itemconfig(self.question_text, text=' ')

#################################################################################################################
#################################################################################################################
class MainInterface:
    def __init__(self):
        #self.quiz = quiz_brain
        self.window_main = tk.Tk()
        self.window_main.title("Geography Introduction")
        self.window_main.geometry("850x850")
        self.window_main.configure(bg="#ADD8E6")

        # Display Title
        self.display_title()


        # Mainloop
        self.window_main.mainloop()
 
    def disable_event(self):
       pass

    def display_title(self):
        #self.window_main.protocol("WM_DELETE_WINDOW", self.disable_event)
        #self.window_main.resizable(0,0) 
        #self.window_main.overrideredirect(True)
        intro_label = Label(self.window_main, text="Welcome to Geography!", font=("Helvetica", 24), bg="#ADD8E6")
        intro_label.pack(pady=20)

        intro_text = Label(self.window_main, text="Explore the world with us.", font=("Helvetica", 14), bg="#ADD8E6")
        intro_text.pack(pady=10)

        #general_button = Button(self.window_main, text="General Knowledge", command=self.open_general, bg="#FFA07A", fg="black", font=("Helvetica", 12))
        general_button = Button(self.window_main, text="General Knowledge", command=self.open_general, bg="#FFA07A", fg="black", font=("Helvetica", 12))
        general_button.pack(pady=10)

        countries_button = Button(self.window_main, text="Countries", command=self.open_countries, bg="#FFA07A", fg="black", font=("Helvetica", 12))
        countries_button.pack(pady=10)


        close_button = Button(self.window_main, text="Close", command=self.window_main.destroy, bg="#FFA07A", fg="black", font=("Helvetica", 12))
        close_button.pack(pady=20)

        
        #p=Image.open("countryflags/austria.png")
        #img=ImageTk.PhotoImage(p)

        #image = ImageTk.PhotoImage(Image.open(r'austria.png')) 

        #Label(self.window_main,  image=image, compound='center').grid(row=2, column=2, columnspan=2, pady=50)
        #self.window_main.mainloop()

        # Display it within a label.
        #label12222 = Label(self.window_main,  image=img, compound="center"  )
        #label12222.pack(pady=50)
         #.grid(row=2, column=2, columnspan=2, pady=50)



    def start_quiz_knowledge(self, general_window):
        question_json = open('question_knowledge.json')
        response = json.load(question_json)
        question_data = response["results"]
        question_bank = []
        for question in question_data:
            choices = []
            question_category = question["category"]
            question_text = question["question"]
            correct_answer = question["correct_answer"]
            incorrect_answers = question["incorrect_answers"]
            for ans in incorrect_answers:
                choices.append(ans)
            choices.append(correct_answer)
            shuffle(choices)
            new_question = Question(question_text, correct_answer, choices, question_category)
            question_bank.append(new_question)


        self.quiz = QuizBrain(question_bank)
        try:
            self.window_main.destroy()
        except:
            print("An exception occurred")

        QuizInterface(self.quiz,  general_window)
   
    def start_quiz_countries(self, country_window):
        question_json = open('question_countries.json')
        response = json.load(question_json)
        question_data = response["results"]
        question_bank = []
        for question in question_data:
            choices = []
            question_category = question["category"]
            question_text = html.unescape(question["question"])
            correct_answer = html.unescape(question["correct_answer"])
            incorrect_answers = question["incorrect_answers"]
            category = question["category"]
            for ans in incorrect_answers:
                choices.append(html.unescape(ans))
            choices.append(correct_answer)
            shuffle(choices)
            new_question = Question(question_text, correct_answer, choices, question_category)
            question_bank.append(new_question)


        self.quiz = QuizBrain(question_bank)
        try:
            self.window_main.destroy()
        except:
            print("An exception occurred")

        QuizInterface(self.quiz,  country_window)      
 
    def open_countries(self):
        self.countrywindow = Tk()
        self.countrywindow.title("Countries")
        self.countrywindow.geometry("800x800")
        countries_label = Label(self.countrywindow,  text="Welcome to the Countries page!", font=("Helvetica", 16))
        
        countries_label.pack(pady=20)

        countries_text = Label(self.countrywindow,width=80, text="Here you can learn about different countries.   Lorem Ipsum is simply dummy\n text of the printing and typesetting industry. Lorem Ipsum has been the \n industry standard dummy text ever since the 1500s, when an unknown \n printer took a galley of type and scrambled it to make a type specimen\n  book. It has survived not only five centuries, but also the leap into\n   electronic typesetting, remaining essentially unchanged. It was \n   popularised in the 1960s with the release of Letraset sheets containing\n    Lorem Ipsum passages, and more recently with desktop publishing \n software like Aldus PageMaker including versions of Lorem Ipsum.\n")
        
        countries_text.pack(pady=10)
         



        start_quiz_button_country = Button(self.countrywindow, text="Start Quiz", command=lambda: self.start_quiz_countries(  self.countrywindow), bg="#FFA07A", fg="black", font=("Helvetica", 12))
        start_quiz_button_country.pack(pady=20)

        close_button_country = Button(self.countrywindow, text="Close Screen", command=self.countrywindow.destroy, bg="#FFA07A", fg="black", font=("Helvetica", 12))
        close_button_country.pack(pady=20)
        
        self.countrywindow.mainloop()


    def open_general(self):
        self.general_window = Tk()
        self.general_window.title("General Knowledge")
        self.general_window.geometry("800x800")
        general_label = Label(self.general_window, text="Welcome to the General Knowledge page!", font=("Helvetica", 16))
        general_label.pack(pady=20)
        #general_text = Label(self.general_window, text="Here we are going to test your General Knowledge Skills.")
        general_text = Label(self.general_window,width=80, text="ere we are going to test your General Knowledge Skills   Lorem Ipsum is simply dummy\n text of the printing and typesetting industry. Lorem Ipsum has been the \n industry standard dummy text ever since the 1500s, when an unknown \n printer took a galley of type and scrambled it to make a type specimen\n  book. It has survived not only five centuries, but also the leap into\n   electronic typesetting, remaining essentially unchanged. It was \n   popularised in the 1960s with the release of Letraset sheets containing\n    Lorem Ipsum passages, and more recently with desktop publishing \n software like Aldus PageMaker including versions of Lorem Ipsum.\n")
        

        general_text.pack(pady=10)
 
        start_quiz_button = Button(self.general_window, text="Start Quiz", command=lambda: self.start_quiz_knowledge(  self.general_window), bg="#FFA07A", fg="black", font=("Helvetica", 12))
        start_quiz_button.pack(pady=20)

        close_button = Button(self.general_window, text="Close Screen", command=self.general_window.destroy, bg="#FFA07A", fg="black", font=("Helvetica", 12))
        close_button.pack(pady=20)
        
        self.general_window.mainloop()



 
main_ui  = MainInterface()