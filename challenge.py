import argparse
from bs4 import BeautifulSoup
import requests
from mako.lookup import TemplateLookup as MakoTemplateLookup
from datetime import datetime, timedelta
import yaml
import logging

logging.basicConfig(level=logging.INFO)

YES = 'yes'
NO = 'no'
SLOW = 'slow'
YES_APP = 'yes_app'
CPU = 'CPU'
GPU = 'GPU'

subprojects = yaml.safe_load(open('subprojects.yaml', 'r', encoding="utf-8"))

def time(s):
    return datetime.now().strftime(s)

class yaml_boi:
    def __init__(self, file=None):
        self.file = file if file else f"challenges{time('%Y')}.yaml"
        self.data = []
        try:
            with open(self.file,'r') as f:
                self.data = yaml.load(f, Loader=yaml.FullLoader)
                if self.data is None: self.data = []
            logging.info(f"Loaded {self.file}")
        finally:
            self.update_challenges()
    
    def __getitem__(self, key):
        if isinstance(key, str):
            return [ch for ch in self.data if key in ch['title']][0]
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
        self.save()
    
    def save(self):
        with open(self.file, 'w') as f:
            yaml.dump(self.data, f, default_flow_style=False)

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def append(self, item):
        self.data.append(item)
        self.save()
    
    def update_challenges(self):
        logging.info("Requesting challenge.php")
        r = requests.get('https://www.primegrid.com/challenge/challenge.php')
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find(id='table4')
        logging.info("Parsing challenge.php")
        rows = table.find_all('tr')
        master_list = []
        for tr in rows[2:-2]:
            l = []
            for td in list(tr)[:-1]:
                l.append(td.text if hasattr(td, 'text') else td)
            link = tr.find('x')
            l.append("https://www.primegrid.com"+(link['href'] if link else '/forum_post.php?id=2'))
            master_list.append(l)

        def extract_start_time(challenge):
            from parse import parse
            time_str = challenge[1] + " " + challenge[2]
            if ((res := parse("{day:d}-{:d} {month} {hour:d}:{minute:d}:{second:d}", time_str)) is not None):
                time_data = res.named
            else:
                time_data = parse("{day:d} {month} - {:d} {} {hour:d}:{minute:d}:{second:d}", time_str).named
            time_data["month"] = datetime.strptime(time_data["month"], "%B").month
            dt = datetime(1900, **time_data)
            return dt.strftime('%m/%d %H:%M')

        for i, challenge in enumerate(master_list):
            if i >= len(self): self.append({})
            d = self[i]
            d['number'] = int(challenge[0])
            d['start_time'] = extract_start_time(challenge)
            d['sp'] = []
            for sp in subprojects:
                if sp in challenge[3]:
                    d['sp'].append(sp)
            d['title'] = challenge[4]
            d['length'] = int(challenge[5].split(' ')[0])
            d['celebrating'] = "celebrating TODO!"
            d['background'] = "TODO!"
            d['thread'] = challenge[6]
            if 'updates' not in d: logging.info(f"Initializing updates field for {d['title']}")
            d['updates'] = {
                'first': False,
                'second': False,
                'news': False,
                'stats': False,
                'cleanup': False,
                'results': False
            } if 'updates' not in d else d['updates']
            self[i] = d

    def get_needed_updates(self):
        logging.info("Getting needed updates")
        now = datetime.now()

        def challenge_timeline(ch):
            start = datetime.strptime(f"{ch['start_time']} {time('%Y')}", '%m/%d %H:%M %Y')
            return dict(
                # the dates after which we need to worry about each item
                first = start + timedelta(weeks=999),
                second = start - timedelta(weeks=2),
                news = start - timedelta(days=3),
                stats = start,
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

        for challenge in self:
            t = challenge_timeline(challenge)
            for u, s in challenge['updates'].items():
                if s == False and now > t[u]:
                    ups[u].append(challenge['title'])
                    logging.info(f"Need to do {u} for {challenge['title']}")

        return ups

class Challenge:

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

    class Subproject:
        def __init__(self, name):
            self.name = name
            for key, value in subprojects[name].items():
                setattr(self, key, value)
        
        @property
        def cpu_time(self):
            hms = self.get_time(CPU)
            if hms is None: return None
            hms = hms.split(':')
            if int(hms[0]) == 0:
                return f"{hms[1].strip('0')} minutes"
            if int(hms[0]) < 48:
                return f"{hms[0].strip('0')} hours"
            if int(hms[0]) < 24*13:
                return f"{int(hms[0])//24} days"
            return f"{int(hms[0])//168} weeks"
                
        @property
        def gpu_time(self):
            hms = self.get_time(GPU)
            if hms is None: return None
            hms = hms.split(':')
            if int(hms[0]) == 0:
                return f"{hms[1].strip('0')} minutes"
            if int(hms[0]) < 48:
                return f"{hms[0].strip('0')} hours"
            if int(hms[0]) < 24*13:
                return f"{int(hms[0])//24} days"
            return f"{int(hms[0])//168} weeks"

        def _get_prefs_page(self):
            try:
                from auth import strong_key
            except ImportError:
                import os
                strong_key = os.environ['STRONG_KEY']
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
            

    def __init__(self, title, number, length, celebrating, sp, start_time, background, thread=None, **kwargs):
        self.title = title if "'s" in title else "the "+title
        self.number_int = number
        self.number = self.ths[number]
        self.length = length
        self.celebrating = celebrating
        self.sp = [self.Subproject(s) for s in sp]
        self._start_time_object = datetime.strptime(start_time, '%m/%d %H:%M')
        self._end_time_object = self._start_time_object + timedelta(days=self.length)
        self.start = self._start_time_object.strftime('%d %B %H:%M UTC')
        self.end = self._end_time_object.strftime('%d %B %H:%M UTC')
        self.background = background
        self.thread = thread
    
    def s(self):
        return 's' if len(self.sp)>1 else ''

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
        logging.info(f"Initializing new challenge yaml file: {outfile}")
        y = yaml_boi(file=outfile)
        exit()
    if template:
        y = yaml_boi()
        c = Challenge(**y[template])
    if not outfile:
        outfile = template.split('.')[0] + '.txt'
    mtl = MakoTemplateLookup(directories=["", "project_overviews/", "templates/"])
    
    outputs = []
    for post in posts:
        file = outfile.split('.')[0] + '_' + post + ('.txt' if len(outfile.split('.')) == 1 else '.' + outfile.split('.')[1])
        logging.info(f"Writing {c.title}: {post} to {file}")
        with open(file, 'w+', encoding="utf-8") as f:
            r = c.title + '\n\n'
            r += mtl.get_template(post + '.mako').render(c=c)
            r += '\n\n'+c.thread
            print(r,file=f)
            outputs.append(r)
    return outputs
        


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--init', default=None, help='initialize template')
    argparser.add_argument('-t', '--template', default=None, help='use template')
    argparser.add_argument('-o', '--outfile', default=None, help='output file')
    argparser.add_argument('-p', '--posts', nargs='+', default=['firstpost','secondpost','newspost'], help='generate posts')
    args = argparser.parse_args()
    args = vars(args)
    main(**args)