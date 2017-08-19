import time

def doSomethingArbitrary():
    foo = 10
    for i in range(0, 999999):
        foo += (i / 2) - (777)

start = time.time()
print("Doing arbitrary busywork...")
doSomethingArbitrary()
end = time.time()

timeResult = str(end - start)

print("Arbitrary busywork took " + timeResult + " seconds.")