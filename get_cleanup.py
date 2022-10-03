import requests
from bs4 import BeautifulSoup
from auth import info_auth
from datetime import datetime
r = requests.get('https://www.primegrid.com/info/show_challenge_cleanup.php', auth=info_auth)
soup = BeautifulSoup(r.content, 'html.parser')
cleanup = soup.find('body').text.split('\n')[-2].split(':')[-1].strip()
day = datetime.strftime(datetime.now(), '%b %d')
print(f'{day}: {cleanup}')