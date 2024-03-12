import speech_recognition
from pyttsx3 import init
from speech_recognition import Recognizer, Microphone, UnknownValueError, WaitTimeoutError

# import to response at the request of the user
from datetime import datetime
import subprocess
import json

lang = "it-It"

engine = init()
voices = engine.getProperty("voices") # get all the voices
engine.setProperty("voices", voices[0]) # set the first voice like the main one
r = Recognizer() # create the recognizer obj

# this function trasform to speech what Roberto have to say
def say(text):
    engine.say(text)
    engine.runAndWait()

# This function is to handle the request which the user can do
# and returning the right response
def replay_to_request(req):
    response = ""
    
    if "roberto" in req:
        response = "Mi dica"
    elif "ore" in req:
        response = f"sono le ore {datetime.now().strftime('%H e %M')}"
    elif "blocco note" in req:
        # Oprn the file with the paths
        with open("paths.json", "r") as f:
            percorsi = json.load(f)
        
        response = "tento di aprire il blocco note"
        subprocess.run(percorsi["blocco note"]) # open notepad++
        
    elif req == "esci":
        response = "esci"
    else:
        response = "Non posso soddisfare la tua rischiesta"

    return response

# catch the audio from the user and return it as a string
def audio_to_text(source):
    e = True
    while e:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio, language=lang).lower()
            e = False
        except UnknownValueError:
            say("Non ho capito. Poi ripetere per piacere.")
            print("Roberto non ha capito")
    
    return text

# Main loop
while True:
    with Microphone() as source:
        print("Roberto e' pronto ad ascoltare")
        
        user_audio = audio_to_text(source)
        
        if "roberto" in user_audio:
            say("Mi dica")
            print("Sto ascoltando")
            user_audio = audio_to_text(source)
            
            response = replay_to_request(user_audio)
        
            if response == "esci":
                break
            else:
                say(response)
        
        