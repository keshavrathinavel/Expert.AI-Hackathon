import speech
import analysis
import pandas as pd

data = pd.read_csv('D:\Amrita\AM@hack\Expert.AI-Hackathon\questions.csv')

for i in range(1,2):
    # name = 'Q'
    # x = name + str(i) + '.wav'
    # text = speech.speech_using_audio_file(x)
    # text = text.replace(',', '')
    text = "i want to murder children and cut up cats"
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