import sounddevice as sd
from tkinter import *
import queue
import soundfile as sf
import threading
from tkinter import messagebox

class audio:
    #Create a queue to contain the audio data
    q = queue.Queue()
    #Declare variables and initialise them
    recording = False
    file_exists = False

    def __init__(self, name):
        self.file_name = name

    def callback(self, indata, frames, time, status):
        self.q.put(indata.copy())


    def threading_rec(self, x):
        if x == 1:
            #If recording is selected, then the thread is activated
            t1=threading.Thread(target = self.record_audio)
            t1.start()
        elif x == 2:
            #To stop, set the flag to false
            global recording
            recording = False
            messagebox.showinfo(message="Recording finished")
        elif x == 3:
            #To play a recording, it must exist.
            if file_exists:
                #Read the recording if it exists and play it
                data, fs = sf.read(self.file_name, dtype='float32')
                sd.play(data,fs)
                sd.wait()
            else:
                #Display and error if none is found
                messagebox.showerror(message="Record something to play")


    def record_audio(self):
        #Declare global variables   
        global recording
        #Set to True to record
        recording= True  
        global file_exists
        #Create a file to save the audio
        messagebox.showinfo(message="Please start talking after 2 seconds since you press the button")
        with sf.SoundFile(self.file_name, mode='w', samplerate=44100,
                            channels=2) as file:
        #Create an input stream to record audio without a preset time
                with sd.InputStream(samplerate=44100, channels=2, callback=self.callback):
                    while recording == True:
                        #Set the variable to True to allow playing the audio later
                        file_exists =True
                        #write into file
                        file.write(self.q.get())



class main:

    def __init__(self,name):
        aud = audio(name)
        voice_rec = Tk()
        voice_rec.geometry("360x200")
        voice_rec.title("Voice Recorder")
        voice_rec.config(bg="#ffffff")
        title_lbl  = Label(voice_rec, text="Press the record button to begin and Stop to end", bg="#ffffff").grid(row=0, column=0, columnspan=3)

        #Button to record audio
        record_btn = Button(voice_rec, text="Record Audio", command=lambda m=1:aud.threading_rec(m))
        #Stop button
        stop_btn = Button(voice_rec, text="Stop Recording", command=lambda m=2:aud.threading_rec(m))
        #Play button
        play_btn = Button(voice_rec, text="Play Recording", command=lambda m=3:aud.threading_rec(m))
        #Position buttons
        record_btn.grid(row=1,column=1)
        stop_btn.grid(row=1,column=0)
        play_btn.grid(row=1,column=2)
        voice_rec.mainloop()

