import argparse
from bs4 import BeautifulSoup
import requests
from mako.lookup import TemplateLookup as MakoTemplateLookup
from datetime import datetime, timedelta
import yaml

YES = 'yes'
NO = 'no'
SLOW = 'slow'
YES_APP = 'yes_app'
CPU = 'CPU'
GPU = 'GPU'

subprojects = yaml.safe_load(open('subprojects.yaml', 'r', encoding="utf-8"))

def time(s):
    return datetime.now().strftime(s)

def update_challenge_yaml():
    r = requests.get('https://www.primegrid.com/challenge/challenge.php')
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find(id='table4')
    rows = table.find_all('tr')
    master_list = []
    for tr in rows[2:-2]:
        l=[]
        for td in list(tr)[:-1]:
            l.append(td.text if hasattr(td, 'text') else td)
        master_list.append(l)
    try:
        with open(f"challenges{time('%Y')}.yaml", 'r') as f:
            dump_list = yaml.load(f, Loader=yaml.FullLoader)
    except:
        dump_list = []
    for i, ch in enumerate(master_list):
        d=dump_list[i] if i < len(dump_list) else {}
        d['number'] = int(ch[0])
        d['start_time'] = datetime.strptime(f"{ch[1].split('-')[0]} {ch[1].split(' ')[-1]} {ch[2]}", '%d %B %H:%M:%S').strftime('%m/%d %H:%M')
        for sp in subprojects.keys():
            if sp in ch[3]:
                d['sp'] = sp
                break
        d['title'] = ch[4]
        d['length'] = int(ch[5].split(' ')[0])
        d['celebrating'] = d['background'] = d['thread'] = "a"
        d['updates'] = {
            'first': False,
            'second': False,
            'news': False,
            'stats': False,
            'cleanup': False,
            'results': False
        } if 'updates' not in d.keys() else d['updates']
        dump_list[i] = d
    with open(f"challenges{time('%Y')}.yaml", 'w') as f:
        yaml.dump(dump_list, f, default_flow_style=False)
    return dump_list

def get_needed_updates():
    now = datetime.now()

    def challenge_timeline(ch):
        start = datetime.strptime(f"{ch['start_time']} {time('%Y')}", '%m/%d %H:%M %Y')
        return dict(
            # the dates after which we need to worry about each item
            first = start - timedelta(weeks=2),
            second = start - timedelta(weeks=1),
            news = start - timedelta(days=3),
            stats = start + timedelta(days=1),
            end_reminder = start + timedelta(days=ch['length'] - 1),
            cleanup = start + timedelta(days=ch['length']),
            results = start + timedelta(days=ch['length']),
        )

    ups = {
        'first': [],
        'second': [],
        'news': [],
        'stats': [],
        'cleanup': [],
        'results': []
    }

    for ch in update_challenge_yaml():
        t = challenge_timeline(ch)
        for u in ch['updates']:
            if ch['updates'][u] == False and now > t[u]:
                ups[u].append(ch['title'])



class challenge:

    ths = {
        1: 'first',
        2: 'second',
        3: 'third',
        4: 'fourth',
        5: 'fifth',
        6: 'sixth',
        7: 'seventh',
        8: 'eighth',
        9: 'ninth and final',
    }

    class subproject:
        def __init__(self, name):
            self.name = name
            for key, value in subprojects[name].items():
                setattr(self, key, value)
        
        @property
        def cpu_time(self):
            hms = self.get_time(CPU).split(':')
            if int(hms[0]) == 0:
                return f"{hms[1].strip('0')} minutes"
            if int(hms[0]) < 48:
                return f"{hms[0].strip('0')} hours"
            if int(hms[0]) < 24*13:
                return f"{int(hms[0])//24} days"
            return f"{int(hms[0])//168} weeks"
                
        @property
        def gpu_time(self):
            hms = self.get_time(GPU).split(':')
            if int(hms[0]) == 0:
                return f"{hms[1].strip('0')} minutes"
            if int(hms[0]) < 48:
                return f"{hms[0].strip('0')} hours"
            if int(hms[0]) < 24*13:
                return f"{int(hms[0])//24} days"
            return f"{int(hms[0])//168} weeks"

        def _get_prefs_page(self):     
            from auth import strong_key
            url = 'https://www.primegrid.com/prefs_edit.php?subset=project&cols=1'
            cookies = {'auth': strong_key}
            r = requests.get(url, cookies=cookies)
            soup = BeautifulSoup(r.content, 'html.parser')
            self._prefs_page = soup
        
        def get_time(self, type=CPU):
            if not hasattr(self, '_prefs_page'):
                self._get_prefs_page()
            notes = self._prefs_page.find_all("div", class_="note")
            timestr = ''
            for note in notes:
                project = note.parent.find("a")
                if project and self.name in project.text:
                    timestr = note.find(string=lambda text: text and f"Recent average {type} time" in text)
            if timestr:
                return timestr.strip()[len(f"Recent average {type} time: "):]
            return None
            

    def __init__(self, title, number, length, celebrating, sp, start_date, background, thread=None):
        self.title = title if "'s" in title else "the "+title
        self.number_int = number
        self.number = self.ths[number]
        self.length = length
        self.celebrating = celebrating
        self.sp = self.subproject(sp)
        self._start_time_object = datetime.strptime(start_date, '%m/%d %H:%M')
        self._end_time_object = self._start_time_object + timedelta(days=self.length)
        self.start = self._start_time_object.strftime('%d %B %H:%M UTC')
        self.end = self._end_time_object.strftime('%d %B %H:%M UTC')
        self.background = background
        self.thread = thread

    def _get_users_page(self):
        url = f'https://www.primegrid.com/challenge/{time("%Y")}_{self.number_int}/top_users.html'
        r1 = requests.get(url)
        soup = BeautifulSoup(r1.content, 'html.parser')
        self._users_page = soup
    
    def _get_teams_page(self):
        url = f'https://www.primegrid.com/challenge/{time("%Y")}_{self.number_int}/top_teams.html'
        r1 = requests.get(url)
        soup = BeautifulSoup(r1.content, 'html.parser')
        self._teams_page = soup
    
    def _get_primes_page(self):
        # TODO: add primepage abbreviation field to subproject dict
        url = f'https://www.primegrid.com/primes/primes.php?project={self.sp.abbrv}'

    @property
    def total_tasks_done(self):
        if not hasattr(self, '_users_page'):
            self._get_users_page()
        table = self._users_page.find('table')
        rows = table.find_all('tr')
        sum = 0
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            if len(cols) > 0:
                sum += int(cols[4].replace('\u202f', ''))
        return sum

    @property
    def top_3_users(self):
        if not hasattr(self, '_users_page'):
            self._get_users_page()
        table = self._users_page.find('table')
        rows = table.find_all('tr')
        users = []
        for row in rows:
            cols = row.find_all('td')
            cols = [ele for ele in cols if cols[0].text.strip() in ['1', '2', '3']]
            if cols:
                users.append(("https://primegrid.com"+cols[1].a['href'], cols[1].a.text.strip(), cols[4].text.strip().replace('\u202f', ',')))
        return users

    @property
    def top_3_teams(self):
        if not hasattr(self, '_teams_page'):
            self._get_teams_page()
        table = self._teams_page.find('table')
        rows = table.find_all('tr')
        teams = []
        for row in rows:
            cols = row.find_all('td')
            cols = [ele for ele in cols if cols[0].text.strip() in ['1', '2', '3']]
            if cols:
                teams.append(("https://primegrid.com"+cols[1].a['href'], cols[1].a.text.strip(), cols[3].text.strip().replace('\u202f', ',')))
        return teams

    @property
    def total_users(self):
        if not hasattr(self, '_users_page'):
            self._get_users_page()
        table = self._users_page.find('table')
        rows = table.find_all('tr')
        return len(rows)-1

    @property
    def total_teams(self):
        if not hasattr(self, '_teams_page'):
            self._get_teams_page()
        table = self._teams_page.find('table')
        rows = table.find_all('tr')
        return len(rows)-1

# I'm very sorry, i've used "template" for both the mako one and for the yaml file where you fill in the challenge info
def main(init=False,template="",outfile=None,posts=[],**kwargs):
    if init:
        update_challenge_yaml()
        exit()
    if template:
        with open(template, 'r', encoding="utf-8") as f:
            y = yaml.safe_load(f)
            c = challenge(**y)
    if not outfile:
        outfile = template.split('.')[0] + '.txt'
    mtl = MakoTemplateLookup(directories=["", "project_overviews/", "templates/"])
    
    for post in posts:
        file = outfile.split('.')[0] + '_' + post + ('.txt' if len(outfile.split('.')) == 1 else '.' + outfile.split('.')[1])
        with open(file, 'w+', encoding="utf-8") as f:
            print(mtl.get_template(post+".mako").render(c=c),file=f)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--init', default=None, help='initialize template')
    argparser.add_argument('-t', '--template', default=None, help='use template')
    argparser.add_argument('-o', '--outfile', default=None, help='output file')
    argparser.add_argument('-p', '--posts', nargs='+', default=['firstpost','fullpost','newspost'], help='generate posts')
    args = argparser.parse_args()
    args = vars(args)
    main(**args)