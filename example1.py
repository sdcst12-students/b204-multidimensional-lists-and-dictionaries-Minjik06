#!python

pokemon = {
    'name' : 'Tinkatink',
    'category' : 'Metalsmith',
    'types' : ['Fairy','Steel'],
    'hp' : 3,
    'attack' : 3,
    'defense' : 3,
    'spAtk' : 3,
    'spDef' : 4,
    'speed' : 4
}

pokedex = []
pokedex.append(pokemon)

# note we can also append a dictionary inline:
pokedex.append({
    'name' : 'Hippowdon',
    'category' : 'Heavyweight',
    'types' : ['Ground'],
    'hp' : 7,
    'attack' : 7,
    'defense' : 7,
    'spAtk' : 4,
    'spDef' : 5,
    'speed' : 3
})
print("Raw list output of entire pokedex")
print(pokedex)
print("-")

print("Raw output of single entry from pokedex")
print(pokedex[0])
print("-")

print("Raw output of select items in pokedex entry")
print("Name",pokedex[1]['name'])
print("Types",pokedex[1]['types'])
print("Raw output of single entry from a specific type")
print("Type[0]",pokedex[1]['types'][0])
print("-")

print("use of for loop to display all the names")
for i in pokedex:
    print(i['name'])
print('-')

print('use of for loop on a list buried in the dictionary in the list')
print(f"{pokedex[0]['name']} is of the following types:")
for i in pokedex[0]['types']:
    print(i)

# 