# Quiz maker reads a set of questions from a file "questions.txt" and presents them in a window. It keeps
# the score of the users in a different file called "highscores.txt"
# 1.create the layout
#picture size 110x80
#
#
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image #for importing images


#creating the window and setting up its' components
okno = Tk()
okno.title("Quiz maker 0.2")
okno.geometry("550x280")
okno.resizable(0,0) #user can't change the size of the window

# creating quiz name label and form
quiznamelabel = Label(okno, text="Quiz name", font=("Arial Black", 15))
quiznamelabel.grid(column=0, row=0, sticky=W)

quiznameentry = Entry(okno, width=40)
quiznameentry.grid(column=1, row=0, sticky=W)
############################################################################

#creating question label and form
questionnumber=1
questionlabel = Label(okno, text="Question "+ str(questionnumber)+":", font=("Arial Black", 15))
questionlabel.grid(column=0,row=1, sticky=W)

questionentry = Entry(okno, width=40)
questionentry.grid(column=1, row=1, sticky=W)
############################################################################

#creating buttons for next question and previos question
nextquestionbutton = Button(okno, text="Next question")
nextquestionbutton.grid(column=2,row=1)

previousquestionbutton = Button(okno, text="Previous question")
previousquestionbutton.grid(column=2, row=0)
############################################################################

#answer widget
var1=IntVar
checkbox1 = Checkbutton(okno, text="Answer 1", variable=var1)
checkbox1.grid(column=0,row=2,  pady=10)
answer1entry = Entry(okno, width=40)
answer1entry.grid(column=1,row=2, sticky=W)

var2=IntVar
checkbox2 = Checkbutton(okno, text="Answer 2", variable=var2)
checkbox2.grid(column=0,row=3,  pady=10)
answer2entry = Entry(okno, width=40)
answer2entry.grid(column=1,row=3, sticky=W)

var3=IntVar
checkbox3 = Checkbutton(okno, text="Answer 3", variable=var2)
checkbox3.grid(column=0,row=4,  pady=10)
answer3entry = Entry(okno, width=40)
answer3entry.grid(column=1,row=4, sticky=W)

var4=IntVar
checkbox4 = Checkbutton(okno, text="Answer 4", variable=var2)
checkbox4.grid(column=0,row=5,  pady=10)
answer4entry = Entry(okno, width=40)
answer4entry.grid(column=1,row=5, sticky=W)
#############################################################################
#adding image
path="mozg.png"
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(okno, image=img)
panel.grid(column=2, row=2, rowspan=3, sticky=E, padx=10)

change_image = Button(okno, text="Change image")
change_image.grid(column=2,row=5)
#creating the window


# creating the menu
menubar = Menu(okno)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New quiz")
filemenu.add_command(label="Quit", command=okno.quit)
menubar.add_cascade(label="File", menu=filemenu)
okno.config(menu=menubar)
#creating the menu




okno.mainloop()
