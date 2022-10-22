import analysis
import speech

# We take the voice recording using Google's API and convert it to usable text
text = speech.speech()
text = str(text)
# Removing commas within the recognized text to avoid errors with the csv
text = text.replace(',', '')

# Using Expert.AI, we create sentiment, behaviour and hate-speech analysis
analysis.behavioural_analysis(text)
analysis.hatespeechdetection(text)
analysis.sentiment(text)

# Tabulate our results in a CSV and score them according to their immediate need
# for a psychological professional

# hemanth's csv code