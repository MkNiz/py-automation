import re

rx = re.compile(r'kick (goblin|chair|can|door|grue|computer)')

print("You are in a sprawling cavern. A goblin is sitting on a chair reading")
print("the newspaper and hasn't noticed you. There is a can on the floor and a door")
print("to your west. It is pitch black to the east. Your computer is acting up.")
print("~> kick")

while(True):
    u_command = input("What would you like to kick?\n~> ")
    if u_command == "q" or u_command == "quit":
        break
    
    result = rx.search(u_command)
    if not result:
        print("I do not understand '", u_command, "'.")
        continue
    
    target = result.group(1)
    print("You kick the", target, "!")
    break
    

