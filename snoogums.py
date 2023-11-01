import yagmail
import arxiv
try:
    from auth import yagmail_auth
except ImportError:
    yagmail_auth = "yagmail_auth.json"

# Search for the latest paper in the "astro-ph" category (Astrophysics).
papers = arxiv.Search(query="cat:astro-ph", sort_by=arxiv.SortCriterion.SubmittedDate, sort_order=arxiv.SortOrder.Ascending, max_results=10)

if papers:
    latest_paper = next(arxiv.Client().results(papers))
    title = latest_paper.title
    published_datetime = latest_paper.published
    link = latest_paper.pdf_url
    abstract = latest_paper.summary
    print("Title of the latest arXiv astrophysics paper:")
    print(title)
    with yagmail.SMTP("magpie31415@gmail.com", oauth2_file=yagmail_auth) as yag:
        yag.send(
            to="findmagpie@gmail.com",
            subject=title,
            contents=f"""Guys this is huge! Astrophysicists just discovered {title}!!!
            
            {link}
            {str(published_datetime)[:20]}
            {abstract}""",
        )
else:
    print("No astrophysics papers found")
