import re

# Passing re.I as an argument 
word_filter = re.compile(r'(f)uck|(s)hit|(h)ell', re.I)

inp = input("Say some swears:\n~> ")

print("Original Input:\n\t", inp)
inp = word_filter.sub(r'\1\2\3***', inp)
print("Modified:\n\t", inp)