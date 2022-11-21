from challenge import yaml_boi, main, time
from get_cleanup import main as info
import logging

logging.basicConfig(level=logging.INFO)

y = yaml_boi()

email_contents=[]

for u, chs in y.get_needed_updates().items():
    for ch in chs:
        if u == 'stats':
            logging.info(f" {u} update for {ch}")
            with open(f"{time('%Y-%m-%d')}.txt", 'a') as f:
                i = info(update=True, name=ch.split(" ")[0])
                if i == 'EMPTY':
                    y[ch]['updates']['stats'] = True
                else:
                    print(i, file=f)
                    email_contents.append(i)
        elif u == 'cleanup':
            logging.info(f" {u} update for {ch}")
            with open(f"{time('%Y-%m-%d')}.txt", 'a') as f:
                i = info(cleanup=True, name=ch.split(" ")[0])
                if i == 'EMPTY':
                    y[ch]['updates']['cleanup'] = True
                else:
                    print(i, file=f)
                    email_contents.append(i)
        elif (u == 'results' and y[ch]['updates']['cleanup'] == True) or (u != 'results'):
            logging.info(f" {u} update for {ch}")
            i = main(
                template=ch,
                posts=[u+"post"]
            )
            email_contents.append(*i)
            y[ch]['updates'][u] = True
y.save()

mail="""#######################################\n#######################################\n"""
if email_contents:
    for i in email_contents:
        mail+=str(i)
        mail+='\n#######################################\n#######################################\n'
    if mail.count('TODO!') > 0:
        mail = "SOME STUFF NEEDS TO BE FILLED IN HERE FIRST!\n\n#######################################\n#######################################\n" + mail
else:
    mail = "There's nothing here!"

import yagmail
try:
    from auth import yagmail_auth
except ImportError:
    yagmail_auth = "yagmail_auth.json"

with yagmail.SMTP("magpie31415@gmail.com", oauth2_file=yagmail_auth) as yag:
    yag.send(
        to="mgutierrez@primegrid.com",
        subject=f"PG {time('%Y-%m-%d')}",
        contents=mail,
    )