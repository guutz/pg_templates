import yagmail
try:
    from auth import yagmail_auth
except ImportError:
    yagmail_auth = None
import pickle
from datetime import datetime, timedelta

mail = pickle.load(open('mail_dict.p', 'rb'))
current_n = int((list(mail.keys())[0]-datetime(2022, 11, 3))/timedelta(days=1/25))

def send(n,m):
    with yagmail.SMTP("magpie31415@gmail.com", oauth2_file=yagmail_auth) as yag:
        yag.send(
            to="snoogums@googlegroups.com",
            subject=f"NATE THE SNAKE #{n}",
            contents=m,
        )

dellist = []
for n, t, m in zip(range(len(mail.keys())), mail.keys(), mail.values()):
    if datetime.now() > t:
        print(f"Sending mail #{n+current_n+1} scheduled for {t}")
        send(n+current_n+1, m)
        dellist.append(t)
    else:
        break

for t in dellist:
    del mail[t]
pickle.dump(mail, open('mail_dict.p', 'wb'))
current_n = int((datetime.now()-datetime(2022, 11, 3))/timedelta(days=1/25))
print(f"[{datetime.now()}] {len(mail.keys())} mails remain. Next mail #{current_n+2} in {list(mail.keys())[0]-datetime.now()}. Last mail in {list(mail.keys())[-1]-datetime.now()}.")