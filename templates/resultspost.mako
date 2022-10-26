[b][size=18]The results are final![/b][/size]
During the ${c.length} day challenge, we completed [b][color=red]${c.total_tasks_done}[/b][/color] tasks (including doublechecks). 

${c.total_teams} teams and ${c.total_users} individuals participated in the challenge.

[u]Top Three Individuals:[/u]
% for i, user in enumerate(c.top_3_users):
${i+1}. [url=${user[0]}]${user[1]}[/url] with ${user[2]} tasks completed
% endfor

[u]Top Three Teams:[/u]
% for i, team in enumerate(c.top_3_teams):
${i+1}. [url=${team[0]}]${team[1]}[/url] with ${team[2]} tasks completed
% endfor