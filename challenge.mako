<%!
from challenge import time
%>\
######################### BEGIN TEMPLATE
[b][size=18]Welcome to ${c.title} Challenge[/size][/b]

The ${c.number} challenge of the [url=https://www.primegrid.com/challenge/challenge.php]${time("%Y")} Series[/url] will be a [b][color=blue]${c.length}-day[/b][/color] challenge ${c.celebrating} The challenge will be offered on the [b]${c.sp.short_name}[/b] application, beginning [b][color=green]${c.start}[/b][/color] and ending [b][color=green]${c.end}[/b][/color].

${c.background}

To participate in the Challenge, please select only the [u][b]${c.sp.long_name}[/b][/u] project in your [b][url=http://www.primegrid.com/prefs.php?subset=project]PrimeGrid preferences[/url][/b] section.

################################## BEGIN TASK NOTICES
%if c.sp.deadline > c.length: 
Note: The deadline for these WUs is longer than ${c.length} days, so make sure your computer is able to return the WUs within the challenge time-frame. [b]Only tasks issued AFTER the start time and returned BEFORE the finish time will be counted.[/b]

% endif
% if c.sp.short_name == 'SR5-LLR':
[b]NOTE ON SR5 TASKS:[/b] If you've found a prime, the task will take about [u]10 times[/u] as long to run. This is because we always test SR5 candidates with a PRP (probable prime) check first, which runs much quicker. If that comes back positive, that means it's most likely prime but not certain (hence the 'probable'), so we run a full LLR primality test to verify, which takes a lot longer. [b]TL;DR:[/b] If a task is taking an unusually long time, don't abort it!

% endif
% if c.sp.short_name == 'SGS-LLR':
[b][color=indigo]NOTE: If the candidate being tested is indeed prime, the task will take TWICE as long to complete. This is because it's checking for a twin prime![/color][/b]

% endif
% if c.sp.llr2:
[color=indigo][b]Note on [url=https://www.primegrid.com/forum_thread.php?id=9303&nowrap=true#143209]LLR2[/url] tasks:[/b] LLR2 has eliminated the need for a full doublecheck task on each workunit, but has replaced it with a short verification task. Expect to receive a few tasks about 1% of normal length. [/color]

% endif
############################### BEGIN HARDWARE NOTES
% if c.sp.llr:
<%include file="llr_warnings.mako"/>
% endif
% if 'GFN' in c.sp.short_name:
<%include file="gfn_warnings.mako" args="'${c.sp.cpu_time}', '${c.sp.gpu_time}', '${c.sp.short_name}'"/>
% endif
############################### BEGIN MULTITHREADING NOTES
<%
mt_msgs = {
    'yes': 'Multi-threading is supported and IS recommended.',
    'yes_app': 'Multi-threading is supported and IS recommended.',
    'slow': 'Multi-threading is supported, but is [color=red]NOT[/color] recommended except for slower computers.',
    'no': 'Multi-threading is [color=red]NOT[/color] supported for this subproject.'
}
%>\
[u][b]${mt_msgs[c.sp.multithread]}[/b][/u] [color=red](${c.sp.short_name} tasks on one CPU core take about ${c.sp.cpu_time} on average.)[/color]

% if c.sp.multithread != 'no':
Those looking to maximize ${'a very old' if c.sp.multithread == 'slow' else 'their'} computer's performance during this challenge, or when running${' Genefer and' if 'GFN' in c.sp.short_name else ''} LLR in general, may find this information useful.[list]
% endif
### BRANCH FOR DIFFERENT MULTITHREADING OPTIONS
<%include file="multithread_instructions.mako" args="mt='${c.sp.multithreading}'"/>
###################################### THE OUTRO
<%include file="time_zone_converter.mako"/>
<%include file="scoring_information.mako" args="start='${c.start}', end='${c.end}'"/>
<%include file="at_the_conclusion.mako"/>
######################### FURTHER READING
<%include file="${c.sp.short_name}.mako"/>
########################## PROGRAMS
%if c.sp.llr:
<%include file="what_is_llr.mako"/>
% endif
% if c.sp.llr2:
<%include file="what_is_llr2.mako"/>
% endif


