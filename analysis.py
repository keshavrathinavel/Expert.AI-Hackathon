
def sentiment(self, text):
    import os
    os.environ["EAI_USERNAME"] = 'BL.EN.U4CSE20057@bl.students.amrita.edu'
    os.environ["EAI_PASSWORD"] = 'Hemanth@200204'
    
    from expertai.nlapi.cloud.client import ExpertAiClient
    client = ExpertAiClient()
    language= 'en'

    output = client.specific_resource_analysis(
        body={"document": {"text": text}}, 
        params={'language': language, 'resource': 'sentiment'
    })

    print("Overall sentiment: " + str(output.sentiment.overall))
    print("Negativity sentiment: " + str(output.sentiment.negativity))
    print("Positivity sentiment: " + str(output.sentiment.positivity))

def hatespeech(self):
    print("he;;[")