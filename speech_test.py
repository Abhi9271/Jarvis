# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    print (voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

import pyttsx3
engine = pyttsx3.init('sapi5')
v = engine.getProperty('voices')
voiceRate = 145
engine.setProperty('voice', v[0].id)
print(v[0].id)
engine.setProperty('rate', voiceRate)
engine.say(
    'This is echo 3 1 in the blind. I have 2 tangos in sight. Requesting permission to engage')
# engine.say('Good afternoon!!')
engine.runAndWait()
