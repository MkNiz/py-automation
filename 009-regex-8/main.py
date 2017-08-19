import re

# This catches every word that starts with d/D.
rx = re.compile(r'[dD]\w+')
# This catches every word that does not start with d/D, using the caret in the
# custom character class to symbolize negation.
neg_rx = re.compile(r'\b[^dD ]\w+')

u_inp = input("Please provide text to be searched:\n~> ")
d_words = rx.findall(u_inp)
non_d_words = neg_rx.findall(u_inp)

print("\nAll words beginning with D:")
for w in d_words:
    print(w)
    
print("\nAll words not beginning with D:")
for w in non_d_words:
    print(w)