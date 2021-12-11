import datetime
import sys
import speech_recognition as sr
import pyautogui as pa
import name
import tasks
from speak import speak


pa.PAUSE = 1
AI = 'friday'


def activate():
    '''
    Activates jarvis to take commands from the user
    '''
    while True:
        com = take_command().lower()
        while True:
            if 'go to sleep' in com:
                quit()
            elif f'activate {AI}' in com:
                return
            else:
                speak("activation required")
                break


def wish_me():
    '''
    It reads the system time and greets you according to the hour. Then it gives it's introduction
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")

    speak("Please tell me how may I help you?")


def take_command():
    '''
    It takes microphone input from user and returns String output
    '''
    rec_audio = sr.Recognizer()  # Helps to recognize audio
    with sr.Microphone() as source:
        print("Listening...")
        # notif("Listening...")
        rec_audio.pause_threshold = 1
        rec_audio.energy_threshold = 450
        audio = rec_audio.listen(source)

    try:
        print("Recognizing...")
        # notif("Recognizing...")
        command = rec_audio.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
        # notif(f"User said: {query}\n")

    except Exception:
        # print(Exception) #Will  print the error (not recommended)
        print("Say that again please...")
        return "None"
    return command


def start(stmt):
    '''
    start any installed windows program using your voice
    '''
    pa.press('win')
    pa.write(stmt)
    pa.press('enter')


def prog_quit():
    '''
    Exits the program with a spoken message
    '''
    speak("Okay sir")
    sys.exit()


if __name__ == "__main__":
    activate()
    wish_me()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            res = tasks.search_wiki(query)
            speak("According to Wikipedia")
            speak(res)

        elif query == f'ok {AI}' or query == f'{AI}':
            speak("Yes sir!")

        elif 'who are you' in query:
            me = tasks.myself()
            speak(f'{me}')

        elif 'on youtube' in query:
            try:
                ysearch = query.replace('search', '').replace('for', '').replace(
                    ' on ', '').replace('youtube', '').replace('ok', '').replace(f'{AI}', '')
                speak("searching")
                tasks.search_youtube(ysearch.strip())
            except Exception as caught_exception:
                print(caught_exception)

        elif 'open youtube' in query:
            tasks.open_yt()

        elif 'search' in query and 'google' in query:
            try:
                gsearch = query.replace('search', '').replace('for', '').replace(
                    ' on ', '').replace('google', '').replace('ok', '').replace(f'{AI}', '')
                speak("searching")
                tasks.search_google(gsearch.strip())
            except Exception as caught_exception:
                print(caught_exception)
                speak("Sorry sir, an error occured during your search")

        elif 'play music' in query:
            tasks.play_music()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email' in query:
            try:
                speak("whom should I send it to sir?")
                nm = take_command().lower()
                nm = nm.replace('send', '').replace('it', '').replace('to', '')
                speak("What should I say?")
                message = take_command()
                message = message.replace('say', '').replace('that', '')
                to = name.eread(nm.strip())
                tasks.send_email(to, message)
                speak("Email has been sent sir")

            except Exception as caught_exception:
                speak("Could not send the specified email sir")

        elif 'open movies' in query:
            speak("Opening")
            tasks.movies()

        elif 'open google' in query:
            tasks.open_chrome()

        # elif 'covid-19' in query:
        #     try:
        #         speak("which state sir ?")
        #         state = takeCommand()
        #         ct.showUpdates(state)
        #     except Exception as e:
        #         print(e)

        elif 'message' in query:
            try:
                speak("Tell me the name of the recipent sir")
                rec = take_command().lower()
                speak("What should I text?")
                message = take_command()
                to = name.numRead(rec)
                tasks.send_sms(to, message)
                speak("Your message has been delivered sir")
            except Exception as caught_exception:
                print(caught_exception)

        elif 'start' in query:
            query = query.replace('ok', '').replace(
                f'{AI}', '').replace('start', '')
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
            time = take_command().lower()
            speak(f"Sleeping for {time}")
            tasks.jsleep(time)

        elif 'news' in query or 'headlines' in query:
            try:
                tasks.news()
            except Exception as caught_exception:
                print(caught_exception)

        elif 'shutdown' in query or 'shut down' in query:
            prog_quit()
