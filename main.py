import tkinter as tk
import tkinter.font as tkFont
from audio1 import main
import analysis
import speech
import speech_recognition as sr
import sounddevice as sd
from tkinter import *
import pandas as pd
from tkinter import messagebox
class start:
    def __init__(self, root):
        #setting title
        root.title("START")
        #setting window size
        width=1050
        height=550
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_992=tk.Message(root)
        ft = tkFont.Font(family='Helvetica',size=18)
        GMessage_992["font"] = ft
        GMessage_992["fg"] = "#333333"
        GMessage_992["justify"] = "center"
        GMessage_992["text"] = "Click START to begin your Psych Evaluation"
        GMessage_992.place(x=110,y=50,width=850,height=200)

        GButton_441=tk.Button(root)
        GButton_441["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Helvetica',size=13)
        GButton_441["font"] = ft
        GButton_441["fg"] = "#000000"
        GButton_441["justify"] = "center"
        GButton_441["text"] = "START"
        GButton_441.place(x=480,y=220,width=114,height=46)
        GButton_441["command"] = self.GButton_441_command

        entry = tk.Entry(root)
        entry["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Helvetica',size=13)
        entry["font"] = ft
        entry["fg"] = "#000000"
        entry["justify"] = "center"
        entry["text"] = "Enter the recipient email address"
        entry.place(x=480,y=250,width=114,height=46)
        self.email = entry.get()

    def send_mail(self,isTls=True):
        import smtplib,ssl
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email.mime.text import MIMEText
        from email.utils import formatdate
        from email import encoders
        send_from = "wall.e.autoresponse@gmail.com"
        send_to = str(self.email)
        msg = MIMEMultipart()
        username='wall.e.autoresponse@gmail.com'
        password='ggD7BaBV:zA2_6.'
        msg['From'] = send_from
        msg['To'] = send_to
        msg['Date'] = formatdate(localtime = True)
        text = 'Attached patient evaluation in questions.csv file'
        msg['Subject'] = 'User ' + 'Evaluation on:' + str(formatdate(localtime = True))
        msg.attach(MIMEText(text))
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open("questions.csv", "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="questions.csv"')
        msg.attach(part)
        # context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
        #SSL connection only working on Python 3+
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        if isTls:
            smtp.starttls()
        smtp.login(username,password)
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.quit()

    def GButton_441_command(self):
        data = pd.read_csv("D:\Amrita\AM@hack\Expert.AI-Hackathon\questions.csv")
        self.GButton_441_command = tk.Toplevel(root)
        self.app = question(self.GButton_441_command, data)


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
        GLabel_966["text"] = question.iloc[0,0]
        GLabel_966.place(x=30,y=60,width=910,height=30)

        GButton_312=tk.Button(root)
        GButton_312["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Helvetica',size=10)
        GButton_312["font"] = ft
        GButton_312["fg"] = "#000000"
        GButton_312["justify"] = "center"
        GButton_312["text"] = "START"
        GButton_312.place(x=160,y=100,width=70,height=25)
        GButton_312["command"] = self.GButton_312_command


        GLabel_744=tk.Label(root)
        GLabel_744["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_744["font"] = ft
        GLabel_744["fg"] = "#333333"
        GLabel_744["justify"] = "center"
        GLabel_744["text"] = question.iloc[1,0]
        GLabel_744.place(x=30,y=160,width=910,height=30)

        GLabel_384=tk.Label(root)
        GLabel_384["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_384["font"] = ft
        GLabel_384["fg"] = "#333333"
        GLabel_384["justify"] = "center"
        GLabel_384["text"] = question.iloc[2,0]
        GLabel_384.place(x=30,y=260,width=910,height=30)

        GLabel_903=tk.Label(root)
        GLabel_903["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_903["font"] = ft
        GLabel_903["fg"] = "#333333"
        GLabel_903["justify"] = "center"
        GLabel_903["text"] = question.iloc[3,0]
        GLabel_903.place(x=30,y=360,width=910,height=30)

        GLabel_750=tk.Label(root)
        GLabel_750["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_750["font"] = ft
        GLabel_750["fg"] = "#333333"
        GLabel_750["justify"] = "center"
        GLabel_750["text"] = question.iloc[4,0]
        GLabel_750.place(x=30,y=460,width=910,height=30)

        GButton_59=tk.Button(root)
        GButton_59["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Helvetica',size=10)
        GButton_59["font"] = ft
        GButton_59["fg"] = "#000000"
        GButton_59["justify"] = "center"
        GButton_59["text"] = "START2"
        GButton_59.place(x=160,y=200,width=70,height=25)
        GButton_59["command"] = self.GButton_59_command


        GButton_720=tk.Button(root)
        GButton_720["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Helvetica',size=10)
        GButton_720["font"] = ft
        GButton_720["fg"] = "#000000"
        GButton_720["justify"] = "center"
        GButton_720["text"] = "START3"
        GButton_720.place(x=160,y=300,width=70,height=25)
        GButton_720["command"] = self.GButton_720_command

        GButton_187=tk.Button(root)
        GButton_187["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Helvetica',size=10)
        GButton_187["font"] = ft
        GButton_187["fg"] = "#000000"
        GButton_187["justify"] = "center"
        GButton_187["text"] = "START4"
        GButton_187.place(x=160,y=400,width=70,height=25)
        GButton_187["command"] = self.GButton_187_command

        GButton_152=tk.Button(root)
        GButton_152["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Helvetica',size=10)
        GButton_152["font"] = ft
        GButton_152["fg"] = "#000000"
        GButton_152["justify"] = "center"
        GButton_152["text"] = "START5"
        GButton_152.place(x=160,y=500,width=70,height=25)
        GButton_152["command"] = self.GButton_152_command

        GLabel_528=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=13)
        GLabel_528["font"] = ft
        GLabel_528["fg"] = "#333333"
        GLabel_528["wraplength"] = 900
        GLabel_528["justify"] = "center"
        GLabel_528["text"] = "For each of the question given below, press START button to start recording and once completed press STOP button to end recording of your answer to the question mentioned. Press DELETE button to delete recording and restart recording."
        GLabel_528.place(x=40,y=10,width=903,height=40)

        GButton_867=tk.Button(root)
        GButton_867["bg"] = "#5fb878"
        ft = tkFont.Font(family='Helvetica',size=10)
        GButton_867["font"] = ft
        GButton_867["fg"] = "#000000"
        GButton_867["justify"] = "center"
        GButton_867["text"] = "CONTINUE"
        GButton_867.place(x=760,y=530,width=217,height=41)
        GButton_867["command"] = root.destroy

    def GButton_312_command(self):
        x = 'Q1.wav'
        main(x)
        print("command")

    def GButton_59_command(self):
        x = 'Q2.wav'
        main(x)
        print("command")


    def GButton_720_command(self):
        x = 'Q3.wav'
        main(x)
        print("command")


    def GButton_187_command(self):
        x = 'Q4.wav'
        main(x)
        print("command")


    def GButton_152_command(self):
        x = 'Q5.wav'
        main(x)
        print("command")



if __name__ == "__main__":
    root = tk.Tk()
    app = start(root)
    root.mainloop()
    data = pd.read_csv('D:\Amrita\AM@hack\Expert.AI-Hackathon\questions.csv')
    for i in range(1,5):
        name = 'Q'
        x = name + str(i) + '.wav'
        text = speech.speech_using_audio_file(x)
        text = text.replace(',', '')
        # text = "i want to murder children and cut up cats"
        data.iloc[i-1,1] = text
        behavious_output = analysis.behavioural_analysis(text)
        print("Tab separated list of categories:")
        for category in behavious_output.categories:
            print(category.id_, category.hierarchy, sep="\t")
            behaviour = str(data.iloc[i-1,5]) + "---" + str(category.id_) +":"+ str(category.hierarchy)
            data.iloc[i-1,5] = behaviour
        # hate speech analysis
        hate_speech_analysis = analysis.hatespeechdetection(text)
        print("\nCategorization: ID Code + Category")
        for category in hate_speech_analysis.categories:
            print(category.id_, category.hierarchy, sep="\t")
            hate_id = str(data.iloc[i-1,6])+ "---" + str(category.id_) +":"+ str(category.hierarchy)
            data.iloc[i-1,6] = hate_id

        print("\nRunning Hate-Speech Detection: ")
        j = 1
        for extraction in hate_speech_analysis.extractions:
            print("Record #{}:".format(j))
            for field in extraction.fields:
                print("{} = {}".format(field.name, field.value))
                hate_detect = str(data.iloc[i-1,7])+ "---" + str(field.name) +':'+ str(field.value)
                data.iloc[i-1,7] = hate_detect
            j = j + 1
        
        sentiment_output = analysis.sentiment(text)
        data.iloc[i-1,2] = sentiment_output.sentiment.overall
        data.iloc[i-1,3] = sentiment_output.sentiment.positivity
        data.iloc[i-1,4] = sentiment_output.sentiment.negativity
    data.to_csv('D:\Amrita\AM@hack\Expert.AI-Hackathon\questions.csv', index=False)
