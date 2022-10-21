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


    return data
speech()
