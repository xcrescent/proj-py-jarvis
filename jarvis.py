import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
# import time
import requests
# import playsound
import webbrowser
import os
import keyboard
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# import tkinter

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
    # speak("Dhruv Bhai Bhej Dia Email, email has been sent!")
    # speak("I'm Jarvis. You must be Utkarsh Singh. Please tell me how may I help you?")
    speak("I'm Jarvis.")

# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))

# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

def sendEmail(to, content):
    port = 465  # For SSL
    username = "noedmale@gmail.com" 
    # username = input("Type your username and press enter: ")
    password = "150783p*" 
    # password = input("Type your password and press enter: ")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(username, password)
        # TODO: Send email here
        server.sendmail(username, to, content)


def takeCommand():
    # It takes microphone input from the user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print  ("Listening....")
        r.pause_threshold = 0.7
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        # query = r.recognize_google(audio, Language='en-US')
        query = r.recognize_google(audio)
        # speak(f"User said: {query}\n")  
        print(f"User said: {query}\n")  

    except Exception as e:
        #print(e)
        print("Sorry, Type that again please...")
        takeInput()
        return "None"
    return query

def takeEmailInput():
    # It takes microphone input from the user and returns string output.
    speak('Enter Text For Email')
    inputString = input('Enter Text For Email:')
    return inputString


def takeInput():
    inputString = input('Enter a command:')
    inputStrng = inputString.lower()
    print(f"You entered: {inputString}\n")  
    # inputStrng = takeInput().lower()

    if 'hello' in inputStrng:
        speak(inputStrng)
        # takeInput()
    elif keyboard.is_pressed("b"):
            print("akg")
            takeCommand()

    elif 'bye' in inputStrng:
        speak(inputStrng)
        # takeInput()

    elif 'voice command' in inputStrng:
        speak('Taking Voice Commands Now')
        takeCommand()

    elif 'wikipedia' in inputStrng:
        speak('Searching wikipedia....')
        inputStrng = inputStrng.replace("wikipedia", "")
        results = wikipedia.summary(inputStrng, sentences=3)
        speak("According to Wikipedia")
        # lis = BeautifulSoup(html).find_all('li')
        print(results)
        speak(results)
        # takeInput()

    elif 'open youtube' in inputStrng:
        # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.open_new_tab("youtube.com")
        # webbrowser.open("youtube.com")
        # takeInput()

    elif 'open google' in inputStrng:
        webbrowser.open("google.com")
        # takeInput()

    elif 'open eliteacademy' in inputStrng:
        webbrowser.open('eliteacademy.co.in')
        # takeInput()

    elif 'open cpanel' in inputStrng:
        webbrowser.open('console.eliteacademy.co.in')
        # takeInput()

    elif 'open test' in inputStrng:
        webbrowser.open("test.eliteacademy.co.in")
            # takeInput()

    elif ('play music') in inputStrng:
        music_dir = 'D:\\Backup\\Galaxy J2\\com.yy.hiyo\\audio\\soundConfig'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        # takeInput()
    
    elif 'heloo' in inputStrng:
        speak("helloo helloo helloo")
        # takeInput()

    elif 'byie' in inputStrng:
        speak("bye bye bye")
        print("bye bye bye")
        # takeInput()

    elif 'up to down' in inputStrng:
        speak("upto down")
        # takeInput()
    elif 'voice input' in inputStrng:
        speak("Switching to voice input")
        # takeInput()    
    
    elif 'the time' in inputStrng:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
        print(f"Sir, the time is {strTime}")
        # takeInput()

    elif 'kiss me' in inputStrng:
        speak('I would love to but....')
        # takeInput()

    elif 'open chrome' in inputStrng:
        try:
            speak('trying to open chrome')
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"  
            os.startfile(chromePath)
        except:
            speak("Sorry dhruv bhai. I was not able to open chrome")

    elif 'open code' in inputStrng:
        codePath = "C:\\Users\\usjad\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"  
        os.startfile(codePath)
        speak('opening v s code')

    elif 'Hello world' in inputStrng:
        print("Computer")
        # takeInput()
    
    elif 'email to me' in inputStrng:
        try:
            speak("What should I say?")
            content = takeEmailInput()
            to = "utkavar@gmail.com"
            sendEmail(to, content)
            speak("DDhhrruuvV BBhhaaii BBhheajj Diiiaaa Email, email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry dhruv bhai. I was not able to send this email")
            print("Not able to Email Currently")

    elif 'say' in inputStrng:
        inputStng = inputStrng.replace("say", "")
        if 'you are an idiot' in inputStrng:
            nputStng = inputStng.replace("you are", "i am")
        #     if 'are' in nputStng:
        #         nputtng = nputStng.replace("are", "am")
        #         # speak(nputtng)
        #     if "'re" in inputStrng:
        #         npuStng = nputStng.replace("'re", "'m")
        #         # speak(npuStng)
        #     if "me" in inputStrng:
        #         npuStng = nputStng.replace("me", "you")
        #         speak(npuStng)
        #     # else:
            speak(nputStng)
            print(nputStng)
        # elif "your" in inputStrng:
        #     nputStng = inputStng.replace("your", "mine")
        #     speak(nputStng)
        #     if 'are' in nputStng:
        #         nputtng = nputStng.replace("are", "am")
        #         speak(nputtng)
        #     elif "'re" in inputStrng:
        #         npuStng = nputStng.replace("'re", "'m")
        #         speak(npuStng)
        #     elif "me" in inputStrng:
        #         npuStng = nputStng.replace("me", "you")
        #         speak(npuStng)

        else:
            speak(inputStng)
            print(inputStng)
    elif 'i love you' in inputStrng:
        # inputStng = inputStrng.replace("you", "")
        speak(inputStrng + "two times more")
        print(inputStrng + "two times more")
    elif 'you born' in inputStrng:
        # inputStng = inputStrng.replace("you", "")
        print('I was created in 2021 by a great guy called Utkarsh')
        speak('I was created in 2021 by a great guy called Utkarsh')
    elif 'wish me' in inputStrng:
        # inputStng = inputStrng.replace("you", "")
        # print('I was created in 2021 by a great guy called Utkarsh')
        # speak('I was created in 2021 by a great guy called Utkarsh')
        wishMe()
        print("Hello")
    else:
        speak('You are an idiot!')
        print('You are an idiot!')
        speak('You said:' + inputStrng)
        print('You said:' + inputStrng)
        # takeInput()

    # except Exception as e:
    #     #print(e)
    #     print("Error in processing...")
    #     return "None"
    # return inputString

if __name__ == "__main__":
    wishMe()
    # 
    # webbrowser.register('chromee', None, webbrowser.BackgroundBrowser(chrome_path))
    # speak("press b to communicate using text")
    # inputString = input('Enter a command:')
    # inputStrng = inputString.lower()
    # if 'no' in inputStrng:
    #     takeInput()
    #     while True:
    #         takeInput()
    # else:

    takeCommand()
    while True:
        query = takeCommand().lower()
        # inputString = input()
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
        elif 'open whatsapp' in query:
                
            ## command using py
            # os.system('pip install pyaudio')
            os.system("explorer shell:appsfolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!WhatsAppDesktop")
            
        elif 'hello world' in query:
            print("Computer")
        elif 'quit exit' in query:
            break
        # elif keyboard.is_pressed("b"):
        #     print("akg")
        #     takeInput()
        # else:
        #     takeInput()
        # elif 'email to me' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "yourEmail@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend dhruv bhai. I am not able to send this email")
        elif 'email to me' in query:
            # https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python
            try:
                speak("What should I say?")
                content = takeEmailInput()
                to = "usjadon19@gmail.com"
                sendEmail(to, content)
                speak("Utkarsh Bhai Bhej Dia Email, email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry utkarsh sir . I was not able to send this email")
                print("Not able to Email Currently")
    # while False:
    #     print("hey")
