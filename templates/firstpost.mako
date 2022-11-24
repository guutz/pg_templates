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
<<<< to celebrate ___, >>>> PrimeGrid will have a [b]${c.length}-day[/b] challenge on the [b]${listem(c.sp,'short_name')}[/b] subproject${c.s()} from [b][color=green]${c.start}[/b][/color] to [b][color=green]${c.end}[/b][/color].

...

More details to follow. Happy crunching!