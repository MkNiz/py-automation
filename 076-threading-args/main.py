import threading, time

print("At start of script")

def aThread(n, pause, str, endstr):
    for i in range(n):
        print(str)
        time.sleep(pause)
    print(endstr)
    
thr = threading.Thread(target=aThread, args=[5, 2, "bepis", "thread done"])
thr.start()

print("At end of script")