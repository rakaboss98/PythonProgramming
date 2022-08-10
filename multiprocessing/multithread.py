from threading import Thread 
import os 
import time 

num_thread = 10 
thread = []

def func():
    for i in range(100):
        i*i
        time.sleep(0.1)

for i in range(num_thread):
    t = Thread(target=func)
    thread.append(t)

for t in thread:
    t.start()

for t in thread:
    t.join()

print('concluding process')