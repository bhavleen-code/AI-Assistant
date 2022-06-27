import pyttsx3
import datetime
import speech_recognition as s
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine=pyttsx3.init()

voices =engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate=200
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hello, This is jarvis made by Bhavleen Kaur.")    

def time():
    speak("Current time is")
    time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back mam !!")
   
    hour=datetime.datetime.now().hour

    if hour>=6 and hour<=12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    elif hour>=18 and hour<=24:
        speak("Good evening")
    else: 
        speak("Good night")

    speak("Always at your service. How I can help you?")


def takeCommand():
    sr=s.Recognizer()
    print("Listening you...")
    with s.Microphone() as m:
        audio=sr.listen(m)
        
    try:
        print("Recognizing...")
        query=sr.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")  

        return "None"
    return query

def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("bhavleen007@gmail.com","b1793502790")
    server.sendmail("bhavleenkaur2021@gmail.com",to,content)
    server.close()

def screenshot():
    img =pyautogui.screenshot()
    img.save("D:\PERSONAL developement\All about codes\CODE\JARVIS\ss.png")

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at "+usage)

    battery=psutil.sensors_battery().percent
    speak("Battery is at")
    speak(battery)

def jokes():
    speak(pyjokes.get_joke())    

if __name__ == '__main__':

    wishme()

    while True:
        query= takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("Signing off Bhavleen BYE BYE Have a good day")
            quit()
        elif "wikipedia" in query:
            speak("Searching...give me second")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak(result)    
        elif "mail" in query:
            try:
                speak("What should I say")
                content=takeCommand()
                to="bhavleenkaur2021@gmail.com"
                sendmail(to,content)
                speak("Email is sent successfully boss!!")    
                speak("sent message is : "+content)
            except Exception as e:
                    speak(e)
                    print(e)
                    speak("Sorry Mam unable to send the meassage")
        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif "logout" in query:
            os.system("shutdown - l")

        elif "shutdown" in query:
            os.system("shutdown /s /t l")

        elif "restart" in query:
            os.system("shutdown /r /t l")

        elif "play song" in query:
            song_dir =r"C:\Users\Bhavleen Kaur\Music\playlist"
            songs = os.listdir(song_dir)
            os.startfile(os.path.join(song_dir,songs[0]))

        elif "remember" in query:
            speak("What should i remember?")
            data= takeCommand()
            speak("you said me to remember that"+data)
            remember =open("data.txt","w")
            remember.write(data)
            remember.close()  

        elif "do you know anything" in query:
            remember= open("data.txt","r")
            speak("you said me to remember that"+ remember.read())    

        elif "screenshot" in query:
            screenshot()
            speak("done!!")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()