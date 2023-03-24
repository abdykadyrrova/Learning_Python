# my_string = "Hello World!"
# print(type(my_string))

# my_integer = 123
# print(type(my_integer))

# my_list = ['abdul']
# my_list.append('ahmad')
# print(type(my_list))

# pet = {'name': 'cookie', 'age': 2, 'home': 'Chicago'}
# print(pet['name'], pet['age'])

# math = 2+2
# print(bool(math))

pets = [
    {
        'name': 'cookie', 
        'age': 2, 
        'home': 'Chicago', 
        'kind': 'cat',
        'toys': ['carrot', 'bunny', 'ball']
    },
    {
        'name': 'Jessie', 
        'age': 5, 
        'home': 'Turkey', 
        'kind': 'dog'
    }
]
first_toy = pets[0]['toys'][0]

for pet in pets:
    if pet['name'] == 'cookie':
        print('My pet is here!')




