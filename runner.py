import analysis

# We take the voice recording using Google's API and convert it to usable text
def speech():
    import speech_recognition as sr

    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using recognize_google
    try:
        data = r.recognize_google(audio)
        print("The text of the audio is:" + data)
    except sr.UnknownValueError:
        print("Audio was unclear")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

# Removing commas within the recognized text to avoid errors with the csv
text = speech()
text = str(text)
text = text.replace(',', '')

# Using Expert.AI, we create sentiment, behaviour and hate-speech analysis
analysis.sentiment(text)
analysis.hatespeech(text)

# Tabulate our results in a CSV and score them according to their immediate need for a psychological professional