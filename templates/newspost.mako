<%
from random import choice
from challenge import time
q = [
    'Questions? Queries? Quandries? Quips? Quotations?',
    'Comments? Concerns? Complaints? Critiques? Contemplations?',
    'Inquiries? Ideas? Impressions? Interjections? Inferences?',
    'Ponderings? Predictions? Proclamations? Prognostications?',
    'Remarks? Ruminations? Rants? Revelations? Rhetorical questions?',
    'Anxieties? Anecdotes? Anachronisms? Anomalies? Analogies?',
    'Doubts? Disagreements? Disparities? Disputes? Disquisitions?',
    'Insights? Intimations? Introspections? Intuitions?',
    'Observations? Opinions? Opuscula? Orations? Outbursts?',
    'Suggestions? Suspicions? Sarcasms? Speculations? Syllogisms?',
    'Thoughts? Theories? Tidbits? Truisms? Trivialities?',
    'Worries? Warnings? Whims? Whatevers? Waffles?',
    'Enquiries? Epiphanies? Embellishments? Enigmas?',
    'Hypotheses? Hunches? Hesitations? Histrionics?',
    'Musings? Misgivings? Misunderstandings? Misconceptions?',
    'Confusions? Conclusions? Cautions? Confessions? Conjectures?',
    'Nonplussed? Nostalgic? Nihilistic? Nervous? Newly inspired?',
    'Dilemmas? Dramas? Diversions? Drollery?',
    'Fears? Fantasies? Frustrations? Factualities?',
    'Addendums? Annotations? Apprehensions?',
    'Riddles? Requests? Reservations? Rebuttals?',
]
def listem(l, attr=None):
    if attr:
        l = [getattr(i, attr) for i in l]
    if len(l) == 1:
        return l[0]
    elif len(l) == 2:
        return f"{l[0]} and {l[1]}"
    else:
        return f"{', '.join(l[:-1])}, and {l[-1]}"
%>\
The ${c.number} challenge of the [url=https://www.primegrid.com/challenge/challenge.php]${time("%Y")} Series[/url] will be a [b][color=blue]${c.length}-day[/b][/color] challenge ${c.celebrating} The challenge will be offered on the [b]${listem(c.sp,'short_name')}[/b] application${c.s()}, beginning [b][color=green]${c.start}[/b][/color] and ending [b][color=green]${c.end}[/b][/color].
To participate in the Challenge, please select only the [u][b]${listem(c.sp,'long_name')}[/b][/u] project${c.s()} in your [b][url=http://www.primegrid.com/prefs.php?subset=project]PrimeGrid preferences[/url][/b] section.
${choice(q)} Join the discussion at [url]${c.thread}[/url]