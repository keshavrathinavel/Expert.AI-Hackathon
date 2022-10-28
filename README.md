## Requirements
Run ```pip install -r requirements.txt``` with cmd open in root directory

## How to run
1. Run main.py to execute the project.
2. Ensure your PC microphone is turned on and access is allowed system-wide.
3. Input your audio answers for every question as per the instructions on-screen.
4. The questions, respective answers and respective outputs are saved in the CSV file.


## Inspiration
In India, where the team comes from, there is visible stigma revolving around concepts pertaining to mental health such as illnesses and seeking professional help. This stigma creates self-doubt and reluctance to get necessary treatment. Coupled with the lack of understanding from peers, friends and family, the inability to get access to professional treatment can be detrimental to many.  To curb this, our team has come up with _WALL-E_, taking inspiration from the movie character from the popular cinematic - _WALL-E_, a robot capable of human emotion and breaking free from prejudicial norms much like the people we are targeting with this product.

## What it does
_WALL-E_ is built to reduce the number of steps it takes for one to get help from a psychological professional. The program works by -
1. First, presenting a set of questions we obtained from popular Psych Evaluations/ curated Psych Evaluations. 
2. The answers to these questions are to be input as voice recordings from the users. 
3. The voice recordings are converted to text using _Google's API for Automatic Speech to Text conversion_. 
4. The text is then saved in our database, a CSV file that we use to maintain all data regarding the questions, answers, outputs and analysis.
5. The text is then stripped of commas and passed as the argument to our functions which are - a) Behavior analysis b) Hate-Speech Detection and Analysis c) Sentiment Analysis 
6. Each of the aforementioned functions uses the Expert.AI's API. Our unique client uses the API for behavior analysis, hate-speech detection and analysis and sentiment analysis to detect patient's current state based on his/her answers.
7. The outputs that we get from these functions are then saved into the CSV file for easy reference by a psychologist.  

## How we built it
1. We built the GUI using the Python package - **Tkinter**, the standard Python interface to the Tcl/Tk GUI toolkit. 
2. Functionality to record answers for the questions is provided interface. We have also enabled deleting and listening to the recordings for the user. This recorded audio is saved in _.wav_ format in the root directory.
3. Each .wav file is saved as the answer for the respective question - answer to question 1 is saved as Q1.wav , question 2 as Q2.wav and so on. 
4. This .wav file is passed to our Google Speech recognition functions as an argument.
5. The resulting output from Google Speech function is then passed over to Expert.AI's API functions for processing.
6. Our functions are enabled by Expert.AI's API and built using Python programming. Each of our functions that uses Expert.AI's API can be found in analysis.py file. 
7. Our functions are called in main.py where they take the .wav audio file, convert it to text and provide outputs after computing, which are saved into the CSV file to be viewed by a psychological professional.

## Challenges we ran into
1. The primary challenge was getting accurate conversions of speech input to text. 
2. We also had difficulty creating the UI, Tkinter is not as simple to use as one may assume.


## Accomplishments that we're proud of
Text answers cannot, essentially, be considered equal to vocal exchanges. The latter contains expression, emotional depth and can provide great inference with regard to the user's mental state. In order to preserve this valuable information, we developed necessary functions that could convey vital information pertaining to the mental state of the user. Granted, the essence of emotional profundity cannot be preserved but this ideology could pave ways to a product that can, in the future. Having been through the highs and lows of the commonly known dramatic teenage without access to a medical professional due to the aforementioned inhibitions, we understand the difficulties one might face taking the first step to seek help. Creating this application to reduce the initial friction could make something so basic, like psychiatric help, much more accessible than it is in today's age in my country. With that said, we are proud of the endeavor as a whole.

## What we learned
We also learned how to make effective usage of Expert.AI's API in the healthcare domain. We also learned it is best to stick to creating web applications over Tkinter GUI. Jokes apart, we learned very interesting applications of the pandas iloc function to save data into cells, rows and columns respectively in CSV files. 

## What's next for _WALL-E_?
_WALL-E_ has multiple use cases, many of which can be expanded beyond the domains of just behavioral analysis. Wall-e could be used as an extractive text summarizer. Say, for example, your next session with a therapist is a while away but you are going through challenging times. You could use _WALL-E_'s behavioral analysis to convey emotional depth, coupled with a built-in text summarizer to summarize all the input data. This feature could be modified to employ NER (Named Entity Recognition) to attach tags to important data (like names, dates, time, psychology dictionary terms et al).
