'''
Real-eorld Example: Multithreading for I/O bound Tasks

Scenario: web Scraping
web scraping often involves making numerous network requests to 
fetch web pages. these tasks are I/O-bound because they spend a lot oftime waiting for responses from servers.
Multithreading can significantly imporove the performance by allowing multiple web pages to be fetched concurrently.
'''
'''
https://docs.python.org/3/library/threading.html
https://www.geeksforgeeks.org/machine-learning/machine-learning/
https://www.ibm.com/think/topics/artificial-intelligence
'''

import threading
import requests 
from bs4 import BeautifulSoup 

urls=[
    'https://docs.python.org/3/library/threading.html',
    'https://www.geeksforgeeks.org/machine-learning/machine-learning/',
    'https://www.ibm.com/think/topics/artificial-intelligence'
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetch {len(soup.text)}')

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('All web pages fetched')

'''
OutPut:
Fetch 10036
Fetch 47303
Fetch 31617
All web pages fetched
'''