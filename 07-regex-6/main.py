import re

rx = re.compile(r'ban(an)+a')

u_inp = input("Will you give me a nanner?\n~> ")
result = rx.search(u_inp)

if result:
    print("Thanks for the", result.group())
else:
    print("Why didn't you give me a nanner...")