#!/usr/bin/python

import Tkinter,time
from threading import Timer



class myTimer(Tkinter.Tk):
    """docstring for myTimer.Tkinter.tk"""

    def __init__(self, parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def change(self):
        self.title("klicked")
        #self.Label(text=u'changed')

    def initialize(self):
        #initialization de grid
        #self.grid(3,3,widthInc=400,heightInc=400)
        self.grid()
        # initialization de widjet "champ de text"
        self.myEntry = Tkinter.Entry(self)
        self.myEntry.grid(column=0,row=0,sticky='ew')#ipady=10,pady=20
        self.myEntry.bind("<Return>", self.OnPressEnter)
        # nom de la fenetre
        self.title('MyTimerInInit')

        #ajout de bouton qui execute change()
        buttonKleek = Tkinter.Button(self,text = u'kleek mee !',command=self.OnButtonClick)#lambda: self.change())
        buttonKleek.grid(row=0,column=1)

        self.labelVarStr = Tkinter.StringVar()
        self.labelVarStr.set("btn dnt clk")

        # ajout de label
        TimerLabel =  Tkinter.Label(self,textvariable=self.labelVarStr,anchor="w",fg="white",bg="blue")
        TimerLabel.grid(column=0,row=1,columnspan=2,sticky='EW')

        # ajout de resize window
        self.grid_columnconfigure(0,weight=1)

        self.resizable(True,True)






    def OnButtonClick(self):
        print "button clicked"
        #self.labelVarStr.set("btn clk")
        self.labelVarStr.set(self.myEntry.get())

    def OnPressEnter(self,event):
        print "enter pressed"
        self.title('Title is changed')


if __name__ == '__main__':
    app = myTimer(None)
#    app.title('MyTimer')
    #Timer(None,app.mainloop).start()
    app.after(10000, lambda:app.destroy()) # quit applilcation apres 5sec
    app.mainloop()
