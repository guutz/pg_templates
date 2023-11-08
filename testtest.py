import random

with open("Another Revolution.txt", "r", encoding="ascii", errors="ignore") as f:
    contents = f.readlines()

# find a random line that starts with either "KAT" or "HENRY" (case sensitive)
line = ""
while not line.startswith(("KAT", "HENRY")):
    line = random.choice(contents)

line_plus_first_word = line.split(" ", 4)[:-1]

print(" ".join(line_plus_first_word))