import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!") 

    else:
        speak("Good Evening")
    
    speak("I am Archi sir. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print  ("Listening....")
        audio = r.listen(source)
        # r.pause_threshold = 1
        # print("hey")

    try:
        print("Recognizing....")
        # for index, name in enumerate(sr.Microphone.list_microphone_names()):
        #     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
        # print(f"User said: {audio}\n")  
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
        speak(query)  
        

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    takeCommand()
    while True:
        query = takeCommand().lower()
    
         # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open elite academy' in query:
            webbrowser.open("eliteacademy.co.in")

        elif 'open c panel' in query:
            webbrowser.open("cpanel.eliteacademy.co.in")

        elif 'open test' in query:
            webbrowser.open("test.eliteacademy.co.in")

        elif ('play music') in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'hello' in query:
            speak("hello hello hello")

        elif 'bye' in query:
            speak("bye bye bye")

        elif 'up to down' in query:
            speak("upto down")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")     

        elif 'open code' in query:
            codePath = "C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
            os.startfile(codePath)
        
        # elif 'email to me' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "yourEmail@gmail.com"
        #       sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend dhruv bhai. I am not able to send this email")
