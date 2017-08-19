import re

rx = re.compile(r'n(orth)?|s(outh)?|e(ast)?|w(est)?')

while(True):
    print("You are in a small, barren room. There are exits to the east and south.")
    u_cmd = input("Where would you like to go?\n~> ")
    if u_cmd == "q" or u_cmd == "quit":
        break
    
    result = rx.search(u_cmd)
    if not result:
        print("I don't know how to '", u_cmd, "'.")
        continue
    
    directive = result.group(0)
    if directive == "n" or directive == "north":
        print("You can't go north from here.")
        continue
    elif directive == "s" or directive == "south":
        print("You open a door and proceed south.")
        break
    elif directive == "e" or directive == "east":
        print("You head down the path to the east.")
        break
    elif directive == "w" or directive == "west":
        print("The way to the west is blocked by debris.")
        continue
    else:
        print("I don't know what's going on.")