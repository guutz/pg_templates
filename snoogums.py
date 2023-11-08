import yagmail
import arxiv
import random
from datetime import datetime
from dateutil import tz
try:
    from auth import yagmail_auth
except ImportError:
    yagmail_auth = "yagmail_auth.json"


def arxiv_email():
    # Search for the latest paper in the "astro-ph" category (Astrophysics).
    client = arxiv.Client()
    search = arxiv.Search(query="cat:astro-ph", sort_by=arxiv.SortCriterion.SubmittedDate, sort_order=arxiv.SortOrder.Descending, max_results=10000)
    results = client.results(search)
    papers = list(results)

    if papers:
        for i in range(5):
            # Get a random paper from the search results
            random_paper_index = random.randint(0, len(papers) - 1)
            latest_paper = papers[random_paper_index]
            title = latest_paper.title
            published_datetime = latest_paper.published
            link = latest_paper.pdf_url
            abstract = latest_paper.summary
            print("Title of the latest arXiv astrophysics paper:")
            print(title)
            with yagmail.SMTP("magpie31415@gmail.com", oauth2_file=yagmail_auth) as yag:
                yag.send(
                    to="snoogums@googlegroups.com",
                    subject=title,
                    contents=f"""Guys this is huge! Astrophysicists just discovered {title}!!!
                    
                    {link}
                    {str(published_datetime)[:20]}
                    {abstract}
                    
                    If this is legit then we just proved Einstein wrong!!! \(°Ω°)/ ☭ ༼つಠ益ಠ༽つ ─=≡ΣO))""",
                )
    else:
        print("No astrophysics papers found")

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

if __name__ == "__main__":
    # another revolution email if date is before 11/10/2023 4:30pm UTC-8
    if datetime.now().astimezone(tz.gettz("America/Los_Angeles")) < datetime(2023, 11, 10, 16, 30, 0, tzinfo=tz.gettz("America/Los_Angeles")):
        another_revolution_email()
    else:    
        arxiv_email()