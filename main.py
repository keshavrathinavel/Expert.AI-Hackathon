import tkinter as tk
import tkinter.font as tkFont
from audio import *
class start:
    def __init__(self, root):
        #setting title
        root.title("Evaluation ")
        #setting window size
        width=995
        height=550
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_992=tk.Message(root)
        ft = tkFont.Font(family='Times',size=18)
        GMessage_992["font"] = ft
        GMessage_992["fg"] = "#333333"
        GMessage_992["justify"] = "center"
        GMessage_992["text"] = "Welcome to Psychology  Evaluation, please click on START button to start the process"
        GMessage_992.place(x=110,y=110,width=794,height=78)

        GButton_441=tk.Button(root)
        GButton_441["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=13)
        GButton_441["font"] = ft
        GButton_441["fg"] = "#000000"
        GButton_441["justify"] = "center"
        GButton_441["text"] = "START"
        GButton_441.place(x=440,y=220,width=114,height=46)
        GButton_441["command"] = self.GButton_441_command

    def GButton_441_command(self):
        self.GButton_441_command = tk.Toplevel(root)
        self.app = question(self.GButton_441_command)


class question:

    def __init__(self, root, question):
        #setting title
        root.title("Evaluation")
        #setting window size
        width=995
        height=700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_966=tk.Label(root)
        GLabel_966["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_966["font"] = ft
        GLabel_966["fg"] = "#333333"
        GLabel_966["justify"] = "center"
        GLabel_966["text"] = question[0]
        GLabel_966.place(x=30,y=60,width=910,height=30)

        GButton_312=tk.Button(root)
        GButton_312["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_312["font"] = ft
        GButton_312["fg"] = "#000000"
        GButton_312["justify"] = "center"
        GButton_312["text"] = "START"
        GButton_312.place(x=160,y=100,width=70,height=25)
        GButton_312["command"] = self.GButton_312_command

        GButton_221=tk.Button(root)
        GButton_221["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_221["font"] = ft
        GButton_221["fg"] = "#000000"
        GButton_221["justify"] = "center"
        GButton_221["text"] = "STOP"
        GButton_221.place(x=450,y=100,width=70,height=25)
        GButton_221["command"] = self.GButton_221_command

        GButton_214=tk.Button(root)
        GButton_214["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_214["font"] = ft
        GButton_214["fg"] = "#000000"
        GButton_214["justify"] = "center"
        GButton_214["text"] = "DELETE"
        GButton_214.place(x=720,y=100,width=70,height=25)
        GButton_214["command"] = self.GButton_214_command

        GLabel_744=tk.Label(root)
        GLabel_744["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_744["font"] = ft
        GLabel_744["fg"] = "#333333"
        GLabel_744["justify"] = "center"
        GLabel_744["text"] = "QUESTION 2"
        GLabel_744.place(x=30,y=160,width=910,height=30)

        GLabel_384=tk.Label(root)
        GLabel_384["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_384["font"] = ft
        GLabel_384["fg"] = "#333333"
        GLabel_384["justify"] = "center"
        GLabel_384["text"] = "QUESTION 3"
        GLabel_384.place(x=30,y=260,width=910,height=30)

        GLabel_903=tk.Label(root)
        GLabel_903["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_903["font"] = ft
        GLabel_903["fg"] = "#333333"
        GLabel_903["justify"] = "center"
        GLabel_903["text"] = "QUESTION 4"
        GLabel_903.place(x=30,y=360,width=910,height=30)

        GLabel_750=tk.Label(root)
        GLabel_750["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_750["font"] = ft
        GLabel_750["fg"] = "#333333"
        GLabel_750["justify"] = "center"
        GLabel_750["text"] = "QUESTION 5"
        GLabel_750.place(x=30,y=460,width=910,height=30)

        GButton_59=tk.Button(root)
        GButton_59["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_59["font"] = ft
        GButton_59["fg"] = "#000000"
        GButton_59["justify"] = "center"
        GButton_59["text"] = "START"
        GButton_59.place(x=160,y=200,width=70,height=25)
        GButton_59["command"] = self.GButton_59_command

        GButton_361=tk.Button(root)
        GButton_361["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_361["font"] = ft
        GButton_361["fg"] = "#000000"
        GButton_361["justify"] = "center"
        GButton_361["text"] = "STOP"
        GButton_361.place(x=450,y=200,width=70,height=25)
        GButton_361["command"] = self.GButton_361_command

        GButton_523=tk.Button(root)
        GButton_523["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_523["font"] = ft
        GButton_523["fg"] = "#000000"
        GButton_523["justify"] = "center"
        GButton_523["text"] = "DELETE"
        GButton_523.place(x=720,y=200,width=70,height=25)
        GButton_523["command"] = self.GButton_523_command

        GButton_720=tk.Button(root)
        GButton_720["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_720["font"] = ft
        GButton_720["fg"] = "#000000"
        GButton_720["justify"] = "center"
        GButton_720["text"] = "START"
        GButton_720.place(x=160,y=300,width=70,height=25)
        GButton_720["command"] = self.GButton_720_command

        GButton_76=tk.Button(root)
        GButton_76["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_76["font"] = ft
        GButton_76["fg"] = "#000000"
        GButton_76["justify"] = "center"
        GButton_76["text"] = "STOP"
        GButton_76.place(x=450,y=300,width=70,height=25)
        GButton_76["command"] = self.GButton_76_command

        GButton_469=tk.Button(root)
        GButton_469["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_469["font"] = ft
        GButton_469["fg"] = "#000000"
        GButton_469["justify"] = "center"
        GButton_469["text"] = "DELETE"
        GButton_469.place(x=720,y=300,width=70,height=25)
        GButton_469["command"] = self.GButton_469_command

        GButton_187=tk.Button(root)
        GButton_187["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_187["font"] = ft
        GButton_187["fg"] = "#000000"
        GButton_187["justify"] = "center"
        GButton_187["text"] = "START"
        GButton_187.place(x=160,y=400,width=70,height=25)
        GButton_187["command"] = self.GButton_187_command

        GButton_305=tk.Button(root)
        GButton_305["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_305["font"] = ft
        GButton_305["fg"] = "#000000"
        GButton_305["justify"] = "center"
        GButton_305["text"] = "STOP"
        GButton_305.place(x=450,y=400,width=70,height=25)
        GButton_305["command"] = self.GButton_305_command

        GButton_1=tk.Button(root)
        GButton_1["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_1["font"] = ft
        GButton_1["fg"] = "#000000"
        GButton_1["justify"] = "center"
        GButton_1["text"] = "DELETE"
        GButton_1.place(x=720,y=400,width=70,height=25)
        GButton_1["command"] = self.GButton_1_command

        GButton_152=tk.Button(root)
        GButton_152["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_152["font"] = ft
        GButton_152["fg"] = "#000000"
        GButton_152["justify"] = "center"
        GButton_152["text"] = "START"
        GButton_152.place(x=160,y=500,width=70,height=25)
        GButton_152["command"] = self.GButton_152_command

        GButton_254=tk.Button(root)
        GButton_254["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_254["font"] = ft
        GButton_254["fg"] = "#000000"
        GButton_254["justify"] = "center"
        GButton_254["text"] = "STOP"
        GButton_254.place(x=450,y=500,width=70,height=25)
        GButton_254["command"] = self.GButton_254_command

        GButton_838=tk.Button(root)
        GButton_838["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_838["font"] = ft
        GButton_838["fg"] = "#000000"
        GButton_838["justify"] = "center"
        GButton_838["text"] = "DELETE"
        GButton_838.place(x=720,y=500,width=70,height=25)
        GButton_838["command"] = self.GButton_838_command

        GLabel_528=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_528["font"] = ft
        GLabel_528["fg"] = "#333333"
        GLabel_528["wraplength"] = 900
        GLabel_528["justify"] = "center"
        GLabel_528["text"] = "For each of the question given below, press START button to start recording and once completed press STOP button to end recording of your answer to the question mentioned. Press DELETE button to delete recording and restart recording."
        GLabel_528.place(x=40,y=10,width=903,height=40)

        GButton_867=tk.Button(root)
        GButton_867["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        GButton_867["font"] = ft
        GButton_867["fg"] = "#000000"
        GButton_867["justify"] = "center"
        GButton_867["text"] = "CONTINUE"
        GButton_867.place(x=760,y=530,width=217,height=41)
        GButton_867["command"] = root.destroy

    def GButton_312_command(self):
        print("command")


    def GButton_221_command(self):
        print("command")


    def GButton_214_command(self):
        print("command")


    def GButton_59_command(self):
        print("command")


    def GButton_361_command(self):
        print("command")


    def GButton_523_command(self):
        print("command")


    def GButton_720_command(self):
        print("command")


    def GButton_76_command(self):
        print("command")


    def GButton_469_command(self):
        print("command")


    def GButton_187_command(self):
        print("command")


    def GButton_305_command(self):
        print("command")


    def GButton_1_command(self):
        print("command")


    def GButton_152_command(self):
        print("command")


    def GButton_254_command(self):
        print("command")


    def GButton_838_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = start(root)
    root.mainloop()
