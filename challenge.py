
from bs4 import BeautifulSoup
import requests
from mako.lookup import TemplateLookup
from datetime import datetime, timedelta
from auth import strong_key

YES = 'yes'
NO = 'no'
SLOW = 'slow'
YES_APP = 'yes_app'
CPU = 'CPU'
GPU = 'GPU'

url = 'https://www.primegrid.com/prefs_edit.php?subset=project&cols=1'
cookies = {'auth': strong_key}
r = requests.get(url, cookies=cookies)
soup = BeautifulSoup(r.content, 'html.parser')
notes = soup.find_all("div", class_="note")

def request_avg_time(sp: str, type=CPU):
    global notes
    timestr = ''
    for note in notes:
        project = note.parent.find("a")
        if project and sp in project.text:
            timestr = note.find(string=lambda text: text and f"Recent average {type} time" in text)
    if timestr:
        return timestr.strip()[len(f"Recent average {type} time: "):]
    return None

subprojects = {
    '321': {
        'short_name' : '321-LLR',
        'long_name' : '321 Prime Search (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=7945',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'cpu_time': request_avg_time('321'),
        'gpu_time': None,
        'deadline': 6,
    },
    'CUL': {
        'short_name' : 'CUL-LLR',
        'long_name' : 'Cullen Prime Search (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=7944',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'cpu_time': request_avg_time('CUL'),
        'gpu_time': None,
        'deadline': 14,
    },
    'ESP': {
        'short_name' : 'ESP-LLR',
        'long_name' : 'Extended Sierpinski Problem (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=5758',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'cpu_time': request_avg_time('ESP'),
        'gpu_time': None,
        'deadline': 6,
    },
    'GCW': {
        'short_name' : 'GCW-LLR',
        'long_name' : 'Generalized Cullen/Woodall Prime Search (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=7073',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'cpu_time': request_avg_time('GCW'),
        'gpu_time': None,
        'deadline': 10,
    },
    'PSP': {
        'short_name' : 'PSP-LLR',
        'long_name' : 'Prime Sierpinski Problem (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=972',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'cpu_time': request_avg_time('PSP'),
        'gpu_time': None,
        'deadline': 21,
    },
    'PPS': {
        'short_name' : 'PPS-LLR',
        'long_name' : 'Proth Prime Search (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=2665',
        'llr': True,
        'llr2': True,
        'multithread': SLOW,
        'cpu_time': request_avg_time('PPS'),
        'gpu_time': None,
        'deadline': 4,
    },
    'PPSE': {
        'short_name' : 'PPSE-LLR',
        'long_name' : 'Proth Prime Search Extended (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=2665',
        'llr': True,
        'llr2': True,
        'multithread': SLOW,
        'cpu_time': request_avg_time('PPSE'),
        'gpu_time': None,
        'deadline': 4,
    },
    'MEGA': {
        'short_name' : 'PPS-MEGA',
        'long_name' : 'Proth Mega Prime Search (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=2665',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'cpu_time': request_avg_time('MEGA'),
        'gpu_time': None,
        'deadline': 4,
    },
    'SOB': {
        'short_name' : 'SOB-LLR',
        'long_name' : 'Seventeen or Bust (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=1647',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'cpu_time': request_avg_time('SOB'),
        'gpu_time': None,
        'deadline': 35,
    },
    'SR5': {
        'short_name' : 'SR5-LLR',
        'long_name' : 'Siepinski/Riesel Base 5 Problem (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=5087',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'cpu_time': request_avg_time('SR5'),
        'gpu_time': None,
        'deadline': 6,
    },
    'SGS': {
        'short_name' : 'SGS-LLR',
        'long_name' : 'Sophie Germain Prime Search (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=1450',
        'llr': True,
        'llr2': False,
        'multithread': SLOW,
        'cpu_time': request_avg_time('SGS'),
        'gpu_time': None,
        'deadline': 4,
    },
    'TRP': {
        'short_name' : 'TRP-LLR',
        'long_name' : 'The Riesel Problem (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=1731',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'cpu_time': request_avg_time('TRP'),
        'gpu_time': None,
        'deadline': 6,
    },
    'WOO': {
        'short_name' : 'WOO-LLR',
        'long_name' : 'Woodall Prime Search (LLR)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=7944',
        'llr': True,
        'llr2': True,
        'multithread': YES,
        'cpu_time': request_avg_time('WOO'),
        'gpu_time': None,
        'deadline': 14, 
    },
    'AP27': {
        'short_name' : 'AP27',
        'long_name' : 'Arithmetic Progression of Primes 27',
        'url': 'https://www.primegrid.com/forum_thread.php?id=7022',
        'llr': False,
        'llr2': False,
        'multithread': YES,
        'cpu_time': request_avg_time('AP27'),
        'gpu_time': request_avg_time('AP27', type=GPU),
        'deadline': 7,
    },
    'WW': {
        'short_name' : 'WW',
        'long_name' : 'Wieferich and Wall-Sun-Sun Prime Search',
        'url': 'https://www.primegrid.com/forum_thread.php?id=9436',
        'llr': False,
        'llr2': False,
        'multithread': YES,
        'cpu_time': request_avg_time('WW'),
        'gpu_time': request_avg_time('WW', type=GPU),
        'deadline': 7,
    },
    'GFN-15': {
        'short_name' : 'GFN-15',
        'long_name' : 'Generalized Fermat Prime Search (n=15)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': NO,
        'cpu_time': None,
        'gpu_time': request_avg_time('GFN-15', type=GPU),
        'deadline': 4,
    },
    'GFN-16': {
        'short_name' : 'GFN-16',
        'long_name' : 'Generalized Fermat Prime Search (n=16)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': YES,
        'cpu_time': request_avg_time('GFN-16'),
        'gpu_time': request_avg_time('GFN-16', type=GPU),
        'deadline': 4,
    },
    'GFN-17': {
        'short_name' : 'GFN-17',
        'long_name' : 'Generalized Fermat Prime Search (n=17)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': YES,
        'cpu_time': request_avg_time('GFN-17'),
        'gpu_time': request_avg_time('GFN-17', type=GPU),
        'deadline': 4,
    },
    'GFN-18': {
        'short_name' : 'GFN-18',
        'long_name' : 'Generalized Fermat Prime Search (n=18)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': YES,
        'cpu_time': request_avg_time('GFN-18'),
        'gpu_time': request_avg_time('GFN-18', type=GPU),
        'deadline': 4,
    },
    'GFN-19': {
        'short_name' : 'GFN-19',
        'long_name' : 'Generalized Fermat Prime Search (n=19)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': YES,
        'cpu_time': request_avg_time('GFN-19'),
        'gpu_time': request_avg_time('GFN-19', type=GPU),
        'deadline': 10,
    },
    'GFN-20': {
        'short_name' : 'GFN-20',
        'long_name' : 'Generalized Fermat Prime Search (n=20)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': YES,
        'cpu_time': request_avg_time('GFN-20'),
        'gpu_time': request_avg_time('GFN-20', type=GPU),
        'deadline': 15,
    },
    'GFN-21': {
        'short_name' : 'GFN-21',
        'long_name' : 'Generalized Fermat Prime Search (n=21)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': YES_APP,
        'cpu_time': request_avg_time('GFN-21'),
        'gpu_time': request_avg_time('GFN-21', type=GPU),
        'deadline': 21,
    },
    'GFN-22': {
        'short_name' : 'GFN-22',
        'long_name' : 'Generalized Fermat Prime Search (n=22)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': NO,
        'cpu_time': None,
        'gpu_time': request_avg_time('GFN-22', type=GPU),
        'deadline': 21,
    },
    'GFN-DYFL': {
        'short_name' : 'GFN-DYFL',
        'long_name' : 'Do You Feel Lucky? (Genefer World Record Attempt)',
        'url': 'https://www.primegrid.com/forum_thread.php?id=3980',
        'llr': False,
        'llr2': False,
        'multithread': NO,
        'cpu_time': None,
        'gpu_time': request_avg_time('Lucky?', type=GPU),
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
            hms = self._cpu_time.split(':')
            if int(hms[0]) == 0:
                return f"{hms[1].strip('0')} minutes"
            if int(hms[0]) < 48:
                return f"{hms[0].strip('0')} hours"
            if int(hms[0]) < 24*13:
                return f"{int(hms[0])//24} days"
            return f"{int(hms[0])//168} weeks"
        
        @cpu_time.setter
        def cpu_time(self, value):
            self._cpu_time = value
                
        @property
        def gpu_time(self):
            hms = self._gpu_time.split(':')
            if int(hms[0]) == 0:
                return f"{hms[1].strip('0')} minutes"
            if int(hms[0]) < 48:
                return f"{hms[0].strip('0')} hours"
            if int(hms[0]) < 24*13:
                return f"{int(hms[0])//24} days"
            return f"{int(hms[0])//168} weeks"
        
        @gpu_time.setter
        def gpu_time(self, value):
            self._gpu_time = value

    def __init__(self, title, number, length, celebrating, sp, start_day, time, background):
        self.title = title
        self.number = self.ths[number]
        self.length = length
        self.celebrating = celebrating
        self.sp = self.subproject(sp)
        self._start_time_object = datetime.strptime(start_day+' '+time, '%m/%d %H:%M')
        self._end_time_object = self._start_time_object + timedelta(days=self.length)
        self.start = self._start_time_object.strftime('%d %B %H:%M UTC')
        self.end = self._end_time_object.strftime('%d %B %H:%M UTC')
        self.background = background

c = challenge(
    'the World Space Week',
    6,
    7,
    'in celebration of world space week!',
    'TRP',
    '10/4',
    '12:00',
    'It\'s World Space Week!'
)

if __name__ == '__main__':
    tl = TemplateLookup(directories=["", "project_overviews/"])
    t = tl.get_template('challenge.mako')
    with open("wsw.txt", 'w') as f:
        print(t.render(), file=f)