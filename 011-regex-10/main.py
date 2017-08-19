import re

# Wildcard will match any character.
# In this case, it matches the three characters before any occurence of
# the characters 'bat', but only if three characters precede it.
rx = re.compile(r'...bat')

inp = input("Provide a phrase:\n~> ")

result = rx.findall(inp)

print("\nMatches:")
for match in result:
    print(match)