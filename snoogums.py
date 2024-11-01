import yagmail
# import arxiv
import feedparser
from bs4 import BeautifulSoup
import requests
import pymupdf
import random
from datetime import datetime, timedelta
from dateutil import tz, parser
try:
    from auth import yagmail_auth
except ImportError:
    yagmail_auth = "yagmail_auth.json"

random.seed(68419)
clase = [
    "class",
    "clase",
    "fellows",
    "darbs",
    "comrades",
    "friends",
    "compatriots",
    "colleagues",
    "gorls",
    "ladies, gentlemen, and members of the jury",
    "students",
    "scholars",
    "scientists",
    "researchers",
    "academics",
    "learners",
    "enthusiasts",
    "nerds",
    "geeks",
    "dorks",
    "frosh",
    "freaks",
    "[de]mentees",
    "pals",
    "lovelies",
    "crewmates",
    "fellow travelers",
    "fellow 4-dimensional sausages",
    "bros",
    "sisters",
    "you cool cats and kittens",
    "you beautiful people",
    "cuties",
    "people",
    "folks",
    "peeps",
    "homies",
    "children of the night",
    "sleepyheads",
    "dreamers",
    "believers",
    "achievers",
    "schemers",
    "Techers",
    "Caltechians",
    "Caltechers",
    "Caltechites",
    "CalTechers",
    "underlings",
    "minions",
    "subordinates",
    "subalterns",
    "marmots",
    "lemmings",
    "squirrel hunters",
    "adequates",
    "mateys",
    "yookeroos",
    "amigos",
    "compadres",
    "sussy frosh",
    "impostors",
    "delightful individuals",
    "smelly meat sacks",
    "sentients",
    "fellow space travelers",
    "friends (and might i just say, you're looking particularly crunchy today)",
    "fellow knowledge seekers",
    "fellow kids",
    "queers",
    "queef biscuits",
    "you ragtag gang of whippersnappers",
    "youths",
    "sociopaths",
    "schizophrenics",
    "fellow neurotypical individuals",
    "besties",
]
random.shuffle(clase)

# def arxiv_email():
#     # Search for the latest paper in the "astro-ph" category (Astrophysics).
#     client = arxiv.Client()
#     search = arxiv.Search(query="cat:astro-ph", sort_by=arxiv.SortCriterion.SubmittedDate, sort_order=arxiv.SortOrder.Descending, max_results=10000)
#     results = client.results(search)
#     papers = list(results)

#     if papers:
#         for i in range(5):
#             # Get a random paper from the search results
#             random_paper_index = random.randint(0, len(papers) - 1)
#             latest_paper = papers[random_paper_index]
#             title = latest_paper.title
#             published_datetime = latest_paper.published
#             link = latest_paper.pdf_url
#             abstract = latest_paper.summary
#             print("Title of the latest arXiv astrophysics paper:")
#             print(title)
#             with yagmail.SMTP("magpie31415@gmail.com", oauth2_file=yagmail_auth) as yag:
#                 yag.send(
#                     to="snoogums@googlegroups.com",
#                     subject=title,
#                     contents=f"""Guys this is huge! Astrophysicists just discovered {title}!!!
                    
#                     {link}
#                     {str(published_datetime)[:20]}
#                     {abstract}
                    
#                     If this is legit then we just proved Einstein wrong!!! \(°Ω°)/ ☭ ༼つಠ益ಠ༽つ ─=≡ΣO))""",
#                 )
#     else:
#         print("No astrophysics papers found")

def another_revolution_email():
    with open("Another Revolution.txt", "r", encoding="ascii", errors="ignore") as f:
        contents = f.readlines()
    
    # find a random line that starts with either "KAT" or "HENRY" (case sensitive)
    line = ""
    while not line.startswith(("KAT", "HENRY")):
        line = random.choice(contents)

    line_index = contents.index(line)

    line_plus_first_word = " ".join(line.split(" ", 4)[:-1])

    with yagmail.SMTP("magpie31415@gmail.com", oauth2_file=yagmail_auth) as yag:
        yag.send(
            to="snoogums@googlegroups.com",
            subject=f"Another Revolution Sneak Preview #{line_index}",
            contents=f"""
            {line_plus_first_word}

            ---

            "Do you like beans? Do you like logical conundrums? Do you like explosions in petri dishes?"

Please come join me and Skyler Ware G6 as we struggle with friendship, ambition and world events on stage in Beckman Institute Auditorium opening WEDNESDAY 11/8 at 7:30pm for three shows: 

Wednesday November 8, 7:30pm
Thursday November 9, 7:30pm
Friday November 10, 4:30pm
Location: Beckman Institute Auditorium

Kat and Henry, two graduate students (one a botanist from a working-class family and the other a theoretical physicist from a wealthy one) are forced to share a lab at Columbia University in 1968. Amid interpersonal differences, a campus devolving into political chaos, and the uncertainty and turmoil of the outside world, they each discover what it’s like to be thrown into someone else’s orbit.
            """
        )

def tech_email():
    d = feedparser.parse("https://campuspubs.library.caltech.edu/cgi/exportview/publication/California_Tech/California_Tech/RSS2/California_Tech_California_Tech.xml")
    index_current = len(d['entries']) - get_index() - 1
    index = min(index_current, read_index())
    title = d['entries'][index]['title']
    libpage = requests.get(d['entries'][index]['id'])
    if libpage.status_code == 200:
        soup = BeautifulSoup(libpage.content, 'html.parser')
        # look for the first <a> tag with the text 'PDF' or 'pdf'
        pdf = soup.find('a', string=lambda x: x and 'pdf' in x.lower())
        if pdf:
            print(pdf['href'])

            # Fetch the PDF file
            pdf_response = requests.get(pdf['href'])
            if pdf_response.status_code == 200:
                with open('temp.pdf', 'wb') as f:
                    f.write(pdf_response.content)
                
                # Open the PDF file
                pdf_document = pymupdf.open('temp.pdf')
                
                # Get the first page
                first_page = pdf_document.load_page(0)
                
                # Convert the first page to an image
                pix = first_page.get_pixmap()
                pix.save('first_page.png')
        with yagmail.SMTP("magpie31415@gmail.com", oauth2_file=yagmail_auth) as yag:
            yag.send(
                to="snoogums@googlegroups.com",
                subject=f"[DEI 169] From the Archives #{index}: {title}",
                contents=[
                    f"Hi {clase[index]},\n",
                    f"READING ASSIGNMENT #{index}:\n====================\n\n{title}\n\n{pdf['href']}\n\n",
                    yagmail.inline("first_page.png")
                ]
            )
        increment_index()

def get_index():
    pacific_tz = tz.gettz('America/Los_Angeles')
    current_time_utc = datetime.now(tz=tz.tzutc())
    current_time_pacific = current_time_utc.astimezone(pacific_tz)
    beginning_of_november = datetime(2024, 11, 1, 0, 0, 0, tzinfo=pacific_tz)
    time_difference = current_time_pacific - beginning_of_november
    # Calculate the number of 20-minute intervals
    i = time_difference.total_seconds() // (20 * 60)
    assert i >= 0, "It is not November yet"
    return int(i)

def read_index():
    try:
        with open("index.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0
    
def increment_index():
    with open("index.txt", "a") as f:
        f.write(str(read_index() + 1))

def error_email(e):
    with yagmail.SMTP("magpie31415@gmail.com", oauth2_file=yagmail_auth) as yag:
        yag.send(
            to="snoogums@googlegroups.com",
            subject=f"Guutz's code sucks",
            contents=[
                "Guutz's code sucks and threw this error:",
                str(e),
                "https://github.com/guutz/pg_templates/blob/main/snoogums.py"
            ]
        )

if __name__ == "__main__":
    # another revolution email if date is before 11/10/2023 4:30pm UTC-8
    # if datetime.now().astimezone(tz.gettz("America/Los_Angeles")) < datetime(2023, 11, 10, 16, 30, 0, tzinfo=tz.gettz("America/Los_Angeles")):
    #     another_revolution_email()

    try:
        tech_email()
    except Exception as e:
        error_email(e)
