import datetime
import pyttsx3
import speech_recognition as sr
import pyautogui as pa
import name
import tasks
import covid_tracker as ct


pa.PAUSE = 1
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voiceRate = 140
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', voiceRate)
ai = 'friday'


def speak(audio):
    '''
    Takes an argument as a string and reads it aloud
    '''
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    '''
    It reads the system time and greets you according to the hour. Then it gives it's introduction
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! sir")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon! sir")

    else:
        speak("Good Evening! sir")

    speak("Please tell me how may I help you?")


def takeCommand():
    '''
    It takes microphone input from user and returns String output
    '''
    r = sr.Recognizer()  # Helps to recognize audio
    with sr.Microphone() as source:
        print("Listening...")
        # notif("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # notif("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
        # notif(f"User said: {query}\n")

    except Exception:
        # print(Exception) #Will  print the error (not recommended)
        print("Say that again please...")
        return "None"
    return command


def activate():
    '''
    Activates jarvis to take commands from the user
    '''
    while True:
        com = takeCommand().lower()
        while True:
            if 'go to sleep' in com:
                quit()
            elif f'activate {ai}' in com:
                return
            else:
                speak("activation required")
                break


def start(query):
    '''
    start any installed windows program using your voice
    '''
    pa.press('win')
    pa.write(query)
    speak(f"Do you want to start {query}?")
    ans = takeCommand().lower()
    if ans == 'yes':
        pa.press('enter')
    else:
        speak("Okay sir")
        pa.press('esc')


def Jarvis_quit():
    '''
    Exits the program with a spoken message
    '''
    speak("Okay sir")
    exit()


if __name__ == "__main__":
    activate()
    WishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            res = tasks.searchWiki(query)
            speak("According to Wikipedia")
            speak(res)

        elif query == f'ok {ai}' or query == f'{ai}':
            speak("Yes sir!")

        elif 'who are you' in query:
            me = tasks.myself()
            speak(f'{me}')

        elif 'on youtube' in query:
            try:
                ysearch = query.replace('search', '').replace('for', '').replace(
                    ' on ', '').replace('youtube', '').replace('ok', '').replace(f'{ai}', '')
                speak("searching")
                tasks.searchYoutube(ysearch.strip())
            except Exception as e:
                print(e)

        elif 'open youtube' in query:
            tasks.openYt()

        elif 'search' in query and 'google' in query:
            try:
                # speak("What do you want me to search about?")
                # query = takeCommand().lower()
                gsearch = query.replace('search', '').replace('for', '').replace(
                    ' on ', '').replace('google', '').replace('ok', '').replace(f'{ai}', '')
                speak("searching")
                tasks.searchGoogle(gsearch.strip())
            except Exception as e:
                print(e)
                speak("Sorry sir, an error occured during your search")

        elif 'play music' in query:
            tasks.playMusic()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email' in query:
            try:
                speak("whom should I send it to sir?")
                nm = takeCommand().lower()
                nm = nm.replace('send', '').replace('it', '').replace('to', '')
                speak("What should I say?")
                message = takeCommand()
                message = message.replace('say', '').replace('that', '')
                to = name.eread(nm.strip())
                tasks.sendEmail(to, message)
                speak("Email has been sent sir")

            except Exception as e:
                speak("Could not send the specified email sir")

        elif 'open movies' in query:
            speak("Opening")
            tasks.movies()

        elif 'open google' in query:
            tasks.open_chrome()

        elif 'covid-19' in query:
            try:
                speak("which state sir ?")
                state = takeCommand()
                ct.showUpdates(state)
            except Exception as e:
                print(e)

        elif 'message' in query:
            try:
                speak("Tell me the name of the recipent sir")
                rec = takeCommand().lower()
                speak("What should I text?")
                message = takeCommand()
                to = name.numRead(rec)
                tasks.send_sms(to, message)
                speak("Your message has been delivered sir")
            except Exception as e:
                print(e)

        elif 'start' in query:
            query = query.replace('ok', '').replace(
                f'{ai}', '').replace('start', '')
            start(query.strip())

        elif 'close' in query:
            pa.moveTo(1340, 1)
            # pa.PAUSE(0.5)
            pa.click()
            pa.moveTo(683, 384)

        elif 'switch window' in query:
            pa.hotkey('altleft', 'tab')

        elif 'go to sleep' in query:
            speak("For how much time sir?")  # seconds or minutes
            time = takeCommand().lower()
            speak(f"Sleeping for {time}")
            tasks.jsleep(time)

        elif 'news' in query or 'headlines' in query:
            try:
                news = tasks.news()
                speak(news)
            except Exception as e:
                print(e)

        elif 'shutdown' in query or 'shut down' in query:
            Jarvis_quit()
