
import os
from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

os.environ["EAI_USERNAME"] = 'bl.en.u4cse20074@bl.students.amrita.edu'
os.environ["EAI_PASSWORD"] = 'dBbuc.3CAfYuvy6'

def hatespeechdetection(text):
    detector = 'hate-speech'
    language= 'en'
    output = client.detection(body={"document": {"text": text}}, params={'detector': detector, 'language': language})
    print("\nCategorization: ID Code + Category")

    for category in output.categories:
        print(category.id_, category.hierarchy, sep="\t")

    print("\nRunning Hate-Speech Detection: ")

    i = 1
    for extraction in output.extractions:
        print("Record #{}:".format(i))
        for field in extraction.fields:
            print("{} = {}".format(field.name, field.value))
        i = i + 1
    
def behavioural_analysis(text):   
    taxonomy = 'behavioral-traits'
    language= 'en'

    output = client.classification(body={"document": {"text": text}}, params={'taxonomy': taxonomy, 'language': language})

    print("Tab separated list of categories:")

    for category in output.categories:
        print(category.id_, category.hierarchy, sep="\t")

def sentiment(text):
    language= 'en'
    output = client.specific_resource_analysis(
        body={"document": {"text": text}}, 
        params={'language': language, 'resource': 'sentiment'
    })

    print("Overall sentiment: " + str(output.sentiment.overall))
    print("Negativity sentiment: " + str(output.sentiment.negativity))
    print("Positivity sentiment: " + str(output.sentiment.positivity))

