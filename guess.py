from tkinter import *
import random

actors = ["NICK NOLTE", "MEL GIBSON", "PATRICK STEWART", "CHRISTIAN BALE", "ARNOLD SCHWARZENEGGER",
      "MATTHEW MCCONAUGHEY", "MERYL STREEP", "JOHNNY DEPP", "ANGELINA JOLIE", "CAMERON DIAZ", "AL PACINO",
      "ANDY GARCIA", "JULIA ROBERTS"]

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
       "W", "X", "Y", "Z"]

class MyButtons:
    def __init__(self, master):
        buttonsFrame = Frame(master)
        buttonsFrame.grid(row=0)

        x = 0
        y = 0
        for i in letters:
            #button = Button(buttonsFrame, text=i, width=5, command=self.onclick(i))
            button = Button(buttonsFrame, text=i, width=5, command=lambda k=i: self.onclick(k))
            button.grid(row=x, column=y)
            y += 1
            if y > 3:
                y = 0
                x += 1

    def onclick(self, k):
        def click():
            print (k)
        return click

actor = random.choice(actors)

root = Tk()

guessFrame = Frame(root)
guessFrame.grid(row=1)

buton = MyButtons(root)

def underscores():
    total = ""
    for i in actor:
        if i == " ":
            i = "     "
            total += i
        else:
            i = "_"
            total += i
    return total

label = Label(guessFrame, text=underscores())
label.grid(row=0)

root.mainloop()
