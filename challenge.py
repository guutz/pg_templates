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

def time(s):
    return datetime.now().strftime(s)

subprojects = {
    '321': {
        'short_name' : '321-LLR',
        'long_name' : '321 Prime Search (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=7945',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'deadline': 6,
    },
    'CUL': {
        'short_name' : 'CUL-LLR',
        'long_name' : 'Cullen Prime Search (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=7944',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'deadline': 14,
    },
    'ESP': {
        'short_name' : 'ESP-LLR',
        'long_name' : 'Extended Sierpinski Problem (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=5758',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'deadline': 6,
    },
    'GCW': {
        'short_name' : 'GCW-LLR',
        'long_name' : 'Generalized Cullen/Woodall Prime Search (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=7073',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'deadline': 10,
    },
    'PSP': {
        'short_name' : 'PSP-LLR',
        'long_name' : 'Prime Sierpinski Problem (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=972',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'deadline': 21,
    },
    'PPS': {
        'short_name' : 'PPS-LLR',
        'long_name' : 'Proth Prime Search (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=2665',
        'llr': True,
        'llr2': True,
        'multithread': SLOW,
        'deadline': 4,
    },
    'PPSE': {
        'short_name' : 'PPSE-LLR',
        'long_name' : 'Proth Prime Search Extended (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=2665',
        'llr': True,
        'llr2': True,
        'multithread': SLOW,
        'deadline': 4,
    },
    'MEGA': {
        'short_name' : 'PPS-MEGA',
        'long_name' : 'Proth Mega Prime Search (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=2665',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'deadline': 4,
    },
    'SOB': {
        'short_name' : 'SOB-LLR',
        'long_name' : 'Seventeen or Bust (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=1647',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'deadline': 35,
    },
    'SR5': {
        'short_name' : 'SR5-LLR',
        'long_name' : 'Siepinski/Riesel Base 5 Problem (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=5087',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'deadline': 6,
    },
    'SGS': {
        'short_name' : 'SGS-LLR',
        'long_name' : 'Sophie Germain Prime Search (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=1450',
        'llr': True,
        'llr2': False,
        'multithread': SLOW,
        'deadline': 4,
    },
    'TRP': {
        'short_name' : 'TRP-LLR',
        'long_name' : 'The Riesel Problem (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=1731',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'deadline': 6,
    },
    'WOO': {
        'short_name' : 'WOO-LLR',
        'long_name' : 'Woodall Prime Search (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=7944',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'deadline': 14, 
    },
    'AP27': {
        'short_name' : 'AP27',
        'long_name' : 'Arithmetic Progression of Primes 27',
        'url': 'https://www.primegrid.com/forum_thread.php?id=7022',
        'llr': False,
        'llr2': False,
        'multithread': YES,
        'deadline': 7,
    },
    'WW': {
        'short_name' : 'WW',
        'long_name' : 'Wieferich and Wall-Sun-Sun Prime Search',
        'url': 'https://www.primegrid.com/forum_thread.php?id=9436',
        'llr': False,
        'llr2': False,
        'multithread': YES,
        'deadline': 7,
    },
    'GFN-15': {
        'short_name' : 'GFN-15',
        'long_name' : 'Generalized Fermat Prime Search (n=15)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': NO,
        'deadline': 4,
    },
    'GFN-16': {
        'short_name' : 'GFN-16',
        'long_name' : 'Generalized Fermat Prime Search (n=16)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': YES,
        'deadline': 4,
    },
    'GFN-17': {
        'short_name' : 'GFN-17',
        'long_name' : 'Generalized Fermat Prime Search (n=17)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': YES,
        'deadline': 4,
    },
    'GFN-18': {
        'short_name' : 'GFN-18',
        'long_name' : 'Generalized Fermat Prime Search (n=18)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': YES,
        'deadline': 4,
    },
    'GFN-19': {
        'short_name' : 'GFN-19',
        'long_name' : 'Generalized Fermat Prime Search (n=19)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': YES,
        'deadline': 10,
    },
    'GFN-20': {
        'short_name' : 'GFN-20',
        'long_name' : 'Generalized Fermat Prime Search (n=20)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': YES,
        'deadline': 15,
    },
    'GFN-21': {
        'short_name' : 'GFN-21',
        'long_name' : 'Generalized Fermat Prime Search (n=21)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': YES_APP,
        'deadline': 21,
    },
    'GFN-22': {
        'short_name' : 'GFN-22',
        'long_name' : 'Generalized Fermat Prime Search (n=22)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': NO,
        'deadline': 21,
    },
    'GFN-DYFL': {
        'short_name' : 'GFN-DYFL',
        'long_name' : 'Do You Feel Lucky? (Genefer World Record Attempt)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': NO,
        'deadline': 21,
    },
}

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
        url = f'https://www.primegrid.com/challenge/{time("%Y")}_{self.number}/top_users.html'
        r1 = requests.get(url)
        soup = BeautifulSoup(r1.content, 'html.parser')
        self._users_page = soup
    
    def _get_teams_page(self):
        url = f'https://www.primegrid.com/challenge/{time("%Y")}_{self.number}/top_teams.html'
        r1 = requests.get(url)
        soup = BeautifulSoup(r1.content, 'html.parser')
        self._teams_page = soup

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
                teams.append(("https://primegrid.com"+cols[1].a['href'], cols[1].a.text.strip(), cols[4].text.strip().replace('\u202f', ',')))
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

def init_template(file):
    with open(file+'.yml', 'w+', encoding="utf-8") as f:
        f.write("""\
title: 
number: 
length: 
celebrating: 
sp: 
start_date: 
background: >-

thread: 
        """)

# I'm very sorry, i've used "template" for both the mako one and for the yaml file where you fill in the challenge info
if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--init', default=None, help='initialize template')
    argparser.add_argument('-t', '--template', default=None, help='use template')
    argparser.add_argument('-o', '--outfile', default=None, help='output file')
    argparser.add_argument('-g', '--generate', nargs='+', default=['firstpost','fullpost','newspost'], help='generate posts')
    args = argparser.parse_args()
    args = vars(args)
    if args['init']:
        init_template(args['init'])
        exit()
    elif args['template']:
        with open(args['template'], 'r', encoding="utf-8") as f:
            y = yaml.safe_load(f)
            c = challenge(**y)
    else:
        argparser.print_help()
        exit()
    if args['outfile']:
        outfile = args['outfile']
    else:
        outfile = args['template'].split('.')[0] + '.txt'
    mtl = MakoTemplateLookup(directories=["", "project_overviews/"])
    makotemplates = {
        'firstpost': mtl.get_template('firstpost.mako'),
        'fullpost': mtl.get_template('challenge.mako'),
        'newspost': mtl.get_template('newspost.mako'),
        'endpost': mtl.get_template('results_are_final.mako'),
    }
    
    for post in args['generate']:
        file = outfile.split('.')[0] + '_' + post + ('.txt' if len(outfile.split('.')) == 1 else '.' + outfile.split('.')[1])
        with open(file, 'w+', encoding="utf-8") as f:
            print(makotemplates[post].render(c=c),file=f)