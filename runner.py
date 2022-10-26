import analysis
import speech
import pandas as pd

# # We take the voice recording using Google's API and convert it to usable text
# text = speech.speech_using_audio_file()
# text = str(text)
# # Removing commas within the recognized text to avoid errors with the csv
# text = text.replace(',', '')

# # Using Expert.AI, we create sentiment, behaviour and hate-speech analysis
# analysis.behavioural_analysis(text)
# analysis.hatespeechdetection(text)
# analysis.sentiment(text)



for i in range(1, 5):
    question = pd.read_csv(r'D:\Amrita\AM@hack\Expert.AI-Hackathon\questions.csv')
    print(question.iloc[1,0])
    name = 'Q'
    # x = name + str(i) + '.wav'
    # text = speech.speech_using_audio_file(x)
    text = text.replace(',', '')
    text = str(text)
    text = "texting"
    question.iloc[i,1] = text
    # # Using Expert.AI, we create sentiment, behaviour and hate-speech analysis
    # analysis.behavioural_analysis(text)

    # # hate speech analysis
    # hate_speech_analysis = analysis.hatespeechdetection(text)
    # print("\nCategorization: ID Code + Category")
    # for category in hate_speech_analysis.categories:
    #     print(category.id_, category.hierarchy, sep="\t")

    # print("\nRunning Hate-Speech Detection: ")
    # i = 1
    # for extraction in hate_speech_analysis.extractions:
    #     print("Record #{}:".format(i))
    #     for field in extraction.fields:
    #         print("{} = {}".format(field.name, field.value))
    #     i = i + 1
    
    # # sentiment analysis
    # analysis.sentiment(text)


# Tabulate our results in a CSV and score them according to their immediate need
# for a psychological professional

# hemanth's csv code