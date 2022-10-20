import speech_recognition as sr
def speech(self):

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile() as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Sphinx
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    return r.recognize_sphinx(audio)