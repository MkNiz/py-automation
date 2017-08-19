import re

greedy_rx = re.compile(r'(hee){1,4}')
nongreedy_rx = re.compile(r'(hee){1,4}?')

u_inp = input("Gimme some 'hee's.\n~> ")
greed_result = greedy_rx.search(u_inp)
ungreed_result = nongreedy_rx.search(u_inp)

if greed_result:
    print("Nice", greed_result.group())

if ungreed_result:
    print("Very nice", ungreed_result.group(), "indeed.")

if not greed_result and not ungreed_result:
    print("That's an illegal way to hee.")