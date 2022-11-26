import yagmail
try:
    from auth import yagmail_auth
except ImportError:
    yagmail_auth = "yagmail_auth.json"
import pickle
from datetime import datetime, timedelta

time_from_start = datetime.now()-datetime(2022, 11, 25, 23, 22)
n = int(time_from_start/timedelta(minutes=15))
s = str((n+1)*4)
s = "0"*max(0, 5-len(s))+s
contents = [f"<img src='https://storage.googleapis.com/guutz/among-meme/among_{s}.png'>"]

def send(n,m):
    with yagmail.SMTP("magpie31415@gmail.com", oauth2_file=yagmail_auth) as yag:
        yag.send(
            to="snoogums@googlegroups.com",
            subject=f"C͓̽L͓̽U͓̽E͓̽L͓̽E͓̽S͓̽S͓̽ #{n}",
            contents=m,
        )

try:
    n_prev = pickle.load(open("snoogums.p", "rb"))
except EOFError:
    n_prev = 2
for i in range(n_prev+1,n+1):
    if int(s)>=4 and int(s)<=1296:
        send(i, contents)
pickle.dump(n, open("snoogums.p", "wb"))