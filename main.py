import os
os.environ['TF_CPP_MIN_LOG_LENGTH']='2'

import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import datetime
import time
import pywintypes

engine=pyttsx3.init()

def youtube():
    r1=sr.Recognizer()
    r2=sr.Recognizer()
    r3=sr.Recognizer()
    engine=pyttsx3.init()
    engine.say("Alright sir, Youtube has been enabled!")
    url='https://www.youtube.com/'
    with sr.Microphone() as source:
        audio=r2.listen(source)
        try:
            get=r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("An error occured")

        except sr.RequestError as e:
            print('failed'.format(e))    

def email():
    r1=sr.Recognizer()
    r2=sr.Recognizer()
    r3=sr.Recognizer()
    engine=pyttsx3.init()
    engine.say("Working on it Sir, opeining email now:")
    url1=''
    url2=''
    with sr.Microphone() as source:
        audio=r2.listen(source)
        if 'IIT Goa' in r3.recognize_google(audio):
            try:
                get=r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url1+get)
            except sr.UnknownValueError:
                print("An error occured")

            except sr.RequestError as e:
                print('failed'.format(e)) 
            finally:
                anythingelse()      
        elif 'Personal' in r3.recognize_google(audio):
            try:
                get=r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url2+get)
            except sr.UnknownValueError:
                print("An error occured")

            except sr.RequestError as e:
                print('failed'.format(e)) 
        else:
            engine.say("Sorry sir, I wasn't able to understand that, please speak clearly.")        





def google():
    r1=sr.Recognizer()
    r2=sr.Recognizer()
    r3=sr.Recognizer()
    engine=pyttsx3.init()
    engine.say("Yes sir, I'm fetching google for you")
    url='https://www.google.co.in/'
    with sr.Microphone() as source:
        audio=r2.listen(source)
        try:
            get=r2.recognize_google(audio)
            print(get)
            wb,get().open_new(url+get)
        except sr.UnknownValueError:
            print("An error occured")

        except sr.RequestError as e:
            print('failed'.format(e))
        finally:
            anythingelse()      
                
def weather():
    r1=sr.Recognizer()
    r2=sr.Recognizer()
    r3=sr.Recognizer()
    engine=pyttsx3.init()
    engine.say("As you say sir. The weather isn't a predictable phenomenon, its quite uncanny I know, but let me fetch it for you!")
    url= 'https://www.google.co.in/search?q=google+weather&source=hp&ei=JWIKYYq6E8eb-AbgooOYAQ&iflsig=AINFCbYAAAAAYQpwNSd_4SxKA1t410axftqTCgEqZ-a1&oq=google+weather&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAEIAEELEDEEYQgAIyCAgAEIAEELEDMggIABCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyCAgAEIAEEMkDMgUIABCABDIFCAAQgAQ6CwgAEIAEELEDEIMBOggIABCxAxCDAToOCAAQgAQQsQMQgwEQyQM6BQgAEJIDUI0DWN0mYL4vaABwAHgAgAGGAYgB0Q2SAQQwLjE0mAEAoAEB&sclient=gws-wiz&ved=0ahUKEwjK4NeAi5fyAhXHDd4KHWDRABMQ4dUDCAc&uact=5'
    with sr.Microphone() as source:
        audio=r2.listen(source)
        try:
            get=r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("An error occured")

        except sr.RequestError as e:
            print('failed'.format(e))
        finally:
            anythingelse()    
            
def greeter():
    engine=pyttsx3.init()
    currentTime = time.strftime('%H:%M') 
    if currentTime.hour<12:
        engine.say("Good Morning Sir!")
    elif 18>currentTime.hour>12:
        engine.say("Good Afternoon Sir!")
    elif currentTime.hour>18:
        engine.say("Good Evening Sir!")
    else:
        print("Error occured")
                   

def anythingelse():
    engine=pyttsx3.init()
    ask=engine.say("Is there anything else I could do sir?")
    r1=sr.Recognizer()
    r2=sr.Recognizer()
    r3=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r3.listen(source)

    if "Proceed" in r2.recognize_google(audio):
        command()
    elif "End"  in r2.recognize_google(audio):
        engine.say("Thank You. Always at your service sir!")
    else:
        print("Error occured!")
        anythingelse()          




def command():
    r1=sr.Recognizer()
    r2=sr.Recognizer()
    r3=sr.Recognizer()
    engine=pyttsx3.init()
    engine.say("What can I do for you sir?")
    with sr.Microphone as source:
        audio=r2.listen(source)
    if 'Youtube' in r3.recognize_google(audio):

        youtube()
    elif 'Email' in r3.recognize_google(audio):
        email()
    elif 'Google' in r3.recognize_google(audio):
        google()
    elif 'Weather' in r3.recognize_google(audio):

        weather()        
    else:
        anythingelse()    





       


