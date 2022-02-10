from speak import *

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Sir!")

    elif hour>=12 and hour<12:
        speak("Good Afternoon Sir!")

    else:
        speak("Good evening Sir!")

    speak("I am Nova. Please tell me how may I help you my leige.")