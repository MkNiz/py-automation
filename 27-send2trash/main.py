import send2trash, os.path

if os.path.isfile('trashme.txt'):
    send2trash.send2trash('trashme.txt')
    print("file TRASHED")