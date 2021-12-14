import datetime
import time
import sys
import re
import speech_recognition as sr
import pyautogui as pa
from pywhatkit import playonyt
import name
import tasks
from speak import speak


pa.PAUSE = 1
AI = 'friday'


def activate():
    '''
    Activates the assistant to take commands from the user
    '''
    hotwords = ['shutdown', 'shut down',
                f'hey {AI}', f'hi {AI}', f'ok {AI}', f'wake up {AI}', f'activate {AI}']
    while True:
        com = take_command().lower()
        for i in range(2, len(hotwords)):
            if com in hotwords[i]:
                return
        if com in (hotwords[0], hotwords[1]):
            prog_quit()
        else:
            speak("activation required")


def wish_me():
    '''
    It reads the system time and greets you according to the hour. Then it gives it's introduction
    '''
    hour = int(datetime.datetime.now().hour)
    cur_time = time.strftime("%I:%M %p")
    if hour in range(0, 12):
        speak(f"Good Morning sir. It's {cur_time}")

    elif hour in range(12, 16):
        speak(f"Good Afternoon sir. It's {cur_time}")

    else:
        speak(f"Good Evening sir. It's {cur_time}")

    speak("Please tell me how may I help you?")


def take_command():
    '''
    It takes microphone input from user and returns String output
    '''
    rec_audio = sr.Recognizer()  # Helps to recognize audio
    with sr.Microphone() as source:
        print("Listening...")
        rec_audio.pause_threshold = 1
        rec_audio.energy_threshold = 420
        try:
            audio = rec_audio.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("Say that again please...")
            return "None"

    try:
        print("Recognizing...")
        command = rec_audio.recognize_google(audio, language='en-IN')
        print(f"User said: {command}\n")

    except Exception:
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
    REPLACEMENTS = {'ok': '', f'{AI}': '', 'search': '', 'for': '',
                    'on': '', 'google': '', 'youtube': '', 'wikipedia': '', 'close': ''}
    activate()
    wish_me()
    while True:
        query = take_command().lower()
        if query is not None:
            if 'wikipedia' in query:
                rep = dict((re.escape(k), v) for k, v in REPLACEMENTS.items())
                pattern = re.compile("|".join(rep.keys()))
                wiki_search = pattern.sub(
                    lambda m: rep[re.escape(m.group(0))], query)
                speak('Searching Wikipedia...')
                res = tasks.search_wiki(wiki_search.strip())
                speak("According to Wikipedia")
                speak(res)

            elif query == f'ok {AI}' or query == f'{AI}':
                speak("Yes sir!")

            elif 'who are you' in query:
                me = tasks.myself()
                speak(f'{me}')

            elif 'play music on youtube' in query:
                speak('What do you wanna listen?')
                y_play = take_command().lower()
                playonyt(y_play)

            elif 'on youtube' in query:
                try:
                    rep = dict((re.escape(k), v)
                               for k, v in REPLACEMENTS.items())
                    pattern = re.compile("|".join(rep.keys()))
                    ysearch = pattern.sub(
                        lambda m: rep[re.escape(m.group(0))], query)
                    speak("searching")
                    tasks.search_youtube(ysearch.strip())
                except Exception as caught_exception:
                    print(caught_exception)

            elif 'open youtube' in query:
                tasks.open_yt()

            elif 'search' in query and 'google' in query:
                try:
                    rep = dict((re.escape(k), v)
                               for k, v in REPLACEMENTS.items())
                    pattern = re.compile("|".join(rep.keys()))
                    g_search = pattern.sub(
                        lambda m: rep[re.escape(m.group(0))], query)
                    speak("searching")
                    tasks.search_google(g_search.strip())
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
                    nm = nm.replace('send', '').replace(
                        'it', '').replace('to', '')
                    # speak("Would you like to add an attachment?")
                    # choice = take_command()
                    # # if 'yes' in query:
                    # #     # speak("What should I write as the subject?")
                    # #     # sub = take_command().lower()
                    # #     # speak("What should I write in the body?")
                    # #     # message = take_command().lower()
                    # #     # file_location = input(r"Enter file path here(Use \\): ")

                    # if 'no' in query:
                    speak("Okay, what should I text?")
                    message = take_command().lower()
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

            elif 'message' in query:
                try:
                    speak("Tell me the name of the recipent sir")
                    rec = take_command().lower()
                    speak("What should I text?")
                    message = take_command()
                    to = name.num_read(rec)
                    tasks.send_sms(to, message)
                    speak("Your message has been delivered sir")
                except Exception as caught_exception:
                    print(caught_exception)

            elif 'start' in query:
                query = query.replace('ok', '').replace(
                    f'{AI}', '').replace('start', '')
                start(query.strip())

            elif 'close this window' in query:
                pa.moveTo(1340, 1)
                # pa.PAUSE(0.5)
                pa.click()
                pa.moveTo(683, 384)

            elif 'close' in query:
                rep = dict((re.escape(k), v) for k, v in REPLACEMENTS.items())
                pattern = re.compile("|".join(rep.keys()))
                app = pattern.sub(
                    lambda m: rep[re.escape(m.group(0))], query)
                tasks.close(app.strip().lower())

            elif 'switch window' in query:
                pa.keyDown('altleft')
                pa.press('tab')
                pa.keyUp('altleft')

            elif 'tell me a joke' in query:
                tasks.jokes()

            elif 'go to sleep' in query:
                speak("For how much time sir?")  # seconds or minutes
                time = take_command().lower()
                if "cancel" in time or "none" in time:
                    continue
                speak(f"Sleeping for {time}")
                tasks.jsleep(time)

            elif 'news' in query or 'headlines' in query:
                try:
                    tasks.news()
                except Exception as caught_exception:
                    print(caught_exception)

            elif 'ip address' in query:
                tasks.get_ip()

            elif 'powerdown' in query or 'power down' in query:
                tasks.power_down()
                sys.exit()

            elif 'shutdown' in query or 'shut down' in query:
                prog_quit()

        # elif 'covid-19' in query:
        #     try:
        #         speak("which state sir ?")
        #         state = takeCommand()
        #         ct.showUpdates(state)
        #     except Exception as e:
        #         print(e)
