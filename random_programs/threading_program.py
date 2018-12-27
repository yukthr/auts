import threading
import os
import time


clients = ['4.2.2.2','8.8.8.8','www.goolge.com']

def os_ping(i):
    os.system('ping {} -c 5'.format(i))

threads = []


def without_threading():
    total_time = 0.0
    print('\n This is not using threading')
    for j in clients:
        t1 = time.time()
        os_ping(j)
        t2 = time.time()
        total_time += (t2-t1)

    print('\nTotal time without using threading: {}\n'.format(total_time))

def using_threading():
    total_time = 0.0 #Time measurement
    print('\nThis is using threading')
    for j in clients:
        t1 = time.time() # Time before start
        t = threading.Thread(target=os_ping,args=(j,))
        t.start()
        threads.append(t)
        t2 = time.time() #Time afterexecution
        total_time += (t2-t1)

    for thread in threads:
        thread.join()

    print('\nTotal Time using threading: {}\n'.format(total_time))

without_threading()
using_threading()
