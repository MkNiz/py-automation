import re

rx_please = re.compile(r'^[P|p]lease')
rx_thanks = re.compile(r'([T|t]hanks)|([T|t]hank you)(\.)?$')

u_inp1 = input("If you don't say please first, I won't listen.\n~> ")
result1 = rx_please.search(u_inp1)

if result1:
    print("Alright, I heard you.")
else:
    print("What was that? Sounded like an ungrateful mouse.")
    
u_inp2 = input("If you don't say thank you last, I'll scream.\n~> ")
result2 = rx_thanks.search(u_inp2)

if result2:
    print("Phew, glad you listened.")
else:
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")