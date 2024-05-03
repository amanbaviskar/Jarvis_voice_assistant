import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine=pyttsx3.init('sapi5') #to use voice we use sapi5
voices=engine.getProperty('voices')  #
engine.setProperty('voice',voices[0].id)# setting voice 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("good morning")
    elif hour>=12 and hour <18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am jarvis sir . Please tell me how may i help you")


def takecommand():# its takes microphone input form user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language='en-in')
        print(f'user said:{query}\n')
    except Exception as e:
        
        
        print("say that again please....")
        return "None"
    return query  
def sendEmail(to,content):
     server=smtplib.SMTP('smtp.gmail.com',587)
     server.starttls()
     server.login('amanbaviskar44@gmail.com','csfk rcok uxvc uvjj')
     server.sendmail('amanbaviskar44@gmail.com',to,content)
     server.close()
        
        

if __name__== "__main__":
    
    wishme()
    while True:
        query= takecommand().lower()
        if 'wikipedia' in query:
            print("searching wikipedia....")
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=4)
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com/in/aman-baviskar-776486237/")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
           music_dir='G:\\mp3'
           songs=os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")  
            speak(f'sir,the time is{strTime}') 
        elif 'open code' in query:
            codepath="C:\\Users\\amanb\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    
            os.startfile(codepath)
        elif 'send email to my friend' in query:
            try:
                speak("what should i say")
                content=takecommand()
                to="vedantsubhashjadhav@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry i am not able to sent the email")
        elif 'stop' in query:
            exit()
                
            
    
    