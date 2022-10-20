from tkinter import *
import os
import requests
import speech
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Feedback Sentiment Analysis")

        self.label = Label(master, text="Enter your feedback!")
        self.label.pack()

        self.greet_button = Button(master, text="Go", command=self.greet)
        self.greet_button.pack()

    def greet(self):
        print("Greetings!")
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()