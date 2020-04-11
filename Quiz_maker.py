# Quiz maker reads a set of questions from a file "questions.txt" and presents them in a window. It keeps
# the score of the users in a different file called "highscores.txt" v 0.5
# 1.create the layout
#picture size 110x80
#
#
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image #for importing images
from tkinter import filedialog


def change_image():
    obrazak_do_otwarcia = filedialog.askopenfilename()


def next_question(): # It changes the number of question and saves it in a file.
    global questionnumber
    quizname_get = quiznameentry.get() #getting the quiz name
    file_with_questions = open(quizname_get+".txt", "a")
    writequestion = questionentry.get() #getting the question
    questionentry.delete(0,"end")

    answer1get = answer1entry.get() #getting the answers
    answer1entry.delete(0, "end")
    var1get = var1.get() #gettin if answer is checked or not

    answer2get = answer2entry.get()
    answer2entry.delete(0, "end")
    var2get = var2.get()

    answer3get = answer3entry.get()
    answer3entry.delete(0, "end")
    var3get = var3.get()

    answer4get = answer4entry.get()
    answer4entry.delete(0, "end")
    var4get = var4.get()

    file_with_questions.write("Question " + str(questionnumber) + " '" + writequestion + "' " + answer1get + str(var1get) + " " + answer2get +str(var2get)+ " " + answer3get +str(var3get) + " " + answer4get + str(var4get))
    file_with_questions.close()
    questionnumber += 1
    questionlabel.configure(text="Question " + str(questionnumber)+":", font=("Arial Black", 15))



#creating the window and setting up its' components
okno = Tk()
okno.title("Quiz maker 0.4")
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
nextquestionbutton = Button(okno, text="Next question", command=next_question)
nextquestionbutton.grid(column=2,row=1)

previousquestionbutton = Button(okno, text="Previous question")
previousquestionbutton.grid(column=2, row=0)
############################################################################

#answer widget
var1=IntVar()
checkbox1 = Checkbutton(okno, text="Answer 1", variable=var1)
checkbox1.grid(column=0,row=2,  pady=10)
answer1entry = Entry(okno, width=40)
answer1entry.grid(column=1,row=2, sticky=W)

var2=IntVar()
checkbox2 = Checkbutton(okno, text="Answer 2", variable=var2)
checkbox2.grid(column=0,row=3,  pady=10)
answer2entry = Entry(okno, width=40)
answer2entry.grid(column=1,row=3, sticky=W)

var3=IntVar()
checkbox3 = Checkbutton(okno, text="Answer 3", variable=var3)
checkbox3.grid(column=0,row=4,  pady=10)
answer3entry = Entry(okno, width=40)
answer3entry.grid(column=1,row=4, sticky=W)

var4=IntVar()
checkbox4 = Checkbutton(okno, text="Answer 4", variable=var4)
checkbox4.grid(column=0,row=5,  pady=10)
answer4entry = Entry(okno, width=40)
answer4entry.grid(column=1,row=5, sticky=W)
#############################################################################
#adding image button
path="mozg.png"
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(okno, image=img)
panel.grid(column=2, row=2, rowspan=3, sticky=W, padx=1)

change_image = Button(okno, text="Change image", command=change_image)
change_image.grid(column=2, row=5)
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
