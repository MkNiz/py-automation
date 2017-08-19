def valid_mdy(text):
    """Ensures 'text' is in MM/DD/YYYY format"""
    # Basic string checks
    if len(text) != 10:
        return False
    for i in range(0, 2):
        if not text[i].isdecimal():
            return False
    if text[2] != '/':
        return False
    for i in range(3, 5):
        if not text[i].isdecimal():
            return False
    if text[5] != '/':
        return False
    for i in range(6, 10):
        if not text[i].isdecimal():
            return False
    
    # Rudimentary month and day checks
    mm = int(text[:2])
    if mm < 1 or mm > 12:
        return False
    
    dd = int(text[3:5])
    if dd < 1 or dd > 31:
        return False
    
    return True

print("This program checks whether the text you supply is a date in MM/DD/YYYY format.")
txt = input("Please enter input to check:\n~> ")

if valid_mdy(txt):
    print(txt, " is a valid MM/DD/YYYY value.")
else:
    print(txt, " is not a valid MM/DD/YYYY value.")