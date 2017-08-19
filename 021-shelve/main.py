import shelve
from pygame.examples.aliens import Player

myShelf = shelve.open('data')

# Storing an integer
numOfBats = 30
myShelf['bats'] = numOfBats

# Storing a string
myGreeting = "Hello, Worm"
myShelf['greeting'] = myGreeting

# Storing a list
myList = ["I'm", "just", "a", "list"]
myShelf['list'] = myList

# Storing a dictionary
myPlayer = { 'name': "Bob", 'level': 1, 'HP': 30, 'MP': 15, 'class': "Janitor" }
myShelf['player'] = myPlayer

myShelf.close()

# Re-opening and reading shelf
myShelf = shelve.open('data')

print("Bats:", myShelf['bats'])
print("Greeting:", myShelf['greeting'])
print("List:")
for itm in myShelf['list']:
    print("\t", itm)
print("Player:")
pl = myShelf['player']
print("\tName:", pl['name'])
print("\tLevel:", pl['level'])
print("\tClass:", pl['class'])
print("\tHP:", pl['HP'])
print("\tMP:", pl['MP'])

myShelf.close()