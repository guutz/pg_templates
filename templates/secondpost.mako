<%!
from challenge import time
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
######################### BEGIN TEMPLATE
[b][size=18]Welcome to ${c.title}[/size][/b]

The ${c.number} challenge of the [url=https://www.primegrid.com/challenge/challenge.php]${time("%Y")} Series[/url] will be a [b][color=blue]${c.length}-day[/b][/color] challenge ${c.celebrating} The challenge will be offered on the [b]${listem(c.sp,'short_name')}[/b] application${c.s()}, beginning [b][color=green]${c.start}[/b][/color] and ending [b][color=green]${c.end}[/b][/color].

${c.background}

To participate in the Challenge, please select only the [u][b]${listem(c.sp,'long_name')}[/b][/u] project${c.s()} in your [b][url=http://www.primegrid.com/prefs.php?subset=project]PrimeGrid preferences[/url][/b] section.

################################## BEGIN TASK NOTICES
%if any(sp.deadline > c.length for sp in c.sp):
Note: The deadline for these WUs is longer than ${c.length} days, so make sure your computer is able to return the WUs within the challenge time-frame. [b]Only tasks issued AFTER the start time and returned BEFORE the finish time will be counted.[/b]

% endif
% if any(sp.short_name == 'SR5-LLR' for sp in c.sp):
[b]NOTE ON SR5 TASKS:[/b] If you've found a prime, the task will take about [u]10 times[/u] as long to run. This is because we always test SR5 candidates with a PRP (probable prime) check first, which runs much quicker. If that comes back positive, that means it's most likely prime but not certain (hence the 'probable'), so we run a full LLR primality test to verify, which takes a lot longer. [b]TL;DR:[/b] If a task is taking an unusually long time, don't abort it!

% endif
% if any(sp.short_name == 'SGS-LLR' for sp in c.sp):
[b][color=indigo]NOTE: If the candidate being tested is indeed prime, the task will take TWICE as long to complete. This is because it's checking for a twin prime![/color][/b]

% endif
% if any(sp.llr2 for sp in c.sp):
[color=indigo][b]Note on [url=https://www.primegrid.com/forum_thread.php?id=9303&nowrap=true#143209]LLR2[/url] tasks:[/b] LLR2 has eliminated the need for a full doublecheck task on each workunit, but has replaced it with a short verification task. Expect to receive a few tasks about 1% of normal length. [/color]

% endif
############################### BEGIN HARDWARE NOTES
% if any(sp.llr for sp in c.sp):
<%include file="llr_warnings.mako"/>
% endif
% if any('GFN' in sp.short_name for sp in c.sp):
<%include file="gfn_warnings.mako" args="sp_list=c.sp"/>
% endif
############################### BEGIN MULTITHREADING NOTES
<%
mt_msgs = {
    'yes': 'Multi-threading is supported and IS recommended for',
    'yes_app': 'Multi-threading is supported and IS recommended for',
    'slow': 'Multi-threading is supported, but is [color=red]NOT[/color] recommended except for slower computers for',
    'no': 'Multi-threading is [color=red]NOT[/color] supported for'
}
%>
% for sp in c.sp:
[u][b]${mt_msgs[sp.multithread]} ${sp.short_name}.[/b][/u] [color=red](Tasks on one CPU core take about ${sp.cpu_time} on average.)[/color]
% endfor

% if any(sp.multithread != 'no' for sp in c.sp):
Those looking to maximize ${'a very old' if c.sp[0].multithread == 'slow' else 'their'} computer's performance during this challenge, or when running${' Genefer and' if 'GFN' in c.sp[0].short_name else ''} LLR in general, may find this information useful.[list]
% endif
### BRANCH FOR DIFFERENT MULTITHREADING OPTIONS
<%include file="multithread_instructions.mako" args="mt=c.sp[0].multithread"/>
###################################### THE OUTRO
<%include file="time_zone_converter.mako"/>
<%include file="scoring_information.mako" args="start=c.start,end=c.end"/>
<%include file="at_the_conclusion.mako"/>
######################### FURTHER READING
% for sp in c.sp:
<%include file="${sp.short_name}.mako"/>
% endfor
########################## PROGRAMS
%if c.sp[0].llr:
<%include file="what_is_llr.mako"/>
% endif
% if c.sp[0].llr2:
<%include file="what_is_llr2.mako"/>
% endif


