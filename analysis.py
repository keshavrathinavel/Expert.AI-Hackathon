import os
os.environ["EAI_USERNAME"] = 'BL.EN.U4CSE20057@bl.students.amrita.edu'
os.environ["EAI_PASSWORD"] = 'Hemanth@200204'
def sentiment(self):
    from expertai.nlapi.cloud.client import ExpertAiClient
    client = ExpertAiClient()

    text = "you are amazing!" 
    language= 'en'

    output = client.specific_resource_analysis(
        body={"document": {"text": text}}, 
        params={'language': language, 'resource': 'sentiment'
    })

    print("Output overall sentiment:")

    print(output.sentiment.overall)

def hatespeech(self):
    print("he;;[")