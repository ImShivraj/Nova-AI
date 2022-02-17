import pyttsx3 

<<<<<<< HEAD

=======
>>>>>>> new1
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)
# print(voices)


<<<<<<< HEAD
=======

>>>>>>> new1
def speak(audio):
    engine.say(audio)
    engine.runAndWait()