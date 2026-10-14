import re

with open("story.txt", "rt") as f:
    story = f.read().upper()

words = re.findall(r'\w+', story)

for word in sorted(set(words)):
    print(word)


