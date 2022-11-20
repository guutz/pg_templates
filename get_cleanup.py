import requests
from bs4 import BeautifulSoup
from auth import info_auth
from datetime import datetime
import argparse
import logging

logging.basicConfig(level=logging.INFO)

def main(cleanup=False,update=False,name="",**kwargs):
    if cleanup:
        logging.info("Fetching cleanup for %s", name)
        r = requests.get('https://www.primegrid.com/info/show_challenge_cleanup.php', auth=info_auth)
        soup = BeautifulSoup(r.content, 'html.parser')
        try:
            cleanup = soup.find('body').text.split('\n')[:-1]
            if name:
                cleanup = [x for x in cleanup if name in x]
            entry = cleanup[-1].split(':')[-1].strip()
            day = datetime.strftime(datetime.now(), '%b %d')
            if entry.count('(0)') == 2:
                logging.info("Cleanup is done for %s!", name)
                return 'EMPTY'
            logging.info("Success")
            return f'{day}: {entry}'
        except:
            logging.warn("Couldn't find anything for %s, assuming that means cleanup is done", name)
            return 'EMPTY'
    if update:
        logging.info("Fetching show_update for %s", name)
        r = requests.get('https://www.primegrid.com/info/show_update.php', auth=info_auth)
        soup = BeautifulSoup(r.content, 'html.parser')
        logging.info("Sending you just the entire page")
        return soup

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-c', '--cleanup', action='store_true')
    argparser.add_argument('-u', '--update', action='store_true')
    argparser.add_argument('-n', '--name', type=str, default='')
    args = argparser.parse_args()
    args = vars(args)
    main(**args)