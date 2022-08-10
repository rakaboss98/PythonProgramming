from multiprocessing import Process
from multiprocessing.dummy import freeze_support
import time
import os 

# count the number of available cpus
num_process = os.cpu_count()
process = []


def func():
    for i in range(100):
        i*i
        time.sleep(1)

if __name__ == '__main__':
    freeze_support()
    # Create process 
    for i in range(num_process):
        p = Process(target=func)
        process.append(p)

    # Start process
    for p in process:
        p.start()

    # join 
    for p in process:
        p.join()
    print('end main')
