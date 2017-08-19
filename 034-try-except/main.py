inp = input("Enter a number:\n~> ")
n = False
try:
    n = int(inp)
except ValueError:
    print("That's no number...")
    
if n:
    print("The number was", n)