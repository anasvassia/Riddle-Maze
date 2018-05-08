# A program that shows a popup of a random riddle, providing an answer box for the user to type in an answer
# After answer is entered, will be judged either correct or wrong

# http://docs.python-guide.org/en/latest/starting/install3/osx/
# https://pythonspot.com/en/random-numbers/
# http://goodriddlesnow.com/good-riddles
# https://www.python-course.eu/tkinter_entry_widgets.php
# https://stackoverflow.com/questions/31845482/iterating-through-a-string-word-by-word
# https://stackoverflow.com/questions/18776370/converting-a-csv-file-into-a-list-of-tuples-with-python
# https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
# https://stackoverflow.com/questions/22195141/how-to-make-the-players-image-in-front-of-another-image
# https://stackoverflow.com/questions/40443430/displaying-an-image-using-a-class-on-pygame

import csv
import pygame
from random import randint
from tkinter import *


global e1, quest, answ, expl, master
master = False

class Riddle:

    def __init__(self, color, width, height, x, y):
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        self.image = pygame.Surface([width, height])

        self.color = color

        # load image of sprite
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()


        self.rect.x = x
        self.rect.y = y
        self.cor = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def resize(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))

    def check(self):
        # check if user's answer was correct after button is clicked
        global e1, quest, answ, expl, master
        answer = e1.get()
        correct = "Wrong!"
        if answer.lower() in answ.lower():
            correct = "Correct!"
            self.cor = True
        response = correct + "\n" + "Answer: " + answ + "\n" + expl

        text = Text(master, height=4, width=30)
        text.insert(END, response)
        text.grid(row=1, column=1)

        Button(master, text='Choose a new riddle', command=self.start).grid(row=3, column=0, sticky=W, pady=4)

    def start(self):
        global e1, quest, answ, expl, master
        if (master):
            master.destroy()
        master = Tk()
        with open('Riddles CSV.csv') as f:
            riddles = [tuple(line) for line in csv.reader(f)]


        # displays a text box with the riddle and a field for user to enter answer
        # once user enters and answer
        # displays whether riddle was correct or not along with an explanation of the answer to the riddle
        num = randint(0, len(riddles)-1)
        quest, answ, expl = riddles[num]
        Label(master, text=quest).grid(row=0)
        e1 = Entry(master)
        e1.grid(row=0, column=1)

        Button(master, text='Did I get it?', command=self.check).grid(row=3, column=0, sticky=W, pady=4)

        # runs tkinter window
        master.mainloop()
