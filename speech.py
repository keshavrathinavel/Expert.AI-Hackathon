# def speech():
#     import speech_recognition as sr

#     # obtain audio from the microphone
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Say something!")
#         audio = r.listen(source)

    # recognize speech using recognize_google
    # try:
    #     data = r.recognize_google(audio)
    #     print("The text of the audio is:" + data)
    # except sr.UnknownValueError:
    #     print("Audio was unclear")
    # except sr.RequestError as e:
    #     print("API error; {0}".format(e))
    # return data

def speech_using_audio_file(name):
    import speech_recognition as sr
    from os import path
    file_name = name
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), file_name)

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using recognize_google
    try:
        data = r.recognize_google(audio)
        print("The text of the audio is:" + data)
    except sr.UnknownValueError:
        print("Audio was unclear")
    except sr.RequestError as e:
        print("API error; {0}".format(e))

    return data

