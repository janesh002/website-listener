from bs4 import BeautifulSoup
import datetime
import os
import requests
from random import randint
import time

URL = "https://www.wembleystadium.com/events/2024/UEFA-Champions-League-final"
HAPPY_TEXT = 'TICKETS ARE AVAILABLE!!!'

def notify():
    while True:
        log(HAPPY_TEXT)
        os.system('say -v Bells "Beep dong Beep"')
        os.system('say %s' % HAPPY_TEXT)
        time.sleep(2)

def log(msg):
    print('%s: %s' % (datetime.datetime.now(), msg))

def poll():
    log('Started')
    
    response = requests.get(URL)
    log('Response status: %s' % response.status_code)
    
    # HTML Path : soup.main.article.section.div.ul.li.div.a.span
    soup = BeautifulSoup(response.content, "html.parser")
    element = soup.main.article.section.div.ul.li
    available = True
    disappointing_text = 'COMING SOON'
    for s in element:
        if s.text is not None:
            if disappointing_text in s.text:
                available = False
                break
    if available:
        notify()
    log('Ended')

if __name__ == "__main__":
    ctr = 0
    # notify()
    while True:
        ctr = ctr+1
        log('------------------------------------')
        log('Attempt no. %s' % ctr)
        
        # Poll
        poll()
        
        # Sleep
        sleep_int = randint(15, 70)
        log('Sleeping for %s seconds' % sleep_int)
        time.sleep(sleep_int)
