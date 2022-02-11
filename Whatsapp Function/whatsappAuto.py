
from speak import *

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
    keyboard.press_and_release('enter')
    speak("message sent sir.")