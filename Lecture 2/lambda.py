people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# all of this can be simplified to a lambda function

# def f(person):
#     return person["name"]
    # can be used for "house" also

# tell the sort function how to sort
people.sort(key= lambda person: person["house"])

print(people)