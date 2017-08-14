import threading, time

print("At start of script")

def aThread():
    for i in range(1, 11):
        print("Loop #", i, "in aThread")
        time.sleep(1)
    print("Finished looping in aThread")
    
thr = threading.Thread(target=aThread)
thr.start()

print("At end of script")
    