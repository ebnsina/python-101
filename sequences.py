# List
names = ['Ebn Sina', 'Anas', 'Firnas']

print(names)  # print all names in list
names.sort()  # sort list
names.append('Adam')  # add new item to list


# Tuple
coordinates = (23.8103, 90.4125)

print(coordinates)  # print all names in tuple


# Dict
person = {
    'name': 'ebnsina',
    'age': 100,
    'job': 'software engineer',
    'address': {
        'city': 'Rajshahi',
        'zipcode': '6000'
    }
}

print(person['name'])
print(person['address']['city'])

# Set
s = set()

s.add(1)  # add item to set
s.add(2)  # add item to set
s.add(3)  # add item to set
s.add(4)  # add item to set
s.add(2)  # add item to set

s.remove(3)  # remove item to set

print(s)
