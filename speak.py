'''
Takes a string as input and "speaks" it as audio using the pyttsx3 module
'''
import pyttsx3


engine = pyttsx3.init('sapi5')
VOICES = engine.getProperty('voices')
VOICERATE = 180
engine.setProperty('voice', VOICES[1].id)
engine.setProperty('rate', VOICERATE)


def speak(audio):
    '''
    Takes an argument as a string and reads it aloud
    '''
    print(audio)
    engine.say(audio)
    engine.runAndWait()
