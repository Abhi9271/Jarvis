from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
import assistant


def notifyMe(title, message):
    '''
    It describes the title and content of the notification displayed
    '''
    notification.notify(
        title=title,
        message=message,
        app_icon="icon.ico",
        timeout=6
    )


def getData(url):
    '''
    Retrieves data from a particular website
    '''
    r = requests.get(url)
    return r.text


def showUpdates(state):
    '''
    It displays data in the form of notification to the user according to the input
    '''
    myHtmlData = getData('https://www.mohfw.gov.in/')

    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup.prettify())
    myDataStr = ""
    for tr in soup.find_all('tr'):
        myDataStr += tr.get_text()
    #myDataStr = myDataStr[1:]
    itemList = myDataStr.split("\n\n")

    states = [f'{state}']
    # states=['Rajasthan']

    for item in itemList[1:34]:
        dataList = item.split('\n')
        # print(dataList)
        if dataList[1] in states:
            # print(dataList)
            nTitle = 'Cases of covid - 19'
            nText = f"State: {dataList[1]}\nTotal Cases: {dataList[2]}\nCured: {dataList[3]}\nDeaths: {dataList[4]}"
            notifyMe(nTitle, nText)
            assistant.speak(f"Cases of covid-19 in {state}")
            assistant.speak(
                f"Total Cases: {dataList[2]}, Cured: {dataList[3]}, Deaths: {dataList[4]}")
            time.sleep(2)

# if __name__ == "__main__":
#     showUpdates()
