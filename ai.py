
from pyaudio import paDirectSound
import speech_recognition
import time
import pywhatkit
import webbrowser
import wikipedia
import os
import playsound2

print("Loading...")

import pyttsx3
engine = pyttsx3.Engine()
voice = engine.getProperty("voices")
engine.setProperty("voice",voice[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def reco():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("Listening...")
        speak("Hearing you")
        recognizer.adjust_for_ambient_noise(mic)
        # recognizer.pause_threshold = 1
        audio = recognizer.record(mic,duration=3)
        try:
            print("Reconizing...")
            text = recognizer.recognize_google(audio,language="en-UK",show_all=False)
            print(f"User Said:{text}")
            query = text.lower()
            if 'music' in query:
                print("Enter Music file Path to the code")
                speak("Why Not sir")
                playsound2.playsound('Enter Music file Path here')
                exit()
            elif 'play' in query:
                print("Searching")
                speak("Searching")
                query = query.replace("play",'')
                query = query.replace('hey','')
                pywhatkit.playonyt(query)
                time.sleep(1.5)
                speak("Playing")
                print("Playing On YT")
                print("I am Sleeping for the 2 Minutes")
                speak("I am Sleeping for the last 2Minutes")
                time.sleep(180)
            elif 'song' in query:
                print("Searching")
                speak("Searching")
                query = query.replace("song",'')
                query = query.replace('hey','')
                pywhatkit.playonyt(query)
                time.sleep(1.5)
                speak("Playing")
                print("Playing On YT")
                print("I am Sleeping for the 2 Minutes")
                speak("I am Sleeping for the last 2Minutes")
                time.sleep(180)
            elif 'time' in query:
                print(time.ctime())
                speak(time.ctime())

            elif 'exit' in query:
                print('Exiting...')
                speak("See you sir later")
                exit()

            elif 'wikipedia' in query:
                print("Searching in Wikipedia: ")
                speak("Searching in Wikipedia")
                query = query.replace('wikipedia','')
                results = wikipedia.summary(query,2)
                print(results)
                speak(f"{results} according to wikipedia")
                
            elif 'youtube' in query:
                print("Opening Youtube For You")
                speak("Youtube opening in just few")
                webbrowser.open("youtube.com")

            elif 'are you genius' in query:
                speak("Yeesss I am genius")
                print("Yess I am Genius")
            elif 'are you single' in query:
                print("NOooooo I have the relationship with my alexa")
                speak("I have the relationship with the alexa")
                
            elif 'google' in query:
                print("Opening the Google for you")
                speak("Opening the google ")
                webbrowser.open("google.com")

            elif 'codewithharry' in query:
                print("CodeWithHarry Youtube Channel Found Opening...")
                speak("Codewithharry channel founded opening in just few")
                cwh= 'https://www.youtube.com/results?search_query=code+with+harry'
                webbrowser.get().open(cwh)

            elif 'code' in query:
                print("Opening VS Code in just few")
                speak("Opening Vs code in just few")
                os.startfile("C:\\Users\\raush\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.exe")

            elif "system information" in query:
                speak("Searching System Information>>>")
                print("System information is Searching: ")
                cmd = 'systeminfo'
                os.system(cmd)
                speak("Here is your specifications of your computer")
                print("specifications of your computer")
            else:
                print("Searching")
                query = query.replace('search','')
                pywhatkit.search(query)
                speak("Searching")


        except Exception as e:
            print("Say that again please...")
            speak("did not Get that.")
            # exit()
        
while True:
    reco()
