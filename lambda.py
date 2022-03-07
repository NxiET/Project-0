people = [ 
    {"name": "Harry", "house": "Griffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Droco", "house": "Slytherin"},
]

people.sort(key=lambda person: person["name"])

print(people)