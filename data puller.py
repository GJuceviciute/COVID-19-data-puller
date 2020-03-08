# corona virus data from https://www.worldometers.info/coronavirus/
# saves the website as html every 1 minute


import urllib.request
from datetime import datetime
import time
import os

WEB = 'https://www.worldometers.info/coronavirus/'
TIME = 1  # minutes between requests
DIR = 'data'


def pull_data():
    html = urllib.request.urlopen(WEB)
    now = datetime.now().strftime('%Y-%d-%m %H%M%S')
    filename = 'data ' + now + '.html'
    with open(os.path.join(DIR, filename), 'w') as f:
        for line in html:
            f.write(str(line))


def main():
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    while True:
        pull_data()
        time.sleep(60*TIME)


main()
