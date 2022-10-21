
from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

def sentiment(self, text):
    import os
    os.environ["EAI_USERNAME"] = 'bl.en.u4cse20074@bl.students.amrita.edu'
    os.environ["EAI_PASSWORD"] = 'dBbuc.3CAfYuvy6'

    # from expertai.nlapi.cloud.client import ExpertAiClient
    # client = ExpertAiClient()
    language= 'en'

    output = client.specific_resource_analysis(
        body={"document": {"text": text}}, 
        params={'language': language, 'resource': 'sentiment'
    })

    print("Overall sentiment: " + str(output.sentiment.overall))
    print("Negativity sentiment: " + str(output.sentiment.negativity))
    print("Positivity sentiment: " + str(output.sentiment.positivity))

def hatespeech(self, text):
    import os
    os.environ["EAI_USERNAME"] = 'bl.en.u4cse20074@bl.students.amrita.edu'
    os.environ["EAI_PASSWORD"] = 'dBbuc.3CAfYuvy6'

    # from expertai.nlapi.cloud.client import ExpertAiClient
    # client = ExpertAiClient()
    # text = "i want to murder children and cut up cats"
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