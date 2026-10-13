import json

d = {'title': 'Generative AI', 'duration': 24}
j = json.dumps(d)
print(j)

courses = [{'title': "Python", 'duration': 30},
           {'title': "Generative AI", 'duration': 24},
           {'title': "Java", 'duration': 30}
           ]

with open("courses.json", "wt") as f:
    json.dump(courses, f)
