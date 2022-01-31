from urllib import response
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import random
from PyDictionary import PyDictionary
import requests
import json
import time
import pywhatkit
import pyautogui
import keyboard
import pyjokes

chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)
# print(voices)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Sir!")

    elif hour>=12 and hour<12:
        speak("Good Afternoon Sir!")

    else:
        speak("Good evening Sir!")

    speak("I am Nova. Please tell me how may I help you my leige.")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        # speak("Say that again please")
        return "None"

    return query

def whatsappMessage():     #this  is not working ripnesssss
    #doesn't work
    speak("Sir, Please type me the phone number of the person")
    phone = input()
    ph = '+91' + phone
    speak("Sir, please tell me the message you want to send")    
    msg = takeCommand().lower()
    speak("Sir, tell me the time, first, tell me the hour")
    hr = int(takeCommand())
    speak("Sir, now in minutes")
    min  = int(takeCommand())
    pywhatkit.sendwhatmsg(ph, msg, hr, min)
    speak("message sent sir.")

great_work = ["great work nova", "well done nova", "nova good work"]
if __name__=='__main__':
    
    while True:
        initial = takeCommand().lower()
        if 'nova wake up' in  initial:
                wishMe()
                break
        else:
            continue
    
    while True:
            
        query = takeCommand().lower()    #make it takecommand().lower()

    
        if 'nova wikipedia' in query:            
            speak('Speaking Wikipedia...')
            query = query.replace("nova", "")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'nova how are you' in query:
            how_list = ["i am doing good sir, what about you ?", "i am fine my leige, how well are you doing ?", "i am having a lot of fun sir, how about you sir"]
            rand_how = random.choice(how_list)
            speak(rand_how)
            well_or_no = takeCommand().lower()
            if 'not good' in well_or_no:
                speak("Don't worry sir everything will be fine just keep grinding. Ask me for a help anytime")
            elif 'bad' in well_or_no:
                speak("Don't worry sir everything will be fine just keep grinding. Ask me for a help anytime")
            elif 'not so well' in well_or_no:
                speak("Don't worry sir everything will be fine just keep grinding. Ask me for a help anytime")
            elif 'not fine' in well_or_no:
                speak("Don't worry sir everything will be fine just keep grinding. Ask me for a help anytime")
            elif 'great' in well_or_no:
                speak("Great, its a pleasure to know that you are doing good. Ask me for a help anytime")
            elif 'good' in well_or_no:
                speak("Great, its a pleasure to know that you are doing good")
            elif 'fine' in well_or_no:
                speak("Great, its a pleasure to know that you are doing good")
            elif 'happy' in well_or_no:
                speak("Thats amazing to know sir")
            elif 'same' in well_or_no:
                speak("Thats great sir, lets keep grinding")

        elif 'nova youtube search' in query:
            query = query.replace("nova", "")
            query = query.replace("youtube search", "")
            yt_web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.get('chrome').open_new_tab(yt_web)
            speak(f"Ok sir, this is what i found for {query} on youtube")
        
        elif 'nova play video on youtube' in query:
            query = query.replace("nova play video", "")
            query = query.replace("on youtube", "")
            pywhatkit.playonyt(query)            
            speak(f"Ok sir, this is what i found for {query} on youtube")
        
        elif 'nova open stack overflow website' in query:
            webbrowser.get('chrome').open_new_tab("stackoverflow.com")
        
        elif 'nova open google' in query:
            webbrowser.get('chrome').open_new_tab("google.com")
            
        elif 'nova google search' in query:
            query = query.replace("nova", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            speak(f"Ok sir, this is what i found for {query} on google")
            
        elif 'nova what is' in query:
            query = query.replace("nova what it", "")
            pywhatkit.info(query, lines=4)

        elif 'nova send a whatsapp message' in query:
            whatsappMessage()

        elif 'nova take a screenshot' in query:         #not working ripppppppp
            ss = pyautogui.screenshot(r'F:\pypy\Nova')
            speak("Done sir.")
            
                   

        elif 'nova open website' in query:
            query = query.replace("nova", "")
            query = query.replace("website", "")
            query = query.replace("open", "")
            web_open = query + ".com"
            webbrowser.get('chrome').open_new_tab(web_open)
            speak(f"Ok sir, opening {query} on your browser")

        elif 'nova play song' in query:
            query = query.replace("nova play song", "")
            pywhatkit.playonyt(query)            
            speak(f"Ok sir, now playing {query}")
        
        
        elif 'nova play some music' in query:
            music_dir = 'F:\\Music'
            songs = os.listdir(music_dir)
            print(*songs, sep="\n")
            speak("Do you want a surprise song my king ?")
            surprise_or_no = takeCommand().lower()
            if 'yes' in surprise_or_no:
                ran = random.randint(1,len(songs))
                os.startfile(os.path.join(music_dir,songs[ran]))

            elif 'no' in  surprise_or_no:
                speak("Please tell the song number you want to play")
                song_no = takeCommand()
                os.startfile(os.path.join(music_dir,songs[int(song_no)-1]))
                        
        elif 'nova what is the time' in query:
            Timing = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {Timing}")

        elif 'nova open code' in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening visual studio code for you")
            os.startfile(codePath)
        
        elif 'nova open spotify' in query:
            SpotifyPath = "C:\\Users\\user\\AppData\\Roaming\\Spotify\\Spotify.exe"
            speak("Opening Spotify for you")
            os.startfile(SpotifyPath)
        
        elif 'nova open pycharm' in query:
            pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\bin\\pycharm64.exe"
            speak("Opening pycharm for you")
            os.startfile(pycharmPath)
        
        elif 'open valorant' in query:
            valorantPath = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
            speak("Opening valorant for you")
            os.startfile(valorantPath)
        
        elif 'nova open chrome' in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            speak("Opening chrome for you")
            os.startfile(chromePath)
        elif 'nova open edge' in query:
            edgePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            speak("Opening microsoft edge for you")
            os.startfile(edgePath)
        
        elif 'nova open brave' in query:
            bravePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            speak("Opening brave for you")
            os.startfile(bravePath)
        
        elif 'nova open discord' in query:
            discordPath = "C:\\Users\\user\\AppData\\Local\\Discord\\Update.exe"
            speak("Opening discord for you")
            os.startfile(discordPath)

        elif random.choice(great_work) in query:
            thank_list = ["thank you my leige", "thanks for the appreciation", "i am glad that you liked me"]
            speak(random.choice(thank_list))

        elif 'nova find the meaning of a word' in query:
            speak("may i please know the word for which you want the meaning")
            meaning_of = takeCommand().lower()
            word_dic = PyDictionary()
            meaning_is = word_dic.meaning(meaning_of)
            speak(f"the meaning of the word {meaning_of} is {meaning_is}")

        elif 'tell me some news' in query:
            speak("News for today.. Lets begin")
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=dc325656b9a74c0db0feff0e82e9711b"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            for article in arts:
                speak(article['title'])
                print(article['title'])
                speak("Moving on to the next news..Listen Carefully")
            
        elif 'joke' in query:
            jokeslol = pyjokes.get_joke()
            speak(jokeslol)
            print(jokeslol)

        elif 'nova bye' in query:
            speak("Thank you for using me, make sure to come back later")
            exit()

        