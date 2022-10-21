def behavioural_analysis(text):
    import os
    os.environ["EAI_USERNAME"] = 'bl.en.u4cse20074@bl.students.amrita.edu'
    os.environ["EAI_PASSWORD"] = 'dBbuc.3CAfYuvy6'
    from expertai.nlapi.cloud.client import ExpertAiClient
    client = ExpertAiClient()
    

    taxonomy = 'behavioral-traits'
    language= 'en'

    output = client.classification(body={"document": {"text": text}}, params={'taxonomy': taxonomy, 'language': language})

    print("Tab separated list of categories:")

    for category in output.categories:
        print(category.id_, category.hierarchy, sep="\t")

text = "Michael Jordan was one of the best basketball players of all time. Scoring was Jordan's stand-out skill, but he still holds a defensive NBA record, with eight steals in a half."
behavioural_analysis(text)