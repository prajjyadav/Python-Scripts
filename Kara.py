import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import smtplib
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

emaildict = {   
                "soham" : "bppcs.11500119115@gmail.com", 
                "subhrakanti" : "bppcs.11500119116@gmail.com", 
                "tathagata" : "bppcs11500119117@gmail.com", 
                "sourasish" : "bppcs.11500119119@gmail.com" 
            }

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Hello! I am Kara. How may I help you?")
    print("Hello! I am Kara. How may I help you?")

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

    except Exception:   
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('testemailforkara@gmail.com', 'karabypitchers')
    server.sendmail('testemailforkara@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            print('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            print("According to Wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open github' in query:
            webbrowser.open("github.com")   

        elif 'open whatsapp' in query:
            speak("Opening whatsapp...")
            print("Opening whatsapp...")
            webbrowser.open("https://web.whatsapp.com/") 

        elif 'play' and 'song' in query:
            speak("Searching song....")
            print("Searching song....")
            query = query.replace("play", "")
            webbrowser.open("https://www.youtube.com/results?search_query=" + query)
        
        elif 'search' and 'in youtube' in query:
            speak("Searching, please wait...")
            print("Searching, please wait...")
            query = query.replace("search ", "")
            query = query.replace(" in youtube", "")
            webbrowser.open("https://www.youtube.com/results?search_query=" + query)

        elif 'search' in query:
            speak("Searching, please wait...")
            print("Searching, please wait...")
            query = query.replace("search ", "")
            webbrowser.open("https://www.google.com/search?q=" + query)

        elif 'what' and 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The current time is {strTime}")
            print("The current time is",strTime)

        elif 'what' and 'date' in query:
            strdate=datetime.datetime.now().strftime("%d%m20%y")
            strdate1=datetime.datetime.now().strftime("%d-%m-20%y")
            speak(f"Today's date is {strdate}")
            print("Today's date is",strdate1)

        elif 'send an email to' in query:
            try:
                query = query.replace("send an email to ", "")
                to = emaildict[query]
                speak("What should I say?")
                print("What should I say?")
                content = takeCommand()    
                sendEmail(to, content)
                speak("Your email has been sent succesfully!")
                print("Your email has been sent succesfully!")
            except Exception:
                speak("Sorry! I am not able to send this email")
                print("Sorry! I am not able to send this email")
        
        elif 'quit' in query:
            speak("Quitting...")
            print("Quitting...")
            exit()