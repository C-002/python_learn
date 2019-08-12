import _thread as thread
import time

stdoutmutex = thread.allocate_lock()
numthread = 5
exitmutexes = [thread.allocate_lock() for i in range(numthread)]

def counter(myId, count, mutex):
    for i in range(count):
        time.sleep(1 / (myId + 1))
        with mutex:
            print('[%s] => %s' % (myId, i))
    exitmutexes[myId].acquire()

for i in range(numthread):
    thread.start_new_thread(counter, (i, 5, stdoutmutex))

while not all(mutex.locked() for mutex in exitmutexes): pass

print('Main thread exiting!')
