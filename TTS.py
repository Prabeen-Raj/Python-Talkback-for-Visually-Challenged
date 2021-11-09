from pynput.keyboard import Key, Listener
import pyttsx3

def show(key):
    tts = pyttsx3.init()
    tts.setProperty('rate',180)
    tts.say(key)
    tts.runAndWait()
       
with Listener(on_press=show) as listener:
     listener.join()