
import os
from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

os.environ["EAI_USERNAME"] = 'bl.en.u4cse20074@bl.students.amrita.edu'
os.environ["EAI_PASSWORD"] = 'dBbuc.3CAfYuvy6'

text = 'i want to murder children and eat my cats'

def hatespeechdetection(text):
    detector = 'hate-speech'
    language= 'en'
    output = client.detection(body={"document": {"text": text}}, params={'detector': detector, 'language': language})
    return output

    
def behavioural_analysis(text):   
    taxonomy = 'behavioral-traits'
    language= 'en'
    output = client.classification(body={"document": {"text": text}}, params={'taxonomy': taxonomy, 'language': language})
    return output

def sentiment(text):
    language= 'en'
    output = client.specific_resource_analysis(
        body={"document": {"text": text}}, 
        params={'language': language, 'resource': 'sentiment'
    })
    print("Overall sentiment: " + str(output.sentiment.overall))
    print("Negativity sentiment: " + str(output.sentiment.negativity))
    print("Positivity sentiment: " + str(output.sentiment.positivity))
    return output

