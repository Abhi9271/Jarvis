import webbrowser
import os
import random
import smtplib
import time
import winsound
import wikipedia
import requests
import pyjokes
from bs4 import BeautifulSoup
import check_process as cp
from speak import speak
BROWSER = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'


def search_wiki(wiki_search):
    try:
        results = wikipedia.summary(wiki_search, sentences=2)
        return results
    except Exception as caught_exception:
        print(caught_exception)


def myself():
    info_file = open('myself.txt', mode='r')
    count = len(open('myself.txt').readlines())
    read = info_file.readlines()
    desc = random.randint(0, count-1)
    stmt = read[desc]
    info_file.close()
    return stmt


def play_music():
    m_dir = "C:\\Users\\Public\\Music\\Sample Music"
    songs = os.listdir(m_dir)
    song_list = []
    for song in songs:
        if song.endswith('mp3'):
            song_list.append(song)
    selection = random.randint(0, len(song_list)-1)
    os.startfile(os.path.join(m_dir, song_list[selection]))


def search_google(gsearch):
    if cp.checkIfProcessRunning('chrome'):
        webbrowser.get(BROWSER).open(f'google.co.in/search?q={gsearch}')
    else:
        os.startfile(BROWSER[:-2])
        webbrowser.get(BROWSER).open_new_tab(f'google.co.in/search?q={gsearch}')


def search_youtube(ysearch):
    if cp.checkIfProcessRunning('chrome'):
        webbrowser.get(BROWSER).open(
            f'youtube.com/results?search_query={ysearch}')
    else:
        os.startfile(BROWSER[:-2])
        webbrowser.get(BROWSER).open_new_tab(
            f'youtube.com/results?search_query={ysearch}')


def open_yt():
    if cp.checkIfProcessRunning('chrome'):
        webbrowser.get(BROWSER).open('youtube.com')
    else:
        os.startfile(BROWSER[:-2])
        webbrowser.get(BROWSER).open_new_tab('youtube.com')


def movies():
    mov = 'D:\\Videos\\Movies'
    webbrowser.open(mov)


def open_browser():
    os.startfile(BROWSER[:-2])


def send_email(to, message):
    '''
    sends an Email using the smtplib to a specified email address
    '''
    # enter passcode before accessing
    eid = ""
    passw = ""
    f_r = open('creds.txt', mode='r')
    creds = f_r.readlines()
    eid = creds[0]
    passw = creds[1]
    f_r.close()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(eid, passw)  # id and password are stored in a text file
    server.sendmail(eid, to, message)
    server.close()


def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'wJvZq296cxCg5TPUIk41RzBeO8iflQ0WKhFEoSdGHujabAVyNMCOz3sJcqn0jw2d5vY8RIhfEtm9VPgo',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    resp = response.json()
    print(resp)


def jsleep(sec):
    """
    Makes the assistant suspend operations for a period of time as defined by the user
    Converts time in minutes to seconds and then uses the time.sleep()
    method to temporarily suspend the program process
    """
    if 'minutes' in sec or 'minute' in sec:
        sec = sec.replace('minutes', '').replace('minute', '').strip()
        sec = int(sec)*60
    elif 'seconds' in sec or 'second' in sec:
        sec = sec.replace('seconds', '').replace('second', '').strip()
        sec = int(sec)

    time.sleep(sec)
    winsound.PlaySound("SystemDefault", winsound.SND_ALIAS)


def news():
    """ Gets 5 news headlines from the Times of India website and returns as a String"""
    toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
    toi_soup = BeautifulSoup(toi_r.content, 'html.parser')

    toi_headings = toi_soup.find_all('h2')

    toi_headings = toi_headings[2:6]  # 4 news headlines will be returned

    toi_news = []

    for heading in toi_headings:
        toi_news.append(heading.text)
    for news_item in toi_news:
        speak(news_item)


def get_ip():
    """
    Gets the IP address of the network connected to the system
    """
    ip_addr = requests.get('https://api.ipify.org').text
    speak(f"Your IP Address is: {ip_addr}.")


def close(app):
    os.system(f"taskkill /f /im {app}.exe")


def jokes():
    '''
    Uses the pyjokes module to read out programming jokes
    '''
    joke = pyjokes.get_joke()
    speak(joke)


def todo_list():
    os.startfile(".\\todolist.html")


def power_down():
    """
    Turns off the computer using the os module
    """
    os.system("shutdown /s /t 5")
