import pprint

print("~ [ TODOFOO 64 ] ~")
print("The to-do list of the future\n")

def display_help():
    print("Commands:")
    print("\th - Display this help menu")
    print("\tnew - Re-initialize the to-do list")
    print("\tadd - Add a new task to the to-do list")
    print("\tcheck - Complete the first task in the to-do list, erasing it")
    print("\tstatus - Check the state of the to-do list")
    print("\tsave - Save the to-do list to the disk")
    print("\tload - Load the to-do list from saved data")
    print("\tq - Quit the program")

def add_item(tdl):
    new_item = input("Please enter the item to add to the to-do list (c to cancel):\n~> ")
    if new_item != "c":
        tdl.append(new_item)
        print("Item added to to-do list.")
    return tdl
        
def check_item(tdl):
    if len(tdl) > 0:
        item = tdl.pop(0)
        print("Checked off the item:\n\t", item, "\n")
    else:
        print("There aren't any items to check off.\n")
    return tdl
    
def display_status(tdl):
    print("Current to-do list:")
    for idx, item in enumerate(tdl):
        print("\t", idx+1, ".)", item)
    print("\n")
        
def save_todo(tdl):
    save_file = open('save.py', 'w')
    save_file.write('save_data = ' + pprint.pformat(tdl) + "\n")
    print("Data has been saved.\n")
    
def load_todo():
    import save
    print("Data has been loaded.\n")
    return save.save_data

todo_list = []
while (True):
    cmd = input("Please input your command (h for help):\n~>")
    if cmd == "h":
        display_help()
    elif cmd == "q":
        break
    elif cmd == "new":
        todo_list = []
        print("To-do list has been cleared.\n")
    elif cmd == "add":
        todo_list = add_item(todo_list)
    elif cmd == "check":
        todo_list = check_item(todo_list)
    elif cmd == "status":
        display_status(todo_list)
    elif cmd == "save":
        save_todo(todo_list)
    elif cmd == "load":
        todo_list = load_todo()
    else:
        print("I do not understand '{0}'".format(cmd))
    