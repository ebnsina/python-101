from pprint import pprint

peoples = [
    {"name": "Abu Nasr Al-Farabi", "birth": 872, "death": 950},
    {"name": "Ibn Rushd", "birth": 1126, "death": 1198},
    {"name": "Al Battani", "birth": 858, "death": 929},
    {"name": "Ibn Sina", "birth": 980, "death": 1037},
    {"name": "Ibn Battuta", "birth": 1304, "death": 1369},
    {"name": "Musa Al-Khwarizmi",
        "birth": 780, "death": 850},
    {"name": "Omar Khayyam", "birth": 1048, "death": 1131},
]


# with regular function
# def sort_item(person):
#     return person['birth_year']

# peoples.sort(key=sort_item)


# with lambda function
peoples.sort(key=lambda person: person['birth'])

pprint(peoples)
