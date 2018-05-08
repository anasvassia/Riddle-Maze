# http://docs.python-guide.org/en/latest/starting/install3/osx/
# https://pythonspot.com/en/random-numbers/
# http://goodriddlesnow.com/good-riddles
# https://www.python-course.eu/tkinter_entry_widgets.php
# https://stackoverflow.com/questions/31845482/iterating-through-a-string-word-by-word
# https://stackoverflow.com/questions/18776370/converting-a-csv-file-into-a-list-of-tuples-with-python
# https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
# https://stackoverflow.com/questions/22195141/how-to-make-the-players-image-in-front-of-another-image
# https://stackoverflow.com/questions/40443430/displaying-an-image-using-a-class-on-pygame


# A program that shows a popup of a random riddle, providing an answer box for the user to type in an answer
# After answer is entered, will be judged either correct or wrong

import csv
from random import randint
from tkinter import *


global e1, quest, answ, expl, master
master = False

def check():
    # check if user's answer was correct after "Did I get it?" button is clicked
    global e1, quest, answ, expl, master
    answer = e1.get()
    correct = "Wrong!"
    if answer.lower() in answ.lower():
        correct = "Correct!"
    response = correct + "\n" + "Answer: " + answ + "\n" + expl

    text = Text(master, height=4, width=30)
    text.insert(END, response)
    text.grid(row=1, column=1)

    Button(master, text='Choose a new riddle', command=start).grid(row=3, column=0, sticky=W, pady=4)

def start():
    global e1, quest, answ, expl, master
    if (master):
        master.destroy()
    master = Tk()
    with open('Riddles CSV.csv') as f:
        riddles = [tuple(line) for line in csv.reader(f)]


    # displays a text box with the riddle and a field for user to enter answer
    num = randint(0, len(riddles)-1)
    quest, answ, expl = riddles[num]
    Label(master, text=quest).grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0, column=1)

    Button(master, text='Did I get it?', command=check).grid(row=3, column=0, sticky=W, pady=4)

    master.mainloop()

    # runs tkinter window
if __name__ == "__main__":
     start()

