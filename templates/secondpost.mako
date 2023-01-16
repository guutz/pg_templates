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

[size=14]The ${c.number} challenge of the [url=https://www.primegrid.com/challenge/challenge.php]${time("%Y")} Series[/url] will be a [b][color=blue]${c.length}-day[/b][/color] challenge ${c.celebrating} The challenge will be offered on the [b]${listem(c.sp,'short_name')}[/b] application${c.s()}, beginning [b][color=green]${c.start}[/b][/color] and ending [b][color=green]${c.end}[/b][/color].[/size]

${c.background}

[b][size=16]To participate in the challenge:[/size][/b][list]
*Wait until the challenge timeframe starts (or set your BOINC Client download schedule accordingly), as tasks issued before the challenge [u]will not count[/u].
*In your [b][url=http://www.primegrid.com/prefs.php?subset=project]PrimeGrid preferences[/url][/b] section, select [u]only[/u] the [u][b]${listem(c.sp,'full_name')}[/b][/u] project${c.s()}.
[/list]

################################## BEGIN REMINDERS
[b][size=16]Important reminders:[/size][/b][list]
% if any(sp.short_name in ['GFN-21','GFN-22','GFN-DYFL'] for sp in c.sp):
*These subprojects require [b]a lot of disk space[/b]; ~[color=violet]1.2GB[/color] for GFN-21, and ~[color=violet]2.5GB[/color] for GFN-22 and DYFL. Your tasks will immediately fail if you don't have enough available storage.
*DYFL tasks are [color=red]NOT[/color] supported for CPU, they are too big. (GFN-21 and GFN-22 are fine.)
*Multi-threading is [b]REQUIRED[/b] for GFN-21 and GFN-22. (Must allocate at least 4 threads per task in your [b][url=http://www.primegrid.com/prefs.php?subset=project]PrimeGrid preferences[/url][/b]. See instructions below.)
% endif
% if any(sp.short_name == 'SR5-LLR' for sp in c.sp):
*[b]NOTE ON SR5 TASKS:[/b] If you've found a prime, the task will take about [u]10 times[/u] as long to run. This is because we always test SR5 candidates with a PRP (probable prime) check first, which runs much quicker. If that comes back positive, that means it's most likely prime but not certain (hence the 'probable'), so we run a full LLR primality test to verify, which takes a lot longer. [b]TL;DR:[/b] If a task is taking an unusually long time, don't abort it!
*This app uses a lot of memory. It requires about 1.3 GB of swap space / virtual memory, and 250 MB of physical memory. SR5 may run up to 4 times slower than other LLR tasks on some older CPUs such as AMD Semprons.
% endif
% if any(sp.short_name == 'SGS-LLR' for sp in c.sp):
*[b][color=indigo]NOTE: If the candidate being tested is indeed prime, the task will take TWICE as long to complete. This is because it's checking for a twin prime![/color][/b]
% endif
% if any(sp.short_name == 'GCW-LLR' for sp in c.sp):
*[b]This app uses a lot of memory. It requires about 1.5 GB of swap space / virtual memory, and 750 MB of physical memory.[/b]
*[b]If you are using Digital Ocean or TheScience.cloud 1GB droplets, you can only run one task at a time.[/b]
% endif
% if any(sp.short_name == 'SOB-LLR' for sp in c.sp):
*[b]NOTE: SOB tasks are [i]very[/i] long.[/b]
% endif
% if any(sp.llr2 for sp in c.sp):
*[color=indigo][b]Note on [url=https://www.primegrid.com/forum_thread.php?id=9303&nowrap=true#143209]LLR2[/url] tasks:[/b] LLR2 has eliminated the need for a full doublecheck task on each workunit, but has replaced it with a short verification task. Expect to receive a few tasks about 1% of normal length. [/color]
% endif
%if any(sp.deadline > c.length for sp in c.sp):
*The typical deadline for some of these WUs is longer than the challenge time-frame, so make sure your computer is able to return the WUs within ${c.length} days. [b]Only tasks issued AFTER the start time and returned BEFORE the finish time will be counted.[/b]
% endif
*[u][color=green]At the Conclusion of the Challenge:[/color][/u] We kindly ask users "moving on" to [color=green][b]ABORT[/b][/color] their tasks instead of DETACHING, RESETTING, or PAUSING. [color=green][b]ABORTING[/b][/color] tasks allows them to be recycled immediately; thus a much faster "clean up" to the end of a Challenge. DETACHING, RESETTING, and PAUSING tasks causes them to remain in limbo until they EXPIRE. Therefore, we must wait until tasks expire to send them out to be completed. Please consider either [b]completing what's in the queue[/b] or [color=green][b]ABORTING[/b][/color] them. Thanks![/list]

############################### BEGIN HARDWARE NOTES
[size=16][b]Let's talk about hardware:[/b][/size][list]
% if any(sp.llr for sp in c.sp):
<%include file="llr_warnings.mako"/>
% endif
% if any('GFN' in sp.short_name for sp in c.sp):
<%include file="gfn_warnings.mako" args="sp_list=c.sp"/>
% endif
[color=red]As with all number crunching, excessive heat can potentially cause permanent hardware failure. Please ensure your cooling system is sufficient. Please see [url=http://www.primegrid.com/forum_thread.php?id=857&nowrap=true#8317]this post[/url] for more details on how you can "stress test" your CPU${", and please see [url=http://www.primegrid.com/forum_thread.php?id=4148]this post[/url] for tips on running GFN on your GPU successfully" if any('GFN' in sp.short_name for sp in c.sp) else ""}.\
% if any('GFN' in sp.short_name for sp in c.sp):

[b]IMPORTANT: Overclocking -- including factory overclocking -- on Nvidia GPUs [u]is very strongly discouraged[/u]. Even if your GPU can run other tasks without difficulty, it may be unable to run GFN tasks when overclocked.[/b][/color]\
% endif
[/list]
<%include file="additional_information.mako" args="start=c.start,end=c.end"/>
% if any('GFN' in sp.short_name for sp in c.sp):
<%include file="GFN.mako"/>
% endif
% if any('PPS' in sp.short_name for sp in c.sp):
<%include file="PPS-MEGA.mako"/>
% endif
% if any('321' in sp.short_name for sp in c.sp):
<%include file="321-LLR.mako"/>
% endif
% if any('SOB' in sp.short_name for sp in c.sp):
<%include file="SOB-LLR.mako"/>
% endif
% if any('SR5' in sp.short_name for sp in c.sp):
<%include file="SR5-LLR.mako"/>
% endif
% if any('SGS' in sp.short_name for sp in c.sp):
<%include file="SGS-LLR.mako"/>
% endif
% if any('GCW' in sp.short_name for sp in c.sp):
<%include file="GCW-LLR.mako"/>
% endif
% if any('CUL' in sp.short_name for sp in c.sp):
<%include file="CUL-LLR.mako"/>
% endif
% if any('WOO' in sp.short_name for sp in c.sp):
<%include file="WOO-LLR.mako"/>
% endif
% if any('TRP' in sp.short_name for sp in c.sp):
<%include file="TRP-LLR.mako"/>
% endif
% if any('ESP' in sp.short_name for sp in c.sp):
<%include file="ESP-LLR.mako"/>
% endif
% if any('PSP' in sp.short_name for sp in c.sp):
<%include file="PSP-LLR.mako"/>
% endif
% if any('AP27' in sp.short_name for sp in c.sp):
<%include file="AP27.mako"/>
% endif
%if any(sp.llr for sp in c.sp):
<%include file="what_is_llr.mako"/>
% endif
% if any(sp.llr2 for sp in c.sp):
<%include file="what_is_llr2.mako"/>
% endif