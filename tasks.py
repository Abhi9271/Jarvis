import webbrowser
import os
import random
import smtplib
import time
import winsound
import wikipedia
import requests
from bs4 import BeautifulSoup
import check_process as cp
from speak import speak

CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'


def search_wiki(query):
    try:
        query = query.replace('wikipedia', '').replace('search', '').replace(
            'for', '').replace('on', '').replace('jarvis', '').replace('ok', '')
        results = wikipedia.summary(query.strip(), sentences=2)
        return results
    except Exception as caught_exception:
        print(caught_exception)


def myself():
    info_file = open('myself.txt', mode='r')
    count = len(open('myself.txt').readlines())
    read = info_file.readlines()
    desc = random.randint(0, count-1)
    return read[desc]


def play_music():
    m_dir = "C:\\Users\\Public\\Music"
    songs = os.listdir(m_dir)
    # plays a random song out of the list of all songs
    song = random.randint(0, len(songs)-1)
    os.startfile(os.path.join(m_dir, songs[song]))
    # webbrowser.open(m_dir)


def search_google(gsearch):
    if cp.checkIfProcessRunning('chrome'):
        webbrowser.get(CHROME).open(f'google.co.in/search?q={gsearch}')
    else:
        os.startfile(CHROME[:-2])
        webbrowser.get(CHROME).open_new_tab(f'google.co.in/search?q={gsearch}')


def search_youtube(ysearch):
    if cp.checkIfProcessRunning('chrome'):
        webbrowser.get(CHROME).open(
            f'youtube.com/results?search_query={ysearch}')
    else:
        os.startfile(CHROME[:-2])
        webbrowser.get(CHROME).open_new_tab(
            f'youtube.com/results?search_query={ysearch}')


def open_yt():
    if cp.checkIfProcessRunning('chrome'):
        webbrowser.get(CHROME).open('youtube.com')
    else:
        os.startfile(CHROME[:-2])
        webbrowser.get(CHROME).open_new_tab('youtube.com')


def movies():
    mov = 'C:\\Users\\Abhi\\Videos'
    webbrowser.open(mov)


def open_chrome():
    os.startfile(CHROME[:-2])


def send_email(to, message):
    '''
    sends an Email using the smtplib to a specified email address
    '''
    # enter passcode before accessing
    eid = ""
    passw = ""
    f_r = open('creds.txt')
    if f_r.mode == 'r':
        creds = f_r.readlines()
        eid = creds[0]
        passw = creds[1]
        f_r.close()
    else:
        print('File not in read mode')
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
    if 'minutes' in sec or 'minute' in sec:
        sec = sec.replace('minutes', '').replace('minute', '').strip()
        sec = int(sec)*60
    elif 'seconds' in sec or 'second' in sec:
        sec = sec.replace('seconds', '').replace('second', '').strip()
        sec = int(sec)

    time.sleep(sec)
    winsound.PlaySound("SystemDefault", winsound.SND_ALIAS)


def news():
    """ Gets 5 news headlines for the times of India and returns as a String"""
    toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
    toi_soup = BeautifulSoup(toi_r.content, 'html.parser')

    toi_headings = toi_soup.find_all('h2')

    toi_headings = toi_headings[2:6]  # 4 news headlines will be returned

    toi_news = []

    for heading in toi_headings:
        toi_news.append(heading.text)
    for news_item in toi_news:
        print(news_item)
        speak(news_item)
