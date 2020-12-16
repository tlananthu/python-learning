import os
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os

import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Abhinav!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Abhinav!")   

    else:
        speak("Good Evening Abhinav!")  

    speak("TIDA Activated!")       
 
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        
        print("Say that again please...")  
        return "None"
    return query



wishMe()

while True:
    

    query = takeCommand().lower()

    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        speak("ok! doing as you commanded")
        webbrowser.open("www.youtube.com")

    elif 'open google' in query:
        speak("ok! doing as you commanded")
        webbrowser.open("www.google.com")

    elif 'open stackoverflow' in query:
        speak("ok! doing as you commanded")
        webbrowser.open("www.stackoverflow.com")   


    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")


    elif 'turn on light' in query:
        speak("ok! doing as you commanded")
        webbrowser.open("192.168.1.1")
        os.system("taskkill /im iexplore.exe /f")

    elif 'who are you' in query:
        speak("I am TIDA which means the intelligent desktop assistant. I can perform many actions. I can open various websites, search something on google or wikipedia. control your home appliances and many more on your one command. I am under development system.")

    elif 'i want to open a website' in query:
        try:
            speak("Which website?")
            a = takeCommand()
            b= '.com'
            finalsite = a+b
            webbrowser.open(finalsite)
        except Exception as e:
            print(e)
            speak("Sorry. I am not able to open this")
        